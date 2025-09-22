import tool.frame_data as frame_data
import threading
import time, copy
import global_var as glo_var

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
            self.ser1.d.setDataTodo(2, glo_var.channal[1])
            self.ser1.serialSend()
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
        self.nul_num = 2
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

        # self.push_opea(t) 是一个函数调用表达式，会立即执行并返回结果，而 thread_looparri_fun需要的是一个可调用对象（函数对象）
        # self.time_th.thread_looparri_fun(lambda t: self.push_opea(t)) # 适用于需要参数的函数，提供了更大的灵活性。

    def push_opea(self, the_time): # 一系列执行操作
        # print("time: ",time)
        Opea_time = self.time_adjust(the_time) # 进行时间调整
        if the_time % self.waittime == 0 and glo_var.now_chan < round(self.ui.Simnum_spinBox.value() / 2) : # 达到下一个通道加热的时间
            self.channal_heat()
            print("Opea_time:", Opea_time, "time:", the_time, "通道" + str(glo_var.now_chan) + "(实" + str(glo_var.channal[glo_var.now_chan]) + ")开始加热")

        if ((Opea_time == (self.standtime + self.temptime) or # 达到保持时长开始1、2次采集
                Opea_time == (self.standtime + self.temptime + self.gettime + self.cleartime)) and glo_var.now_Sam < int(self.ui.Simnum_spinBox.value())):
            print("Opea_time:", Opea_time, "time:", the_time, "插入样品" + str(glo_var.now_Sam + 1))
            self.pos_down()  # 插入
            print("Opea_time:", Opea_time, "time:", the_time, "样品" + str(glo_var.now_Sam + 1) + "开始采集")
            self.sample_collect() # 采样


        if (self.is_clear_time(Opea_time)): #第一次采集结束
            print("Opea_time:", Opea_time, "time:", the_time, "气室正在清洗" + "下一个为样品" + str(glo_var.now_Sam + 1))
            self.room_clear()
        if (self.is_clear_time(Opea_time - self.nul_num)): #第一次采集结束
            print("Opea_time:", Opea_time, "time:", the_time, "拔出样品" + str(glo_var.now_Sam))
            self.pos_top_before()
        if (self.is_clear_time(Opea_time - self.nul_num*2)): #第一次采集结束
            print("Opea_time:", Opea_time, "time:", the_time, "转移位置到下一个样品" + str(glo_var.now_Sam + 1))
            self.pos_top()



        if ((self.ui.Simnum_spinBox.value() == 1 and (the_time == self.gettime + self.temptime + self.standtime)) or
        (the_time == (self.waittime) * round(self.ui.Simnum_spinBox.value() / 2) + self.temptime + self.standtime - self.cleartime)):
            self.ui.statues_label.setText("已完成采样")
            print("Opea_time:", Opea_time, "time:", the_time, "已完成采样")
            self.time_th._running = False
            self.ui.Collectbegin_Button.setEnabled(True)
            self.pos_top_before()
            time.sleep(2)
            self.ser1.d.setDataTodo('0C')
            self.ser1.serialSend(True)



    def time_adjust(self, time): # 保证每次操作可循环
        if time >= self.alltime:
            return (time - (self.temptime + self.standtime)) % self.waittime + self.temptime + self.standtime
        else:
            return time

    def is_clear_time(self, Opea_time):
        return (Opea_time == (self.standtime + self.temptime + self.gettime) or  # 气室清理
         Opea_time == (self.alltime - self.cleartime)) and glo_var.now_Sam < int(self.ui.Simnum_spinBox.value())

    def channal_heat(self): # 通道加热，只需要ser1操作
        glo_var.now_chan += 1
        self.ser1.d.setDataTodo(1, glo_var.channal[glo_var.now_chan], int(glo_var.target_temp))  # 开始下一个通道xx加热信号
        self.ser1.serialSend(True)
        self.ui.statues_label.setText("通道" + str(glo_var.now_chan) + "实（" + str(glo_var.channal[glo_var.now_chan]) + "）开始加热")

    def sample_collect(self): # 信号采集
        if glo_var.Save_flag != "开始采集":
            glo_var.Save_flag = "开始采集"
        # 清空采集数据
        print("清空绘图面板")
        self.ui.data = [[] for _ in range(self.ui.data_len)]
        self.ui.alldata = copy.deepcopy(self.ui.data)
        glo_var.now_Sam += 1
        text = ("#Sample1$\r\n")
        self.ser_opea(text, 3, self.gettime)  # 信号发出采集信号
        self.ui.statues_label.setText("样品" + str(glo_var.now_Sam) + "开始采集")

    def room_clear(self):
        if glo_var.Save_flag != "采集完成":
            glo_var.Save_flag = "采集完成"
        print("清空绘图面板")
        self.ui.data = [[] for _ in range(self.ui.data_len)]
        self.ui.alldata = copy.deepcopy(self.ui.data)
        text = ("#Clear1$\r\n")
        self.ui.statues_label.setText("气室正在清洗" + "下一个为样品" + str(glo_var.now_Sam + 1))
        self.ser.write(text)  # 开始采集信号
        self.ser1.d.setDataTodo(4, self.cleartime)  # 清洗30s
        self.ser1.serialSend(True)

    def pos_top(self):
        self.ser1.d.setDataTodo("0A", glo_var.posxyz[glo_var.now_Sam + 1][0], glo_var.posxyz[glo_var.now_Sam + 1][1],
                                (int)(glo_var.posxyz[glo_var.now_Sam + 1][2] * 0.1))  # 清洗30s
        self.ser1.serialSend(True)

    def pos_top_before(self):
        self.ser1.d.setDataTodo("0A", glo_var.posxyz[glo_var.now_Sam][0], glo_var.posxyz[glo_var.now_Sam][1],
                                (int)(glo_var.posxyz[glo_var.now_Sam][2] * 0.1))  # 清洗30s
        self.ser1.serialSend(True)

    def pos_down(self):
        self.ser1.d.setDataTodo("0A", glo_var.posxyz[glo_var.now_Sam + 1][0], glo_var.posxyz[glo_var.now_Sam + 1][1],
                                (int)(glo_var.posxyz[glo_var.now_Sam + 1][2]))  # 清洗30s
        self.ser1.serialSend(True)

    def ser_opea(self, text, opea, opea1, opea2 = 0, opea3 = 0): # ser与ser1发送信号
        self.ser.write(text)  # 开始采集信号
        self.ser1.d.setDataTodo(opea, opea1, opea2, opea3)  # 清洗30s
        self.ser1.serialSend(True)


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
        if (Frame.buf[2] == '02'): # 获取温度
            num = int.from_bytes(bytes.fromhex(Frame.buf[4] + Frame.buf[5]), byteorder='big')  # 1000
            lst_int = [int(x, 16) for x in text.split()]
            text = num / 10.0
            glo_var.now_temp = text
            if self.ui.Currtem_spinBox.value() == 1:
                self.ui.Currtem_spinBox.setValue(text)
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
        # print("转化后：", text)

    def GetSigal(self, text): # 获取信号
        print("收到的信号:",text)
        parts = text.split()  # ['55','AA', ...]


    def Setpos(self): # 设置位置信号
        self.ser1.d.setDataTodo('0A', self.Posx_spinBox.value(), self.Posy_spinBox.value(),self.Posz_spinBox.value())
        self.ser1.serialSend()

    def Getpos(self): # 发送获取坐标信号
        self.ser1.d.setDataTodo('0B')
        self.ser1.serialSend()

    def Stra(self): # 运动轴回到原点
        self.ser1.d.setDataTodo('0C')
        self.ser1.serialSend()

    def Startpos(self): # 是否初始化
        self.ser1.d.setDataTodo('0D')
        self.ser1.serialSend()
