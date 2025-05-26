import serial
import serial.tools.list_ports
import threading


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
        self.port = port  # 串口名称
        self.bund = bund  # 波特率
        self.lock = threading.Lock()  # 创建一个锁
        self.ser = None  # 初始化串口对象

    def setSer(self, port: str, bund: int):
        # 设置串口名称和波特率
        self.port = port
        self.bund = bund

    def open(self, fun, timeout=100):
        # 打开串口
        try:
            # 创建串口对象
            self.ser = serial.Serial(self.port, self.bund, timeout=timeout)
            if self.ser.is_open:
                print("创建串口成功")
                # 如果串口成功打开
                with self.lock:
                    self.read_flag = True  # 设置读取标志为 True
                    self.pause_flag = False  # 设置暂停标志为 False
                rt = threading.Thread(target=self.loopRead, args=(fun,))  # 创建读取线程
                rt.setDaemon(True)  # 设置为守护线程，确保主线程结束时子线程也会结束
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

    def loopRead(self, fun):
        # 循环读取串口数据
        buffer = bytearray()  # 创建一个字节缓冲区
        while True:
            with self.lock:
                if not self.read_flag:
                    break  # 如果读取标志为 False，退出循环
                if self.pause_flag:
                    continue  # 如果暂停标志为 True，跳过本次循环
            try:
                if self.ser.in_waiting:  # 检查串口是否有待读取的数据
                    data = self.ser.read(self.ser.in_waiting)  # 读取所有待读取的数据
                    buffer.extend(data)  # 将读取到的数据添加到缓冲区
                    # 检查缓冲区中是否包含自定义的换行符
                    if b'\r\n' in buffer:  # 假设自定义换行符为 '\r\n'
                        line, buffer = buffer.split(b'\r\n', 1)  # 分割出一行数据
                        fun(line.decode("utf-8"))  # 解码并调用回调函数
            except Exception as e:
                print(f"读取串口数据时发生错误: {e}")
                with self.lock:
                    self.read_flag = False  # 如果读取失败，设置读取标志为 False
                break  # 退出循环

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