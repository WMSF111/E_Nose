import sys

import global_var
import resource_ui.web_app
from resource_ui.modules import *
from resource_ui.widgets import *
import resource_ui.themes as theme
from resource_ui.web_app import run
from PySide6.QtWidgets import QApplication
import os
import threading
import tool.UI_show.serial_show as se
from PySide6.QtWidgets import QMainWindow, QMessageBox
from tool.UI_show.Gragn_show_ui import GraphShowWindow
from tool.UI_show.Alg_ui_show import AlgShow_Init

os.environ["QT_FONT_DPI"] = "150" # FIX Problem for High DPI and Scale above 100%
widgets = None

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # SET AS GLOBAL WIDGETS
        # ///////////////////////////////////////////////////////////////
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui


        # USE CUSTOM TITLE BAR | USE AS "False" FOR MAC OR LINUX
        # ///////////////////////////////////////////////////////////////
        Settings.ENABLE_CUSTOM_TITLE_BAR = True

        # APP NAME
        # ///////////////////////////////////////////////////////////////
        title = "实验平台"
        description = "智能电子鼻实验及算法平台"
        # APPLY TEXTS
        self.setWindowTitle(title)
        widgets.titleLeftApp.setText(title)
        widgets.titleRightInfo.setText(description)

        # TOGGLE MENU
        # ///////////////////////////////////////////////////////////////
        widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))

        # SET UI DEFINITIONS
        # ///////////////////////////////////////////////////////////////
        UIFunctions.uiDefinitions(self)

        # # QTableWidget PARAMETERS
        # # ///////////////////////////////////////////////////////////////
        # widgets.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # BUTTONS CLICK
        # ///////////////////////////////////////////////////////////////

        # 左侧菜单栏按钮初始化
        widgets.btn_serial.clicked.connect(self.buttonClick)
        widgets.btn_test.clicked.connect(self.buttonClick)
        widgets.btn_alg.clicked.connect(self.buttonClick)
        widgets.btn_ai.clicked.connect(self.buttonClick)


        # SHOW APP
        # ///////////////////////////////////////////////////////////////
        self.show()

        # 设置主题颜色
        # ///////////////////////////////////////////////////////////////
        useCustomTheme = True
        themeFile = global_var.themeFile


        # 设置主题
        if useCustomTheme:
            # 下载并应用主题
            UIFunctions.theme(self, themeFile, True)
            AppFunctions.setThemeHack(self)

        # 设置按钮界面
        # 初始化串口界面
        self.serial_init = se.Serial_Init()  # 创建Serial_Init实例
        widgets.stackedWidget.addWidget(self.serial_init)  # 将串口界面添加到 stackedWidget
        # 创建并测试窗口
        self.test_show = GraphShowWindow()
        widgets.stackedWidget.addWidget(self.test_show)  # 将串口界面添加到 stackedWidget
        # 创建并显示算法设置窗口
        self.alg_show = AlgShow_Init()
        widgets.stackedWidget.addWidget(self.alg_show)  # 将串口界面添加到 stackedWidget

        widgets.btn_serial.setStyleSheet(UIFunctions.selectMenu(widgets.btn_serial.styleSheet()))


    # BUTTONS CLICK
    # Post here your functions for clicked buttons
    # ///////////////////////////////////////////////////////////////
    def buttonClick(self):

        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        # SHOW HOME PAGE
        if btnName == "btn_serial":
            widgets.stackedWidget.setCurrentWidget(self.serial_init)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))


        # SHOW WIDGETS PAGE
        if btnName == "btn_test":
            if self.serial_init:
                if self.serial_init.ser:
                    self.serial_init.ser.stop()
            # 创建并测试窗口
            self.test_show = GraphShowWindow()
            widgets.stackedWidget.addWidget(self.test_show)  # 将串口界面添加到 stackedWidget
            widgets.stackedWidget.setCurrentWidget(self.test_show)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW NEW PAGE
        if btnName == "btn_alg":
            widgets.stackedWidget.setCurrentWidget(self.alg_show) # SET PAGE
            UIFunctions.resetStyle(self, btnName) # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet())) # SELECT MENU

        if btnName == "btn_ai":
            try:
                # 创建一个线程来启动 Flask 应用
                self.flask_thread = threading.Thread(target=run)
                self.flask_thread.start()
                resource_ui.web_app.open_browser()
            except:
                self.show_error_message()

        # PRINT BTN NAME
        print(f'Button "{btnName}" pressed!')

    def show_error_message(self):
        # 创建一个QMessageBox实例
        msg = QMessageBox()

        # 设置消息框的类型为错误
        msg.setIcon(QMessageBox.Critical)

        # 设置消息框的标题和内容
        msg.setWindowTitle("错误")
        msg.setText("无法打开链接:")

        # 设置消息框的按钮
        msg.setStandardButtons(QMessageBox.Ok)

        # 显示消息框
        msg.exec()

    # RESIZE EVENTS
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()

        # PRINT MOUSE EVENTS
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')

    def closeEvent(self, event):
        print("关闭事件")
        self.serial_init.closeEvent(event)
        self.test_show.closeEvent(event)
        self.alg_show.closeEvent(event)
        # resource_ui.web_app.shutdown()
        import os,signal

        pid = os.getpid()  # 获取当前进程的PID
        os.kill(pid, signal.SIGTERM)  # 主动结束指定ID的程序运行



if __name__ == "__main__":
    app = QApplication(sys.argv)
    icon = os.path.join(os.path.dirname(__file__), "icon.ico")
    app.setWindowIcon(QIcon(icon))
    window = MainWindow()
    sys.exit(app.exec())


