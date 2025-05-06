import sys, re
import numpy as np
from PySide6.QtCore import (
    Qt,
)
from PySide6.QtWidgets import QApplication, QWidget, QHeaderView
from PySide6.QtGui import QColor, QStandardItemModel, QStandardItem, QBrush
import pyqtgraph as pg
from Enose.resource_ui.ui_pfile.Gragh_show import Ui_Gragh_show
from Enose.tool.serial_thread import myserial, getPortList  # 导入自定义的串口类和获取串口列表的函数
import Enose.global_var as g_var
from itertools import cycle

# 主窗口类
class GraphShowWindow(QWidget, Ui_Gragh_show):
    def __init__(self):
        super(GraphShowWindow, self).__init__()
        self.setupUi(self)  # 设置 UI 界面
        self.setWindowTitle("串口数据实时显示")
        self.data_len = len(g_var.sensors)

        # 初始化串口
        self.serial = myserial()  # 使用自定义的myserial类
        self.port_list, self.port_dict = getPortList()  # 获取串口列表

        # 初始化绘图
        self.plot_widget = pg.PlotWidget()
        self.Linegragh_Layout.addWidget(self.plot_widget)
        self.plot_widget.showGrid(x=True, y=True)
        self.plot_widget.setLabel('left', 'Value')
        self.plot_widget.setLabel('bottom', 'Sample')
        self.curves = []
        self.data = [[] for _ in range(self.data_len)]

        self.colors = [QColor(*np.random.choice(range(256), size=3)) for _ in range(self.data_len)]
        self.color_cycle = cycle(self.colors)
        self._data_colors = dict()  # 绘图颜色

        # 初始化传感器数据表
        self.model = QStandardItemModel(len(g_var.sensors), 2)
        self.model.setHorizontalHeaderLabels(['Sensor', 'Value'])
        self.Senser_stableView.setModel(self.model)
        self.Senser_stableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # 连接信号
        self.Dataclear_Button.clicked.connect(self.clear_data)
        self.Collectbegin_Button.clicked.connect(self.start_serial)
        self.Pause_Button.clicked.connect(self.pause_serial)
        self.Cancel_Button.clicked.connect(self.stop_serial)

    def start_serial(self):
        if not self.serial.read_flag:
            port = g_var.Port_select
            baudrate = g_var.Bund_select
            self.serial.setSer(port, baudrate)
            self.serial.open(self.process_data)

    def pause_serial(self):
        if self.serial.read_flag:
            self.serial.read_flag = False

    def stop_serial(self):
        if self.serial.read_flag:
            self.serial.stop()

    def clear_data(self):
        for data_list in self.data:
            data_list.clear()
        self.update_plot()
        self.update_table()

    def process_data(self, data):
        # 解析数据
        values = re.findall(r'\d+', data)
        if len(values) == self.data_len:
            values = [float(v) for v in values]
            for i, value in enumerate(values):
                self.data[i].append(value)
                if len(self.data[i]) > 300:  # 限制数据长度
                    self.data[i].pop(0)
            self.update_plot()
            self.update_table()

    def update_plot(self):
        if not self.curves:
            for i in range(self.data_len):
                curve = self.plot_widget.plot(pen=pg.mkPen(self.colors[i], width=2))
                self.curves.append(curve)
        for i, curve in enumerate(self.curves):
            curve.setData(self.data[i])

    def update_table(self):
        for i in range(self.data_len):
            sensor_name = g_var.sensors[i]
            value = self.data[i][-1] if self.data[i] else 0
            # color = self.colors[i].name()

            item_name = QStandardItem(sensor_name) # 创建一个item_name对象，用于表示传感器名称
            item_name.citem.setForeground(QBrush(QColor(self.get_currency_color(sensor_name))))  # 设置货币名称的前景色（文本颜色）
            item_name.setColumnCount(2)  # 设置该传感器名称项的列数为 2（货币名称和对应的值）
            item_name.setCheckable(True)  # 设置该传感器货币名称项为可复选
            item_name.setEditable(False) # 设置传感器名称不可编辑
            # 如果该货币名称在默认显示货币列表中，则设置其复选框为选中状态
            if sensor_name in g_var.sensors:
                item_name.setCheckState(Qt.CheckState.Checked)

            item_value = QStandardItem(f"{value:.2f}") # 创建一个item_value对象，用于表示传感器数据
            item_value.setEditable(False)

            self.model.setItem(i, 0, item_name)
            self.model.setItem(i, 1, item_value)

    def get_currency_color(self, sensor):
        if sensor not in self._data_colors:
            self._data_colors[sensor] = next(self.color_cycle)

        return self._data_colors[sensor]

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GraphShowWindow()
    window.show()
    sys.exit(app.exec())