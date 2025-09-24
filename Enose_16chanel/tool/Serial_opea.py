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


class time_thread(): # 时间相关的线程
    # 初始化输入两个串口， 停止时间与初始时间
    def __init__(self,ser, ser1,  ui = None, stoptime = 0, starttime = 0):
        self.time = starttime
        self.ui = ui
        self.stoptime = stoptime
        self.lock = threading.Lock()  # 创建一个锁
        self._stop_evt = threading.Event()  # 用来打断 sleep
        self._running = True
        self.opea = None # 串口操作
        self.ser = ser
        self.ser1 = ser1
        self.timeout = 1000; # 循环时间

    def thread_loopfun(self, fun, timeout=1000): # 输入要循环的函数和循环时间
        self.time = 0
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
            target = glo_var.target_temp
            print("现在温度是：", glo_var.now_temp)
            self.ser1.serialSend(2, glo_var.channal[1])
            self.time += 1
            if target <= glo_var.now_temp:  # 当目标温度达成
                glo_var.target_temp = target # 赋值目标温度到全局
                print("达到目标温度需要时间：",self.time)
                self.ui.attendtime_spinBox.setValue(self.time)
                self.opea = time_opea(self.ui, self.time, self.ser,self.ser1,
                                      gettime=(int)(self.ui.Sample_spinBox.value()))
                self._running = False
                break
            time.sleep(self.timeout / 1000)

    def thread_looparri_fun(self, fun, timeout=1000): # 输入要调用循环函数返回结果的函数fun和循环时间
        # self.time = 0
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
            self.temptime = 0
            glo_var.now_temp = 0
            glo_var.target_temp = 0
            glo_var.now_chan = 1
            glo_var.now_Sam = 0
            glo_var.target_Sam = 1

class time_opea(): # 得到达温时间后，正式开启采样过程
    def __init__(self, ui, temptime, ser, ser1, gettime = 10):
        print("temptime:", temptime, "cleartime:", ui.Cleartime_spinBox.value(), "standtime:", ui.Standtime_spinBox.value())
        self.ui = ui
        self.a = Action(self.ui)
        self.initMS()
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
        self.time_th = time_thread(ser, ser1, starttime = temptime) # 开始计时
        self.time_th.thread_looparri_fun(self.push_opea) # 适用于不需要参数的函数

    def initMS(self):
        ms._Currtem_spinBox.connect(self.a._Currtem_spinBox)
        ms._statues_label.connect(self.a._statues_label)
        ms._ClearDraw.connect(self.a._ClearDraw)

    def push_opea(self, the_time): # 一系列执行操作


        if (self.ui.Simnum_spinBox.value() == glo_var.now_Sam):
            ms.statues_label.emit("已完成采样")
            print( "time:", the_time, "已完成采样")
            self.time_th._running = False
            self.ui.Collectbegin_Button.setEnabled(True)
            self.pos_top_before()
            time.sleep(2)
            self.ser1.serialSend('0C', flag = True)


    def is_clear_time(self, Opea_time):
        return (Opea_time == (self.standtime + self.temptime + self.gettime) or  # 气室清理
         Opea_time == (self.alltime - self.cleartime)) and glo_var.now_Sam < int(self.ui.Simnum_spinBox.value())

    def channal_heat(self): # 通道加热，只需要ser1操作
        glo_var.now_chan += 1
        self.ser1.serialSend(1, glo_var.channal[glo_var.now_chan], int(glo_var.target_temp), flag = True)  # 开始下一个通道xx加热信号
        ms.statues_label.emit("通道" + str(glo_var.now_chan) + "实（" + str(glo_var.channal[glo_var.now_chan]) + "）开始加热")

    def sample_collect(self): # 信号采集
        if glo_var.Save_flag != "开始采集":
            glo_var.Save_flag = "开始采集"
        # 清空采集数据
        ms._ClearDraw.emit()
        glo_var.now_Sam += 1
        text = ("#Sample1$\r\n")
        self.ser_opea(text, 3, self.gettime)  # 信号发出采集信号
        ms.statues_label.emit("样品" + str(glo_var.now_Sam) + "开始采集")

    def room_clear(self):
        if glo_var.Save_flag != "采集完成":
            glo_var.Save_flag = "采集完成"
        print("清空绘图面板")
        ms._ClearDraw.emit()
        text = ("#Clear1$\r\n")
        ms.statues_label.emit("气室正在清洗" + "下一个为样品" + str(glo_var.now_Sam + 1))
        self.ser.write(text)  # 开始采集信号
        self.ser1.serialSend(4, self.cleartime, flag = True)

    def pos_top(self):
        self.ser1.serialSend("0A", glo_var.posxyz[glo_var.now_Sam + 1][0], glo_var.posxyz[glo_var.now_Sam + 1][1],
                                (int)(glo_var.posxyz[glo_var.now_Sam + 1][2] * 0.1), flag = True)

    def pos_top_before(self):
        self.ser1.serialSend("0A", glo_var.posxyz[glo_var.now_Sam][0], glo_var.posxyz[glo_var.now_Sam][1],
                                (int)(glo_var.posxyz[glo_var.now_Sam][2] * 0.1),flag = True)

    def pos_down(self):
        self.ser1.serialSend("0A", glo_var.posxyz[glo_var.now_Sam + 1][0], glo_var.posxyz[glo_var.now_Sam + 1][1],
                                (int)(glo_var.posxyz[glo_var.now_Sam + 1][2]), flag = True)

    def ser_opea(self, text, opea, opea1, opea2 = 0, opea3 = 0): # ser与ser1发送信号
        self.ser.write(text)  # 开始采集信号
        self.ser1.serialSend(opea, opea1, opea2, opea3, flag = True)


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
        self.ser.getSignal = Frame.buf
        print("收到的信号:", self.GetSigal)
        if (Frame.buf[2] == '02'): # 获取温度
            num = int.from_bytes(bytes.fromhex(Frame.buf[4] + Frame.buf[5]), byteorder='big')  # 1000
            text = num / 10.0
            glo_var.now_temp = text # 更新现在的温度
            ms._Currtem_spinBox.emit(text)
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

