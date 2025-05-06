import sys, os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
grandparent_dir = os.path.dirname(parent_dir)
# sys.path.append(parent_dir)
import Enose.global_var as g_var
from PySide6.QtCore import QObject, Signal
from PySide6.QtWidgets import QWidget, QFileDialog
from PySide6.QtGui import QIcon, QTextCursor
import serial
import serial.tools.list_ports
import threading
from Enose.resource_ui.ui_pfile.Serial import Ui_Serial


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
        self.port = port  # 串口名称
        self.bund = bund  # 波特率

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
                self.read_flag = True  # 设置读取标志为 True
                rt = threading.Thread(target=self.loopRead, args=(fun,))  # 创建读取线程
                rt.setDaemon(True)  # 设置为守护线程，确保主线程结束时子线程也会结束
                rt.start()  # 启动读取线程

                return 0, "打开串口%s成功,波特率%d\n" % (self.port, self.bund)  # 返回成功信息
        except Exception as e:
            # 如果打开串口失败
            self.read_flag = False  # 设置读取标志为 False
            return 1, "打开串口%s失败\n%s\n" % (self.port, str(e))  # 返回失败信息

    def write(self, text):
        # 向串口写入数据
        result = self.ser.write(text.encode('utf-8'))  # 将字符串编码为字节并写入串口
        return result  # 返回写入的字节数


    def loopRead(self, fun):
        # 循环读取串口数据
        while self.read_flag:
            try:
                if self.ser.in_waiting:  # 检查串口是否有待读取的数据
                    txt = self.ser.read(self.ser.in_waiting).decode("utf-8")  # 读取数据并解码为字符串
                    fun(txt)  # 调用回调函数处理接收到的数据
            except:
                self.read_flag = True  # 如果读取失败，设置读取标志为 False

    def stop(self):
        # 停止串口通信
        self.read_flag = False  # 设置读取标志为 False
        self.ser.close()  # 关闭串口
        print("关闭串口")
#
#
# class MySignals(QObject):
#     # 定义一种信号，两个参数 类型分别是： QTextBrowser 和 字符串
#     # 调用 emit方法 发信号时，传入参数 必须是这里指定的 参数类型
#     print = Signal(str)
#
#     _serialComboBoxResetItems = Signal(list)
#     _serialComboBoxClear = Signal()
#     _setButtonText = Signal(str)
#     _lineClear = Signal()
#     print = Signal(str)
#
#
# ms = MySignals()
#
#
# class Action():
#     def __init__(self, ui: QWidget) -> None:
#         self.ui = ui
#
#     def _serialComboBoxResetItems(self, texts: list):
#         self.ui.serialComboBox.clear()
#         self.ui.serialComboBox.addItems(texts)
#
#     def _serialComboBoxclear(self):
#         self.ui.serialComboBox.clear()
#
#     def _setButtonText(self, text: str):
#         self.ui.connectButton.setText(text)
#
#     def _lineClear(self):
#         self.ui.sendEdit.clear()
#
#     def print(self, receive_data):
#         self.ui.tb.insertPlainText(receive_data)
#
#         # 获取到text光标,确保下次插入到内容最后
#         textCursor = self.ui.tb.textCursor()
#         # 滚动到底部
#         textCursor.movePosition(QTextCursor.End)
#         # 设置光标到text中去
#         self.ui.tb.setTextCursor(textCursor)
#
#         # 确保光标可见
#         self.ui.tb.ensureCursorVisible()

