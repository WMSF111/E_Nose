## 串口设置UI界面

import sys, os, re
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
grandparent_dir = os.path.dirname(parent_dir)
import global_var as g_var
from PySide6.QtCore import QObject, Signal
from PySide6.QtWidgets import QWidget, QFileDialog, QApplication
from PySide6.QtGui import QIcon, QTextCursor
import serial_thread as mythread
from Serial_ui import Ui_Serial
import Gragn_uishow


class MySignals(QObject):
    # 定义一种信号，两个参数 类型分别是： QTextBrowser 和 字符串
    # 调用 emit方法 发信号时，传入参数 必须是这里指定的 参数类型
    print = Signal(str)

    _serialComboBoxResetItems = Signal(list)
    _serialComboBoxClear = Signal()
    _setButtonText = Signal(str)
    _lineClear = Signal()


ms = MySignals()


class Action():
    def __init__(self, ui: QWidget) -> None:
        self.ui = ui

    def _serialComboBoxResetItems(self, texts: list):
        self.ui.serialComboBox.clear()
        self.ui.serialComboBox.addItems(texts)
        self.ui.serialComboBox2.clear()
        self.ui.serialComboBox2.addItems(texts)

    def _serialComboBoxclear(self):
        self.ui.serialComboBox.clear()
        self.ui.serialComboBox2.clear()

    def _setButtonText(self, text: str):
        self.ui.connectButton.setText(text)

    def _lineClear(self):
        self.ui.sendEdit.clear()

    def headerprint(self, receive_data):
        # data 示例：MQ3_1=123,MQ3_2=456,TGS2603_1=789,base=999,...
        pattern = r'([^=,]+)='  # 捕获等号前的名称
        names = re.findall(pattern, receive_data)
        # 去重且保序（Python 3.7+ dict 保序）
        g_var.sensors = list(dict.fromkeys(names))
        print(receive_data)
        self.ui.tb.insertPlainText(receive_data)

        # 获取到text光标,确保下次插入到内容最后
        textCursor = self.ui.tb.textCursor()
        # 滚动到底部
        textCursor.movePosition(QTextCursor.End)
        # 设置光标到text中去
        self.ui.tb.setTextCursor(textCursor)

        # 确保光标可见
        self.ui.tb.ensureCursorVisible()

    def print(self, receive_data):

        self.ui.tb.insertPlainText(receive_data)

        # 获取到text光标,确保下次插入到内容最后
        textCursor = self.ui.tb.textCursor()
        # 滚动到底部
        textCursor.movePosition(QTextCursor.End)
        # 设置光标到text中去
        self.ui.tb.setTextCursor(textCursor)

        # 确保光标可见
        self.ui.tb.ensureCursorVisible()

class Serial_Init(QWidget, Ui_Serial):
    def __init__(self, Gragh):

        super(Serial_Init, self).__init__()
        self.setupUi(self)
        self.Gragh = Gragh

        self.a = Action(self)
        self.initMS()
        self.ports = []
        self.Port_select = ""
        # self.set_initial_baud_rate(g_var.Bund_select)
        self.Com_Dict = {}
        sconfig = ["COM1", 115200, "COM3", 9600]  #
        self.smng = mythread.SerialsMng(sconfig)
        self.ser = self.smng.ser_arr[0]
        self.ser1 = self.smng.ser_arr[1]
        self.initSerial()

    def set_initial_baud_rate(self, baud_rate):
        """
        设置初始波特率。
        :param baud_rate: 初始波特率值
        """
        # 遍历 QComboBox 的所有选项
        for i in range(self.baudComboBox.count()):
            # 获取当前选项的文本（波特率值）
            current_rate = int(self.baudComboBox.itemText(i))
            # 如果当前选项的波特率值等于目标波特率，则设置为当前选中项
            if current_rate == baud_rate:
                self.baudComboBox.setCurrentIndex(i)
                break

    def initMS(self):
        ms._serialComboBoxResetItems.connect(self.a._serialComboBoxResetItems)
        ms._serialComboBoxClear.connect(self.a._serialComboBoxclear)
        ms._setButtonText.connect(self.a._setButtonText)
        ms.print.connect(self.a.print)
        ms._lineClear.connect(self.a._lineClear)
        self.CheckButton.clicked.connect(self.initSerial)  # 链接按钮选择
        self.connectButton.clicked.connect(self.openPort)  # 链接按钮选择
        self.sendButton.clicked.connect(self.send)  # sendButton联系
        # 串口信息显示
        self.serialComboBox.currentTextChanged.connect(
            lambda: self.initSerial
        )
        self.serialComboBox2.currentTextChanged.connect(
            lambda: self.initSerial()
        )
        self.saveButton.clicked.connect(self.savefile)  # 保存文件按钮
        self.clearButton.clicked.connect(self.tb.clear)  # 清除按钮

    def initSerial(self):
        ports, self.Com_Dict = mythread.getPortList()  # 获取串口列表
        self.port_imf(self.serialComboBox, self.statues)  # 显示串口信息
        self.port_imf(self.serialComboBox2, self.statues_3)  # 显示串口信息
        if self.ports != ports:  # 如果串口不是所选的
            self.ports = ports
            if g_var.Port_select not in [i.name for i in self.ports]:
                self.ser1.read_flag = False
                print([i.name for i in self.ports], g_var.Port_select)
                print("g_var.Port_select not in [i.name for i in self.ports]")
            ms._serialComboBoxResetItems.emit([i.name for i in self.ports])  # 添加所有串口


    def openPort(self):  # 打开串口
        print("read_flag:", str(self.ser1.read_flag))
        if self.ser1.read_flag:
            ms._setButtonText.emit("断开状态")
            # self.ser_open_look_ui(False)
        else:
            ms._setButtonText.emit("连接状态")
            # self.ser_open_look_ui(True)
        if self.ser1.read_flag:  # 如果串口存在
            self.ser.stop()  # 关闭串口
            self.ser1.stop()  # 关闭串口
            # ms._setButtonText.emit("连接")
        else:
            g_var.Port_select = self.serialComboBox.currentText()  # 串口选择
            self.ser.setSer(g_var.Port_select, g_var.Bund_select)  # 设置串口及波特率
            d = self.ser.open(ms.print.emit)
            print(d)
            g_var.Port_select2 = self.serialComboBox2.currentText()  # 串口选择
            self.ser1.setSer(g_var.Port_select2, g_var.Bund_select2)  # 设置串口及波特率
            d = self.ser1.open(ms.print.emit, flag=1)
            print(d)
            ms.print.emit(d[1])
            # ms._setButtonText.emit("断开")

    def send(self):
        text = self.sendEdit.text()
        print("text:", text)
        print(text[0:2])
        if not (text == "") or not (text is None):
            if self.ser1.read_flag:
                if text[0:2] == "55":
                    self.ser1.serialSendData(text)
                else:
                    self.ser1.write(text)
                ms._lineClear.emit()

    def showAbout(self):
        self.msg.show()

    # 串口信息
    def port_imf(self, serialComboBox, statues):
        # 显示选定的串口的详细信息
        imf_s = serialComboBox.currentText()
        if imf_s != "":
            statues.setText(self.Com_Dict[serialComboBox.currentText()])
            g_var.Com_select = serialComboBox.currentText()
        else:
            statues.setText("     无串口信息")

    def savefile(self):
        filename = QFileDialog.getSaveFileName(None, "open file", "/", "TEXT Files(*.txt)")
        # print(filename)
        if filename[0] == "" or filename is None:
            return
        try:
            with open(filename[0], "w") as f:
                text = self.tb.toPlainText()
                f.write(text)
            ms.print.emit("保存到" + filename[0])
        except Exception as e:
            ms.print.emit("保存失败" + str(e))

        # 锁定和解锁ui 无法点击串口信息及波特率

    def ser_open_look_ui(self, status):
        self.serialComboBox.setEnabled(status)
        self.baudComboBox.setEnabled(status)

    def closeEvent(self, event):
        """点击右上角 X 时调用"""
        # 1. 停止串口线程
        if hasattr(self, 'ser1') and self.ser1.read_flag:
            self.ser1.stop()
        if hasattr(self, 'ser') and self.ser.read_flag:
            self.ser.stop()
        event.accept()  # 允许窗口真正关闭
        self.Gragh.serial_setting()

        # window = Gragn_show_ui.GraphShowWindow()
        # window.show()
        # 2. 如果有额外线程，一并停止
        #   例：self.worker_thread.quit(); self.worker_thread.wait()
        # 3. 结束 Qt 事件循环
        # QCoreApplication.quit()





def runApp(ui):
    mainw = Serial_Init(ui)


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     app.setStyle("WindowsVista")  # 强制使用 WindowsVista 主题
#     window = Serial_Init()
#     window.show()
#     sys.exit(app.exec())