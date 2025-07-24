''' 用来显示主界面和其他界面的关系'''

import Enose.tool.UI_show.serial_show as se
from PySide6.QtWidgets import QMainWindow
from Enose.resource_ui.ui_pfile.MianWindow import Ui_MainWindow
from Enose.tool.UI_show.Gragn_show_ui import GraphShowWindow
from Enose.resource_ui.ui_pfile.Serial_setting import SerialSetting_Init
from Enose.tool.UI_show.Alg_ui_show import AlgShow_Init

class MianWindow_Init(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MianWindow_Init, self).__init__()
        # 使用ui文件导入定义界面类
        self.setupUi(self)
        self.InitMS()


    def InitMS(self):
        self.treeWidget.itemClicked.connect(self.on_tree_item_clicked)


    def on_tree_item_clicked(self, item, column):
        if item.text(column) == "准备阶段":
            self.clear_layout()
        # 检查点击的项目是否是“串口设置”
        if item.text(column) == "串口设置":
            # 创建并显示串口设置窗口
            self.serial_settings_window = se.Serial_Init()
            self.serial_settings_window.show()  # 显示窗口
        # 检查点击的项目是否是“传感器设置”
        if item.text(column) == "传感器设置":
            self.SerialSetting_show = SerialSetting_Init()
            self.SerialSetting_show.show()  # 显示窗口
        # 检查点击的项目是否是“测试阶段”
        if item.text(column) == "测试阶段":
            self.clear_layout()
            # 创建并显示串口设置窗口
            self.test_show = GraphShowWindow()
            self.show_Layout.addWidget(self.test_show)
        if item.text(column) == "算法选择":
            self.clear_layout()
            # 创建并显示串口设置窗口
            self.test_show = AlgShow_Init()
            self.show_Layout.addWidget(self.test_show)

    def clear_layout(self):
        # 清除布局中的所有内容
        while self.show_Layout.count():
            item = self.show_Layout.takeAt(0)
            if item.widget():  # 如果是控件
                item.widget().deleteLater()  # 删除控件
            elif item.layout():  # 如果是子布局
                self.clear_layout_recursive(item.layout())  # 递归清除子布局
                item.layout().deleteLater()  # 删除子布局

    def clear_layout_recursive(self, layout):
        # 递归清除布局中的所有内容
        while layout.count():
            item = layout.takeAt(0)
            if item.widget():  # 如果是控件
                item.widget().deleteLater()  # 删除控件
            elif item.layout():  # 如果是子布局
                self.clear_layout_recursive(item.layout())  # 递归清除子布局
                item.layout().deleteLater()  # 删除子布局

    def closeEvent(self, event):
        self.test_show.closeEvent(event)
        event.accept()  # 允许窗口真正关闭