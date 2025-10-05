import tool.frame_data as frame_data
import threading
import time, copy
import global_var as glo_var


class time_thread(): # 时间相关的线程
    # 初始化输入两个串口， 停止时间与初始时间
    def __init__(self,ser, ser1,  ui = None, stoptime = 0, starttime = 0):
        self.time = starttime
        self.ms = ui
        self.stoptime = stoptime
        self.lock = threading.Lock()  # 创建一个锁
        self._stop_evt = threading.Event()  # 用来打断 sleep
        self._running = True
        self.opea = None # 串口操作
        self.ser = ser
        self.ser1 = ser1
        self.timeout = 1000; # 循环时间

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
        while True:
            if self._running:
                # 线程安全：把值读出来再比较
                print("现在温度是：", glo_var.now_temp)
                self.ms._Currtem_spinBox.emit(glo_var.now_temp)
                self.ser1.serialSend(2, glo_var.channal[1])
                self.time += 1
                if glo_var.target_temp <= glo_var.now_temp:  # 当目标温度达成
                    print("达到目标温度需要时间：",self.time)
                    self.ms._attendtime_spinBox.emit(self.time)
                    # self.opea = Serial1opea(self.ms, self.ser, self.ser1)
                    # self.opea.push_opea()
                    self._running = False
                    break
                time.sleep(self.timeout / 1000)
            if self._stop_evt.is_set():
                print("Thread stopped by event.")
                break

    def run_time(self): # 每1s读取一次温度，直到达到合适温度glo_var.target_temp
        while self._running:
            self.time += 1
            time.sleep(self.timeout / 1000)

    def thread_draw(self, fun, timeout=1000): # 输入要调用循环函数返回结果的函数fun和循环时间
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
        while True:
            if self._running:
                # 线程安全：把值读出来再比较
                self.time += 1
                fun(self.time) # fun函数调用累加的时间
                time.sleep(self.timeout / 1000)
                if(self.stoptime != 0 and self.time == self.stoptime):
                    self.ms._Clear_Button.emit(True) # 允许继续
                    self._running =  False
            if self._stop_evt.is_set():
                print("Thread stopped by event.")
                break

    # —— 供外部调用的停止接口 ——
    def pause(self, name = None):
        with self.lock:  # 若存在并发访问，加锁
            self._running = False
        if name != None:
            print(name + "线程暂停")
        else:
            print("时间线程暂停")

    def resume(self, name = None):
        with self.lock:
            self._running = True  # 设置暂停标志为 False
        if name != None:
            print(name + "恢复时间线程")
        else:
            print("恢复时间线程")

    def stop(self, name = None):
        glo_var.now_temp = 0
        self._running = False  # 设置读取标志为 False
        self.time = 0
        self._stop_evt.set()  # 通过事件通知线程停止
        if name != None:
            print(name + "线程已结束")
        else:
            print("线程已结束")

channal = [0, 4,3,2,1,5,6,7,8]
posxyz = [
    [0,0,0],
    [944, 3184, 1548],
    [1536, 3184, 1548],
    [960, 18943, 1548],
    [1728, 19455, 1548],
]
class Serial1opea():
    def __init__(self, ms, ser, ser1):
        self.ser = ser
        self.ser1 = ser1
        self.ms = ms
        # self.time_th = None
        self.temptime = 0  # 达到目标温度的时间
        self.cleartime = glo_var.cleartime
        self.standtime = glo_var.standtime
        self.gettime = glo_var.gettime  # 采集时常
        self.target_Sam = glo_var.target_Sam
        self.now_Sam = 0
        self.now_chan = 1

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

    def push_opea(self): # 一系列执行操作
        self.now_Sam = 1
        while self.now_Sam <= self.target_Sam:  # target_Sam个样品循环操作
            print("开始操作:self.now_Sam", self.now_Sam)
            time.sleep(4)

            self.pos_down()  # 插入
            print( "插入样品" + str(self.now_Sam))
            time.sleep(4)

            self.sample_collect()  # 采集
            print( "样品" + str(self.now_Sam) + "开始采集")

            self.room_clear()
            print("气室正在清洗, 下一个为样品" + str(self.now_Sam + 1))
            self.ms._ClearDraw.emit()

            self.pos_top_before()
            print("拔出样品" + str(self.now_Sam))
            time.sleep(2)

            self.pos_top()  # 转移位置到下一个样品
            print( "转移位置到下一个样品" + str(self.now_Sam + 1))
            self.now_Sam += 1

    def channal_heat(self): # 通道加热，只需要ser1操作
        self.now_chan += 1
        self.ser_opea(1, channal[self.now_chan], glo_var.target_temp)
        # self.time_th.time = 0 #重新开始计算时间
        self.ms._statues_label.emit("通道" + str(self.now_chan) + "）开始加热")

    def sample_collect(self): # 信号采集
        self.ms._draw_open.emit()
        # 清空采集数据
        # self.ms._ClearDraw.emit()
        while True:
            if self.now_Sam == 1 or self.ser.getSignal == "32" or self.ser.pause_flag == True:  # 清洗完成
                text = ("21\n\r")
                self.ser_opea(3, self.gettime, text=text,
                              re = "55 AA 03 00 01 00 00 00 00 0A")
                self.ms._statues_label.emit("样品" + str(self.now_Sam) + "开始采集")
                break


    def room_clear(self):
        while True:
            if self.ser.getSignal == "22" or self.ser.pause_flag == True:  # 采样完成
                self.ms._draw_close.emit()
                self.ms._auto_save.emit()
                text = ("31\n\r")
                self.ms._statues_label.emit("气室正在清洗" + "下一个为样品" + str(self.now_Sam + 1))
                self.ser_opea(4, self.cleartime, text=text)
                break


    def pos_top(self):
        if(self.now_Sam != self.target_Sam):
            self.ser_opea("0A", posxyz[self.now_Sam + 1][0], posxyz[self.now_Sam + 1][1],
                                (int)(posxyz[self.now_Sam + 1][2] * 0.1), target = 10)
        else:
            self.Stra()
            # self.time_th.stop()
            self.ms._Collectbegin_Button.emit(True)
            # self.ui.pause_serial() # 关闭所有线程

    def pos_top_before(self):
        print(self.now_Sam)
        self.ser_opea("0A", posxyz[self.now_Sam][0], posxyz[self.now_Sam][1],
                                (int)(posxyz[self.now_Sam][2] * 0.1), target = 10)

    def pos_down(self):
        self.ser_opea("0A", posxyz[self.now_Sam][0], posxyz[self.now_Sam][1],
                                (int)(posxyz[self.now_Sam][2]), target = 20)

    def Stra(self): # 运动轴回到原点
        self.ser_opea('0C')

    def ser_opea(self, opea, opea1 = 0, opea2 = 0, opea3 = 0, text = None, re = None, target = 5): # ser与ser1发送信号
        num = 0
        if text != None:
            while True:  # 没到回复
                self.ser.write(text)  # 开始采集信号
                time.sleep(2)
                num += 1
                if self.ser.sameSignal == True:
                    break
                if num == 5:
                    self.ms._statues_label.emit("信号串口掉线")
                    break
        num = 0
        while True:  # 没到回复
            self.ser1.serialSend(opea, opea1, opea2, opea3, flag = True,
                                 re = re)
            time.sleep(2)
            if self.ser1.sameSignal == True:
                break
            num += 1
            if num == target:
                self.ms._statues_label.emit("控制串口掉线,退出程序")
                self.Stra()
                self.ms._pause_serial.emit()
                break

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


