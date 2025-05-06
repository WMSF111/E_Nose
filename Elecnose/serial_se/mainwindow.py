from PySide2.QtCore import QObject, Signal, QTimer
from PySide2.QtWidgets import QApplication, QWidget, QFileDialog
from functools import partial
from PySide2.QtGui import QIcon, QTextCursor
from .core import getPortList, myserial
import time

class MySignals(QObject):
    # 定义一种信号，两个参数 类型分别是： QTextBrowser 和 字符串
    # 调用 emit方法 发信号时，传入参数 必须是这里指定的 参数类型
    print = Signal(str)

    _serialComboBoxResetItems = Signal(list)
    _serialComboBoxClear = Signal()
    _setButtonText = Signal(str)
    _lineClear = Signal()
    print = Signal(str)

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

    def print(self, t:str):
        tc = self.ui.tb.textCursor()
        tc.movePosition(QTextCursor.End)
        if self.ui.showTimeCheckBox.isChecked():
            nowtime = time.strftime("%H:%M:%S", time.localtime())
            tc.insertText("[" + nowtime + "]")
        tc.insertText(t)

        
        if self.ui.autoWrapCheckBox.isChecked():
            # self.ui.tb.ensureCursorVisible()
            self.ui.tb.setTextCursor(tc)
        

class MainWindow(QWidget):
    def __init__(self, ui):
        # 从文件中加载UI定义
        # 从 UI 定义中动态 创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了
        # 比如 self.ui.button , self.ui.textEdit
        super().__init__()
        # 使用ui文件导入定义界面类
        self.ui = ui
        
        self.a = Action(self.ui)
        self.initMS()
        self.ports = []
        self.selectPort = ""
        self.selectBund = ""
        self.ser = myserial()
        self.timer2 = QTimer()
        self.timer2.timeout.connect(self.initSerial)
        self.timer2.start(1000)


    def initMS(self):
        self.ui.connectButton.clicked.connect(self.openPort)
        ms._serialComboBoxResetItems.connect(self.a._serialComboBoxResetItems)
        ms._serialComboBoxClear.connect(self.a._serialComboBoxclear)
        ms._setButtonText.connect(self.a._setButtonText)
        ms.print.connect(self.a.print)
        ms._lineClear.connect(self.a._lineClear)
        self.ui.sendButton.clicked.connect(self.send)
        self.ui.saveButton.clicked.connect(self.savefile)
        self.ui.clearButton.clicked.connect(self.ui.tb.clear)
        

    def initSerial(self):
        ports = getPortList()
        if self.ports != ports:
            self.ports = ports
            if self.ser.port not in [i.name for i in self.ports]:
                self.ser.read_flag = False
            ms._serialComboBoxResetItems.emit([i.name for i in self.ports])

        if self.ser.read_flag:
            ms._setButtonText.emit("断开")
            self.ser_open_look_ui(False)
        else:
            ms._setButtonText.emit("连接")
            self.ser_open_look_ui(True)

    def openPort(self):
        if self.ser.read_flag:
            self.ser.stop()
        else:
            port = self.ui.serialComboBox.currentText()
            bund = int(self.ui.baudComboBox.currentText())
            if port == "":
                ms.print.emit("当前未选择串口\n")
                return
            self.ser.setSer(port, bund)
            d = self.ser.open(ms.print.emit)
            ms.print.emit(d[1])

    def send(self):
        text = self.ui.sendEdit.text()
        if not (text == "") or not (text is None):
            if self.ser.read_flag:
                self.ser.write(text)
                ms._lineClear.emit()

    def showAbout(self):
        self.ui.msg.show()


    def savefile(self):
        filename = QFileDialog.getSaveFileName(self.ui, "open file", "./", "TEXT Files(*.txt)")
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

def runApp():
    mainw = MainWindow()