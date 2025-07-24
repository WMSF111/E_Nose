import frame_data
import threading
import time
import global_var as glo_var

class time_thread():
    def __init__(self, ser, ser1, stoptime = 0, starttime = 0):
        self.time = starttime
        self.stoptime = stoptime
        self.lock = threading.Lock()  # 创建一个锁
        self._running = True
        self.opea = None
        self.ser = ser
        self.ser1 = ser1

    def open_time(self, fun, timeout=1000): # 输入要循环的函数
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

    def loopTime(self, ui):
        while self._running:
            # 线程安全：把值读出来再比较
            target = ui.Heattep_SpinBox.value()
            print("现在温度是：", glo_var.now_temp)
            self.time += 1
            if target <= glo_var.now_temp:
                glo_var.target_temp = target
                print("达到目标温度需要时间：",self.time)
                self.StopTime_wait(ui, self.time)
                # self.StopTime_wait(ui, 30)
                self._running = False
                break
            time.sleep(1)

    def start_time(self, fun, timeout=1000): # 累加时间并执行
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
            self.time += 1
            fun(self.time)
            time.sleep(1)

    def StopTime_wait(self, ui, time):
        print("时间到达：", time)
        self.opea = time_opea(ui, time, ui.Cleartime_spinBox.value(), ui.Standtime_spinBox.value(), self.ser, self.ser1)
        return time

class time_opea():
    def __init__(self, ui, temptime, cleartime, standtime, ser, ser1, gettime = 10):
        print("temptime:", temptime, "cleartime:", cleartime, "standtime:", standtime)
        self.ui = ui
        self.temptime = temptime
        self.cleartime = cleartime
        self.standtime = standtime
        self.gettime = gettime
        self.alltime = temptime + standtime + (cleartime + gettime) * 2
        self.waittime = self.alltime - temptime - standtime
        print("waittime:", self.waittime, "alltime:", self.alltime)
        self.ser = ser
        self.ser1 = ser1
        if self.ser.ser is None:
            raise ValueError("底层串口句柄为 None，请检查串口是否打开成功")
        if self.ser1.ser is None:
            raise ValueError("底层串口句柄为 None，请检查串口是否打开成功")
        self.time_th = time_thread(ser, ser1, starttime = temptime) # 开始计时
        # self.time_th.start_time(self.push_opea)
        self.time_th.start_time(lambda t: self.push_opea(t))

    def push_opea(self, time):
        if time >= self.alltime:
            Opea_time = (time - (self.temptime + self.standtime)) % self.waittime + self.temptime + self.standtime
        else:
            Opea_time = time
        if time % self.waittime  == 0 and glo_var.now_chan < round(self.ui.Simnum_spinBox.value() / 2) : # 达到下一个通道加热的时间
            glo_var.now_chan += 1
            self.ser1.d.setDataTodo(1, glo_var.now_chan, int(glo_var.target_temp))# 开始下一个通道xx加热信号
            self.ser1.serialSend()
            self.ui.statues_label.setText("通道" + str(glo_var.now_chan) + "开始加热")
            print("Opea_time:", Opea_time, "time:", time, "通道" + str(glo_var.now_chan) + "开始加热")
        if ((Opea_time == (self.standtime + self.temptime) or # 达到保持时长开始1、2次采集
                Opea_time == (self.standtime + self.temptime + self.gettime + self.cleartime)) and glo_var.now_Sam < int(self.ui.Simnum_spinBox.value())):
            glo_var.now_Sam += 1
            text = "sample_time:" + str(self.gettime)
            self.ser_opea(text, 3, self.gettime) # 采集
            self.ui.statues_label.setText("样品" + str(glo_var.now_Sam) + "开始采集")
            print("Opea_time:", Opea_time, "time:", time, "样品" + str(glo_var.now_Sam) + "开始采集")
        if ((Opea_time == (self.standtime + self.temptime + self.cleartime) or
                Opea_time == (self.alltime - self.cleartime)) and glo_var.now_Sam < int(self.ui.Simnum_spinBox.value())): #第一次采集结束
            text = "exhaust_time:" + str(self.cleartime) # 清洗30s
            self.ser_opea(text, 4, self.cleartime) # 清洗30s
            self.ser_opea("", "0A", glo_var.now_Sam + 1)  # 切换到下一个样品位置
            self.ui.statues_label.setText("气室正在清洗" + "下一个为样品" + str(glo_var.now_Sam + 1))
            print("Opea_time:", Opea_time, "time:", time, "气室正在清洗" + "下一个为样品" + str(glo_var.now_Sam + 1))
        if time == (self.waittime) * round(self.ui.Simnum_spinBox.value() / 2) + self.temptime + self.standtime - self.cleartime:
            self.ui.statues_label.setText("已完成采样")
            print("Opea_time:", Opea_time, "time:", time, "已完成采样")
            self.time_th._running = False


    def ser_opea(self, text, opea, opea1, opea2 = 0, opea3 = 0):
        self.ser.write(text)  # 开始采集信号
        self.ser1.d.setDataTodo(opea, opea1, opea2, opea3)  # 清洗30s
        self.ser1.serialSend()





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

