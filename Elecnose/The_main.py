import sys, TextEdit
from PySide2.QtGui import QIcon
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QApplication
from qfluentwidgets import MSFluentWindow, FluentIcon
from qframelesswindow import  StandardTitleBar
import resource_ui.tab as tab
import resource_ui.setting as setting
from PySide2 import QtCore
import serial_se.mainwindow as serial
from serial_se import runApp

import logging


class LoginWindow(MSFluentWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("数据看板")
        self.setWindowIcon(QIcon('./logo.png'))

        #添加子界面
        self.tab1 = tab.The_tab1(self)
        self.tab2 = tab.The_tab2(self)
        self.tab4 = tab.The_tab4(self)
        self.tab5 = tab.The_tab5(self)
        self.setTitleBar(StandardTitleBar(self))

        self.addSubInterface(self.tab1, FluentIcon.RINGER, "数据源")
        self.addSubInterface(self.tab2, FluentIcon.EDIT, "绘图")
        self.addSubInterface(self.tab4, FluentIcon.VIDEO, "串口")
        self.addSubInterface(self.tab5, FluentIcon.EDIT, "大模型")


if __name__ == '__main__':
    # enable dpi scale
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logFile = './log.txt'
    # 清除文件内容
    with open(logFile, 'w') as file:
        pass  # 这里 pass 表示什么都不做，即清除文件内容
    fh = logging.FileHandler(logFile, mode='a', encoding='utf-8')
    # 4，设置保存至文件的日志等级
    fh.setLevel(logging.INFO)
    format = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
    # 6，设置 写入日志文件的Handler 的日志格式
    fh.setFormatter(format)

    # 第四步，将Handler添加至日志记录器logger里
    logger.addHandler(fh)
    # 同样的，创建一个Handler用于控制台输出日志
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    ch.setFormatter(format)
    logger.addHandler(ch)

    # 同样的，创建一个Handler用于控制台输出日志
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    ch.setFormatter(format)

    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('logo.png'))
    w = LoginWindow()
    w.tab1.verticalLayout.addWidget(setting.SettingInterface1(w))  # 1.添加插件 2.导入文件
    # 开启高分屏支持
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    # 创建串口窗口
    window = serial.MainWindow(w.tab4)
    input_waiter = TextEdit.InputWaiter(w, logger)  # 绘图
    w.show()
    app.exec_()

