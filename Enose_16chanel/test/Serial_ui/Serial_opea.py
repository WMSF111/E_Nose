import frame_data
import threading
import time
import global_var as glo_var

class time_thread(): # 时间相关的线程
    # 初始化输入两个串口， 停止时间与初始时间
    def __init__(self, ser, stoptime = 0, starttime = 0):
        self.time = starttime
        self.stoptime = stoptime
        self.lock = threading.Lock()  # 创建一个锁
        self._stop_evt = threading.Event()  # 用来打断 sleep
        self._running = True
        self.opea = None # 串口操作
        self.ser = ser
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

    def thread_looparri_fun(self, fun, timeout=1000): # 输入要调用循环函数返回结果的函数fun和循环时间
        self.time = 0
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
            fun(self.time) # fun函数调用累加的时间
            self.time += 1
            time.sleep(self.timeout / 1000)
            if self._running == False:
                break

    def stop(self):
        with self.lock:  # 若存在并发访问，加锁
            self._running = False
            self._stop_evt.set()  # 立即唤醒正在 sleep 的线程
            self.time = 0
            glo_var.now_Sam = 0
            glo_var.target_Sam = 1

class time_opea(): # 得到达温时间后，正式开启采样过程
    def __init__(self, ui, ser, thread, gettime = 10):
        print("cleartime:", ui.Cleartime_spinBox.value(), "gettime:", gettime,"samplenum:", ui.Simnum_spinBox.value())
        self.ui = ui
        self.thread = thread
        self.samplenum = ui.Simnum_spinBox.value()
        self.cleartime = ui.Cleartime_spinBox.value() # 洗气时常
        self.gettime = gettime # 采集时常
        self.alltime = (self.cleartime + gettime) * self.samplenum - self.cleartime # 一个样品整个过程时常
        self.waittime = self.cleartime + gettime # 一个样品采集和清洗时间
        print("waittime:", self.waittime, "alltime:", self.alltime)
        self.ser = ser
        if self.ser.ser is None:
            raise ValueError("底层串口句柄为 None，请检查串口是否打开成功")


    def push_opea(self, time): # 一系列执行操作
        Opea_time = self.time_adjust(time) # 进行时间调整
        print("push_opea:", Opea_time)
        if (Opea_time == 0 and glo_var.now_Sam < int(self.samplenum)):
            self.sample_collect()
            print("Opea_time:", Opea_time, "time:", time, "样品" + str(glo_var.now_Sam) + "开始采集")
        if (Opea_time == self.cleartime and glo_var.now_Sam < int(self.samplenum)): #第一次采集结束
            self.room_clear()
            print("Opea_time:", Opea_time, "time:", time, "气室正在清洗" + "下一个为样品" + str(glo_var.now_Sam + 1))
        if time == self.alltime:
            self.ui.statues_label.setText("已完成采样")
            print("Opea_time:", Opea_time, "time:", time, "已完成采样")
            self.thread._running = False
            self.ser.pause()


    def time_adjust(self, time): # 保证每次操作可循环
        return (time) % self.waittime

    def sample_collect(self): # 信号采集
        if glo_var.Save_flag != "开始采集":
            glo_var.Save_flag = "开始采集"
        glo_var.now_Sam += 1
        text = "sample_time:" + str(self.gettime) # ser需要发出的信息
        self.ser_opea(text, 3, self.gettime)  # 信号发出采集信号
        self.ui.statues_label.setText("样品" + str(glo_var.now_Sam) + "开始采集")

    def room_clear(self):
        if glo_var.Save_flag != "采集完成":
            glo_var.Save_flag = "采集完成"
        text = "exhaust_time:" + str(self.cleartime)  # 清洗30s
        self.ser_opea(text, 4, self.cleartime)  # 清洗30s
        self.ser_opea("", "0A", glo_var.posxyz[glo_var.now_Sam + 1][0], glo_var.posxyz[glo_var.now_Sam + 1][1], glo_var.posxyz[glo_var.now_Sam + 1][2])  # 切换到下一个样品位置
        self.ui.statues_label.setText("气室正在清洗" + "下一个为样品" + str(glo_var.now_Sam + 1))

    def ser_opea(self, text, opea, opea1, opea2 = 0, opea3 = 0): # ser发送信号
        self.ser.write(text)  # 开始采集信号
class Serial1opea():
    def __init__(self, ui, ser):
        self.ser = ser
        self.ui = ui

    def Get_temp(self): # 发送获取温度信号
        self.ser.d.setDataTodo(2, self.Getchannel_spinBox.value())
        self.ser.serialSend()

    def Heat_temp(self):# 发送加热信号
        self.ser.d.setDataTodo(1, self.Getchannel_spinBox.value(), int(self.Heattep_SpinBox_2.value()*10))
        self.ser.serialSend()

    def GetSigal1(self, text): # 获取信号
        print("收到的信号:",text)
        parts = text.split()  # ['55','AA', ...]
        Frame = frame_data.FrameData()
        parts = parts[2 : Frame.pkgLen - 1]
        Frame.setDataToArray(parts)
        print(Frame.buf)
        print(Frame.buf[2])
        if (Frame.buf[2] == '02'): # 获取温度
            num = int.from_bytes(bytes.fromhex(Frame.buf[4] + Frame.buf[5]), byteorder='big')  # 1000
            lst_int = [int(x, 16) for x in text.split()]
            text = num / 10.0
            glo_var.now_temp = text
            # if lst_int[3] == self.ui.Getchannel_spinBox.value():
            #     self.ui.Gettep_spinBox.setValue(text)
            text = "获取温度为：" + str(text)
        if (Frame.buf[2] == '0B'): # 读取当前坐标
            x = int.from_bytes(bytes.fromhex(Frame.buf[3] + Frame.buf[4]), byteorder='big')
            y = int.from_bytes(bytes.fromhex(Frame.buf[5] + Frame.buf[6]), byteorder='big')
            z = int.from_bytes(bytes.fromhex(Frame.buf[7] + Frame.buf[8]), byteorder='big')
            text = '('+ str(x) + ','+ str(y) + ',' + str(z) + ')'
            self.ui.Getpos_lineEdit.setText(text)
            text = "获取坐标为" + text
        if (Frame.buf[2] == '0D'): # 读取当前坐标
            x = Frame.buf[4]
            y = Frame.buf[6]
            z = Frame.buf[8]
            text = '('+ x + ','+ y + ',' + z + ')'
            if x == y == z == '01':
                self.ui.Startpos_Button.setText("已初始化")
            elif x == y == z == '00':
                self.ui.Startpos_Button.setText("未初始化")
            text = "获取初始化数据为：" + text
        print("转化后：", text)

    def GetSigal(self, text): # 获取信号
        print("收到的信号:",text)
        parts = text.split()  # ['55','AA', ...]


