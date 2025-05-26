import sys,os
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
grandparent_dir = os.path.dirname(parent_dir)
# sys.path.append(parent_dir)
import Enose.global_var as g_var
from PySide6.QtCore import QObject, Signal
from PySide6.QtWidgets import QWidget, QFileDialog
from PySide6.QtGui import QIcon, QTextCursor
import Enose.tool.serial_thread as mythread
from Enose.resource_ui.ui_pfile.Serial import Ui_Serial

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

    def _serialComboBoxclear(self):
        self.ui.serialComboBox.clear()

    def _setButtonText(self, text: str):
        self.ui.connectButton.setText(text)

    def _lineClear(self):
        self.ui.sendEdit.clear()

    def print(self, receive_data):
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

class Serial_Init(QWidget):
    def __init__(self):

        super(Serial_Init, self).__init__()
        self.ui = Ui_Serial()
        self.ui.setupUi(self)
        
        self.a = Action(self.ui)
        self.initMS()
        self.ports = []
        g_var.Port_select = ""
        g_var.Bund_select = 115200
        self.set_initial_baud_rate(g_var.Bund_select)
        self.Com_Dict = {}
        self.ser = mythread.myserial()
        self.initSerial()
        # self.timer2 = QTimer()
        # self.timer2.timeout.connect(self.initSerial)
        # self.timer2.start(100)

    def set_initial_baud_rate(self, baud_rate):
        """
        设置初始波特率。
        :param baud_rate: 初始波特率值
        """
        # 遍历 QComboBox 的所有选项
        for i in range(self.ui.baudComboBox.count()):
            # 获取当前选项的文本（波特率值）
            current_rate = int(self.ui.baudComboBox.itemText(i))
            # 如果当前选项的波特率值等于目标波特率，则设置为当前选中项
            if current_rate == baud_rate:
                self.ui.baudComboBox.setCurrentIndex(i)
                break

    def initMS(self):
        ms._serialComboBoxResetItems.connect(self.a._serialComboBoxResetItems)
        ms._serialComboBoxClear.connect(self.a._serialComboBoxclear)
        ms._setButtonText.connect(self.a._setButtonText)
        ms.print.connect(self.a.print)
        ms._lineClear.connect(self.a._lineClear)
        self.ui.CheckButton.clicked.connect(self.initSerial)  # 链接按钮选择
        self.ui.connectButton.clicked.connect(self.openPort) # 链接按钮选择
        self.ui.sendButton.clicked.connect(self.send) # sendButton联系
        # 串口信息显示
        self.ui.serialComboBox.currentTextChanged.connect(self.initSerial) # 串口选择窗口联系显示串口信息
        self.ui.saveButton.clicked.connect(self.savefile) # 保存文件按钮
        self.ui.clearButton.clicked.connect(self.ui.tb.clear) # 清除按钮
        

    def initSerial(self):
        self.port_imf() # 显示串口信息
        ports, self.Com_Dict = mythread.getPortList() # 获取串口列表
        if self.ports != ports: # 如果串口不是所选的
            self.ports = ports
            if self.ser.port not in [i.name for i in self.ports]:
                self.ser.read_flag = False
            ms._serialComboBoxResetItems.emit([i.name for i in self.ports]) # 添加所有串口
        print("read_flag:", str(self.ser.read_flag))
        if self.ser.read_flag:
            ms._setButtonText.emit("断开")
            self.ser_open_look_ui(False)
        else:
            ms._setButtonText.emit("连接")
            self.ser_open_look_ui(True)

    def openPort(self): # 打开串口
        if self.ser.read_flag: # 如果串口存在
            self.ser.stop() # 关闭串口
        else:
            g_var.Port_select = self.ui.serialComboBox.currentText() # 串口选择
            g_var.Bund_select = int(self.ui.baudComboBox.currentText()) # 波特率选择
            self.ser.setSer(g_var.Port_select, g_var.Bund_select) # 设置串口及波特率
            d = self.ser.open(ms.print.emit) # 打开串口，成功返回0，失败返回1， + str信息
            ms.print.emit(d[1])

    def send(self):
        text = self.ui.sendEdit.text()
        if not (text == "") or not (text is None):
            if self.ser.read_flag:
                self.ser.write(text)
                ms._lineClear.emit()

    def showAbout(self):
        self.ui.msg.show()

    #串口信息
    def port_imf(self):
        # 显示选定的串口的详细信息
        imf_s = self.ui.serialComboBox.currentText()
        if imf_s != "":
            self.ui.statues.setText(self.Com_Dict[self.ui.serialComboBox.currentText()])
            g_var.Com_select = self.ui.serialComboBox.currentText()
        else:
            self.ui.statues.setText("     无串口信息")


    def savefile(self):
        filename = QFileDialog.getSaveFileName(None, "open file", "/", "TEXT Files(*.txt)")
        # print(filename)
        if filename[0] == "" or filename is None:
            return
        try:
            with open(filename[0], "w") as f:
                text = self.ui.tb.toPlainText()
                f.write(text)
            ms.print.emit("保存到"+filename[0])
        except Exception as e:
            ms.print.emit("保存失败" + str(e))

        # 锁定和解锁ui 无法点击串口信息及波特率
    def ser_open_look_ui(self, status):
        self.ui.serialComboBox.setEnabled(status)
        self.ui.baudComboBox.setEnabled(status)

def runApp(ui):
    mainw = Serial_Init(ui)