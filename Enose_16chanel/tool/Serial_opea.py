import tool.frame_data as frame_data
import threading
import time, copy
import global_var as glo_var
from PySide6.QtCore import QObject, Signal
from PySide6.QtWidgets import QWidget, QFileDialog, QApplication
from PySide6.QtGui import  QTextCursor


class MySignals(QObject):
    # 定义一种信号，两个参数 类型分别是： QTextBrowser 和 字符串
    # 调用 emit方法 发信号时，传入参数 必须是这里指定的 参数类型
    _Currtem_spinBox = Signal(float) # 更新当前温度
    _statues_label = Signal(str)
    _ClearDraw = Signal()
    _print = Signal(int)


ms = MySignals()


class Action():
    def __init__(self, ui: QWidget) -> None:
        self.ui = ui

    def _Currtem_spinBox(self, value: float):
        self.ui.Currtem_spinBox.setValue(value) #不断更新现在温度

    def _statues_label(self, text: str):
        self.ui.statues_label.setText(text)

    def _ClearDraw(self):
        self.ui.data = [[] for _ in range(self.ui.data_len)]
        self.ui.alldata = copy.deepcopy(self.ui.data)

    def _print(self, time: int):
        print(time)


class time_thread(): # 时间相关的线程
    # 初始化输入两个串口， 停止时间与初始时间
    def __init__(self,ser, ser1,  ui = None, stoptime = 0, starttime = 0):
        self.time = starttime
        self.ui = ui
        self.a = Action(self.ui)
        self.initMS()
        self.stoptime = stoptime
        self.lock = threading.Lock()  # 创建一个锁
        self._stop_evt = threading.Event()  # 用来打断 sleep
        self._running = True
        self.opea = None # 串口操作
        self.ser = ser
        self.ser1 = ser1
        self.timeout = 1000; # 循环时间

    def initMS(self):
        ms._Currtem_spinBox.connect(self.a._Currtem_spinBox)
        ms._statues_label.connect(self.a._statues_label)
        ms._ClearDraw.connect(self.a._ClearDraw)
        ms._print.connect(self.a._print)

    def thread_loopfun(self, fun, timeout=1000): # 输入要循环的函数和循环时间
        # self.time = 0
        try:
            with self.lock:
                self.timeout = timeout
                self._running = True
                self._thread = threading.Thread(
                    target=fun,
                    daemon=True
                )
                self._thread.start()
                return 0, f"开始计时，每{timeout}ms触发一次\n"
        except Exception as e:
            return 1, f"计时失败：{e}\n"

    def loop_to_target_temp(self): # 每1s读取一次温度，直到达到合适温度glo_var.target_temp
        while self._running:
            # 线程安全：把值读出来再比较
            target = self.ui.Heattep_SpinBox.value()
            # print("现在温度是：", glo_var.now_temp)
            ms._Currtem_spinBox.emit(glo_var.now_temp)
            self.ser1.serialSend(2, glo_var.channal[1])
            self.time += 1
            if target <= glo_var.now_temp:  # 当目标温度达成
                print("达到目标温度需要时间：",self.time)
                self.ui.attendtime_spinBox.setValue(self.time)
                self.opea = time_opea(self.ui, self.time, self.ser,self.ser1,
                                      gettime=(int)(self.ui.Sample_spinBox.value()))
                self._running = False
                break
            time.sleep(self.timeout / 1000)

    def run_time(self): # 每1s读取一次温度，直到达到合适温度glo_var.target_temp
        while self._running:
            self.time += 1
            time.sleep(self.timeout / 1000)

    def thread_looparri_fun(self, fun, timeout=1000): # 输入要调用循环函数返回结果的函数fun和循环时间
        try:
            with self.lock:
                self.timeout = timeout
                self._running = True
                self._thread = threading.Thread(
                    target=self.loopTime_arri,
                    args=(fun,),
                    daemon=True
                )
                self._thread.start()
                return 0, f"开始计时，每{timeout}ms触发一次\n"
        except Exception as e:
            return 1, f"计时失败：{e}\n"

    def loopTime_arri(self, fun): # 不断累加时间，不用管和上面是一起用的
        while self._running:
            # 线程安全：把值读出来再比较
            self.time += 1
            fun(self.time) # fun函数调用累加的时间
            time.sleep(self.timeout / 1000)
            if(self.stoptime != 0 and self.time == self.stoptime):
                self.ui.Clear_Button.setEnabled(True) # 允许继续
                break

    # —— 供外部调用的停止接口 ——
    def stop(self):
        with self.lock:  # 若存在并发访问，加锁
            self._running = False
            self._stop_evt.set()  # 立即唤醒正在 sleep 的线程
            self.time = 0
            glo_var.now_temp = 0
            glo_var.now_chan = 1
            glo_var.now_Sam = 0

class time_opea(): # 得到达温时间后，正式开启采样过程
    def __init__(self, ui, temptime, ser, ser1, gettime = 10):
        print("temptime:", temptime, "cleartime:", ui.Cleartime_spinBox.value(), "standtime:", ui.Standtime_spinBox.value())
        self.ui = ui
        self.start_flag = True
        self.temptime = temptime # 达到目标温度的时间
        self.cleartime = ui.Cleartime_spinBox.value() # 洗气时常
        self.standtime = ui.Standtime_spinBox.value() # 保持温度时常
        self.gettime = gettime # 采集时常
        self.alltime = temptime + self.standtime + (self.cleartime + gettime) * 2 # 一个样品整个过程时常
        self.waittime = self.alltime - temptime - self.standtime # 上个通道开启距下个通道开启时间差值
        print("waittime:", self.waittime, "alltime:", self.alltime)
        self.ser = ser
        self.ser1 = ser1
        if self.ser.ser is None:
            raise ValueError("底层串口句柄为 None，请检查串口是否打开成功")
        if self.ser1.ser is None:
            raise ValueError("底层串口句柄为 None，请检查串口是否打开成功")
        self.time_th = time_thread(ser, ser1, ui = ui, starttime = temptime) # 开始计时
        self.time_th.thread_loopfun(self.time_th.run_time) # 循环函数
        self.push_opea()


    def push_opea(self): # 一系列执行操作
        for i in range(1, glo_var.target_Sam + 1):  # target_Sam个样品循环操作
            print("开始操作:glo_var.now_Sam", glo_var.now_Sam)
            glo_var.now_Sam = i   # 更新当前样品的索引

            self.pos_down()  # 插入
            print("time:", self.time_th.time, "插入样品" + str(i))

            self.sample_collect()  # 采集
            print("time:", self.time_th.time, "样品" + str(i) + "开始采集")

            self.room_clear()
            print("time:", self.time_th.time, "气室正在清洗, 下一个为样品" + str(i + 1))

            self.pos_top_before()
            print("time:", self.time_th.time, "拔出样品" + str(i))

            self.pos_top()  # 转移位置到下一个样品
            print("time:", self.time_th.time, "转移位置到下一个样品" + str(i + 1))

            # 一旦循环结束，可以设置start_flag为True，表示可以开始下一次循环
        self.start_flag = True


    def is_clear_time(self, Opea_time):
        return (Opea_time == (self.standtime + self.temptime + self.gettime) or  # 气室清理
         Opea_time == (self.alltime - self.cleartime)) and glo_var.now_Sam < int(self.ui.Simnum_spinBox.value())

    def channal_heat(self): # 通道加热，只需要ser1操作
        target_temp = self.ui.Heattep_SpinBox.value()
        glo_var.now_chan += 1
        self.ser_opea(1, glo_var.channal[glo_var.now_chan], target_temp)
        self.time_th.time = 0 #重新开始计算时间
        self.ui._statues_label.setText("通道" + str(glo_var.now_chan) + "）开始加热")

    def sample_collect(self): # 信号采集
        if glo_var.Save_flag != "开始采集":
            glo_var.Save_flag = "开始采集"
        # 清空采集数据
        ms._ClearDraw.emit()
        while True:
            if glo_var.now_Sam == 1 or self.ser.getSignal == "32":  # 清洗完成
                text = ("21\n\r")
                self.ser_opea(3, self.gettime, text=text)
                ms._statues_label.emit("样品" + str(glo_var.now_Sam) + "开始采集")
                break


    def room_clear(self):
        if glo_var.Save_flag != "采集完成":
            glo_var.Save_flag = "采集完成"
        print("清空绘图面板")
        ms._ClearDraw.emit()
        while True:
            if self.ser.getSignal == "22":  # 采样完成
                ms._statues_label.emit("样品" + str(glo_var.now_Sam + 1) + "正在采样")
                text = ("31\n\r")
                ms._statues_label.emit("气室正在清洗" + "下一个为样品" + str(glo_var.now_Sam + 1))
                self.ser_opea(4, self.cleartime, text=text)
                break


    def pos_top(self):
        if(glo_var.now_Sam != glo_var.target_Sam):
            self.ser_opea("0A", glo_var.posxyz[glo_var.now_Sam + 1][0], glo_var.posxyz[glo_var.now_Sam + 1][1],
                                (int)(glo_var.posxyz[glo_var.now_Sam + 1][2] * 0.1))
        else:
            self.Stra()

    def pos_top_before(self):
        self.ser_opea("0A", glo_var.posxyz[glo_var.now_Sam][0], glo_var.posxyz[glo_var.now_Sam][1],
                                (int)(glo_var.posxyz[glo_var.now_Sam][2] * 0.1))

    def pos_down(self):
        self.ser_opea("0A", glo_var.posxyz[glo_var.now_Sam][0], glo_var.posxyz[glo_var.now_Sam][1],
                                (int)(glo_var.posxyz[glo_var.now_Sam][2]))

    def Stra(self): # 运动轴回到原点

        self.ser_opea('0C')

    def ser_opea(self, opea, opea1, opea2 = 0, opea3 = 0, text = None): # ser与ser1发送信号
        if text != None:
            while True:  # 没到回复
                self.ser.write(text)  # 开始采集信号
                time.sleep(1)
                if self.ser.sameSignal == True:
                    break
        while True:  # 没到回复
            self.ser1.serialSend(opea, opea1, opea2, opea3, flag = True)
            time.sleep(1)
            if self.ser1.sameSignal == True:
                break




class Serial1opea():
    def __init__(self, ui, ser):
        self.ser = ser
        self.ui = ui
        self.pos_flag = False

    def Get_temp(self): # 发送获取温度信号
        self.ser.serialSend(2, self.Getchannel_spinBox.value(), flag = True)

    def Heat_temp(self):# 发送加热信号
        self.ser.serialSend(1, self.Getchannel_spinBox.value(), int(self.Heattep_SpinBox_2.value()*10), flag = True)

    def GetSigal1(self, text): # 获取信号
        parts = text.split()  # ['55','AA', ...]
        Frame = frame_data.FrameData()
        parts = parts[2 : Frame.pkgLen - 1]
        Frame.setDataToArray(parts)
        if (Frame.buf[2] == '02'): # 获取温度
            num = int.from_bytes(bytes.fromhex(Frame.buf[4] + Frame.buf[5]), byteorder='big')  # 1000
            text = num / 10.0
            glo_var.now_temp = text # 更新现在的温度
        if (Frame.buf[2] == '0B'): # 读取当前坐标
            x = int.from_bytes(bytes.fromhex(Frame.buf[3] + Frame.buf[4]), byteorder='big')  # 1000
            y = int.from_bytes(bytes.fromhex(Frame.buf[5] + Frame.buf[6]), byteorder='big')  # 1000
            z = int.from_bytes(bytes.fromhex(Frame.buf[7] + Frame.buf[8]), byteorder='big')  # 1000
            if(x == glo_var.thepos[1][1] and y == glo_var.thepos[1][2] and z == glo_var.thepos[1][3]):
                self.pos_flag = True

    def GetSigal(self, text): # 获取信号
        print("收到的信号:",text)
        parts = text.split()  # ['55','AA', ...]


    def Setpos(self): # 设置位置信号
        self.ser1.serialSend('0A', self.Posx_spinBox.value(), self.Posy_spinBox.value(),
                             self.Posz_spinBox.value(), flag = True)

    def Getpos(self): # 发送获取坐标信号
        self.ser1.serialSend('0B')

    def Stra(self): # 运动轴回到原点
        self.ser1.serialSend('0C')

    def Startpos(self): # 是否初始化
        self.ser1.serialSend('0D')

