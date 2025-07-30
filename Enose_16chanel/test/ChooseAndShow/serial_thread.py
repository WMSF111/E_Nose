import serial
import serial.tools.list_ports
import threading
import frame_data as FrameDate


# 获取系统中所有可用的串口列表
def getPortList():
    Com_Dict = {}
    port_list = list(serial.tools.list_ports.comports())
    for port in port_list:
        Com_Dict["%s" % port[0]] = "%s" % port[1]
    return port_list, Com_Dict


# 自定义串口类
class myserial():
    def __init__(self, port="", bund=0):
        # 初始化串口类
        self.read_flag = False  # 读取标志，用于控制读取线程
        self.pause_flag = False  # 暂停标志，用于控制暂停和恢复
        self.busy = False
        self.port = port  # 串口名称
        self.bund = bund  # 波特率
        self.lock = threading.Lock()  # 创建一个锁
        self.ser = None  # 初始化串口对象
        self.d = FrameDate.FrameData()

    def setSer(self, port: str, bund: int):
        # 设置串口名称和波特率
        self.port = port
        self.bund = bund

    def open(self, fun, flag = 0, stock = 0, timeout=100):
        # 打开串口
        try:
            # 创建串口对象
            if stock == 0:
                self.ser = serial.Serial(self.port, self.bund, timeout=timeout)
            else:
                self.ser = serial.Serial(self.port, self.bund)
            if self.ser.is_open:
                print("创建串口成功")
                # 如果串口成功打开
                with self.lock:
                    self.read_flag = True  # 设置读取标志为 True
                    self.pause_flag = False  # 设置暂停标志为 False
                rt = threading.Thread(target=self.loopRead, args=(fun,flag))  # 创建读取线程
                # rt.setDaemon(True)  # 设置为守护线程，确保主线程结束时子线程也会结束
                # rt.setTerminationEnabled(True)
                rt.start()  # 启动读取线程

                return 0, "打开串口%s成功,波特率%d\n" % (self.port, self.bund)  # 返回成功信息
        except Exception as e:
            # 如果打开串口失败
            with self.lock:
                self.read_flag = False  # 设置读取标志为 False
            return 1, "打开串口%s失败\n%s\n" % (self.port, str(e))  # 返回失败信息

    def write(self, text):
        # 向串口写入数据
        if self.ser:
            result = self.ser.write(text.encode('utf-8'))  # 将字符串编码为字节并写入串口
            return result  # 返回写入的字节数
        else:
            return 0

    def loopRead(self, fun, flag):
        """
        自动识别数据类型：
          - 纯可打印 ASCII → utf-8 文本
          - 含非打印或 0x00 → 十六进制字符串
        fun(line: str) 回调收到的内容
        """
        buffer = bytearray()
        while True:
            with self.lock:
                if not self.read_flag:
                    break
                if self.pause_flag:
                    continue

            # try:
                if self.ser.in_waiting:
                    data = self.ser.read(self.ser.in_waiting)
                    slip_n = b'\r\n'
                    if flag == 1:
                        hex_data = ' '.join(f'{b:02X}' for b in data)
                        hex_data = hex_data + ' '
                        data = (hex_data).encode('ascii')  # b'55 AA 02 01 00 00 00 00 00 0A\r\n'
                        slip_n = b'0A '
                    buffer.extend(data)

                    # 按 \r\n 切帧
                    while slip_n in buffer:
                        frame, buffer = buffer.split(slip_n, 1)

                        # 1. 判断是否全是可打印 ASCII
                        if all(0x20 <= b <= 0x7E for b in frame):
                            # 文本
                            try:
                                text = frame.decode('utf-8', errors='replace')
                            except Exception:
                                text = frame.decode('latin-1', errors='replace')
                        else:
                            # 2. 十六进制
                            text = frame.hex(' ').upper()
                            # 其它字节 → 标准 HEX 字符串
                            # text = frame.hex().upper()  # ← 这里改成无空格的即可
                            print(text)
                        fun(text)

            # except Exception as e:
            #     print(f"读取串口数据时发生错误: {e}")
            #     with self.lock:
            #         self.read_flag = False
            #     break

    def pause(self):
        # 暂停串口通信
        with self.lock:
            self.pause_flag = True  # 设置暂停标志为 True
        print("暂停串口通信")

    def resume(self):
        # 恢复串口通信
        with self.lock:
            self.pause_flag = False  # 设置暂停标志为 False
        print("恢复串口通信")

    def stop(self):
        # 停止串口通信
        with self.lock:
            self.read_flag = False  # 设置读取标志为 False
        if self.ser:
            self.ser.close()  # 关闭串口
        print("关闭串口")

    def setALLDataToArray(self, arr):
        for i in range(0, self.pkgLen):
            self.buf[i] = arr[i]

    def serialSendData(self, dat): # 发送数据到串口，先将数据打包成字节串，然后写入串口。
        req = ' '.join(dat)
        req = bytes.fromhex(req.replace(' ', ''))
        if hasattr(self, 'ser'):
            try:
                self.ser.write(req)
            except serial.serialutil.SerialException:
                self.no_error = False

    def serialSend(self): # 发送 FrameData 对象中的数据到串口。
        # print()
        if not self.busy:
            if hasattr(self, 'ser'):
                try:
                    self.busy = True
                    text = self.d.packBytes()
                    self.ser.write(text)
                    self.busy = False
                    # print( self.ser.readline())#read会阻塞
                except serial.serialutil.SerialException:
                    self.no_error = False


class SerialsMng(): # 管理多线程
    # 接收一个列表 lst，列表中包含串口的配置信息
    # list=[name,bps,pixStyle,width,  name,bps,pixStyle,width,]
    # ["COM3",250000,0x13, 45,"COM4",250000,0x13, 45]
    def __init__(self, lst):

        self.ser_count = int(len(lst) / 2) # 计算串口设备的数量，每个设备占用 4 个配置项。
        self.ser_arr = [] # 初始化一个空列表，用于存储串口设备对象。
        for x in range(0, self.ser_count):
            # 遍历配置列表，为每个串口设备创建一个 SerialOP 对象，并将其添加到 self.ser_arr 列表中。
            idx = x * 2
            sop = myserial(lst[idx], lst[idx + 1])
            print(lst[idx], lst[idx + 1])
            self.ser_arr.append(sop)
        print(self.ser_arr) # 打印串口设备对象列表。

    def setdataAndsend(self, idx, data): # 设置指定串口设备的数据并发送。
        sop = self.ser_arr[idx]
        if not sop.busy:
            sop.d.setDataToArray(data)
            sop.serialSend()


    def splitData(self, data, sidx=0, eidx=0): # 根据起始索引和结束索引，从数据列表中截取子列表。
        b = eidx <= len(data) and sidx >= 0 and eidx - sidx > 0
        if (b):
            d = data[sidx:eidx]
            return b, d
        return False, []

    def sendFrameData(self, data, pixstyle=4, width=10): # 将数据分割并发送到每个串口设备。
        datlen = len(self.ser_arr)
        # 每个串口设备控制一行
        c = 0
        u = pixstyle * width
        # print(u)
        for x in range(datlen):  #

            # 获取切割的数据，发送到对应的节点
            b, d = self.splitData(data, c * u, (c + 1) * u)
            # print(c, c * u, (c + 1) * u,b,d)
            if b:
                # 串口发送1

                self.setdataAndsend(x, d)
            c += 1

    def sendFrameData_splited(self, data): #如果数据已经分割好，直接将每个子列表发送到对应的串口设备。
        dvclen = len(self.ser_arr)

        datlen = len(data)
        # 每个串口设备控制 data 一个子数组的数据
        if dvclen < datlen:
            datlen = dvclen
        # print(u)
        for x in range(datlen):  #
            self.setdataAndsend(x, data[x])
