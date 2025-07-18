import  sys, re, random
from PySide6.QtCore import (
    Qt, QCoreApplication
)
import serial_thread as mythread
from PySide6.QtWidgets import  QWidget, QHeaderView, QFileDialog, QApplication
from PySide6.QtGui import QColor, QStandardItemModel, QStandardItem, QBrush
import pyqtgraph as pg
from ChooseAndShow import Ui_Gragh_show
import global_var as g_var
from itertools import cycle
import logging
import frame_data
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# 主窗口类
class GraphShowWindow(QWidget, Ui_Gragh_show):
    def __init__(self):
        super(GraphShowWindow, self).__init__()
        self.setupUi(self)  # 设置 UI 界面
        self.setWindowTitle("串口数据实时显示")
        self.data_len = len(g_var.sensors)

        # 初始化串口
        # self.serial = myserial()  # 使用自定义的myserial类
        sconfig = [g_var.Port_select2, g_var.Bund_select2]  #
        self.smng = mythread.SerialsMng(sconfig)
        self.ser1 = self.smng.ser_arr[0]
        self.ser1.setSer(g_var.Port_select2, g_var.Bund_select2)  # 设置串口及波特率
        d = self.ser1.open(self.Showtemp, flag = 1)
        print(d)
        # 初始化绘图
        self.plot_widget = pg.PlotWidget()
        self.Linegragh_Layout.addWidget(self.plot_widget)
        self.plot_widget.showGrid(x=True, y=True)
        self.plot_widget.setBackground('w')  # 设置绘图背景为白色
        self.plot_widget.setLabel('left', 'Value')
        self.plot_widget.setLabel('bottom', 'Time(单位:s)')


        self.pie_canvas = None  # 用于持有matplotlib画布引用


        # self.plot_widget_2 = pg.PlotWidget()
        # self.Piegragh_Layout.addWidget(self.plot_widget_2)
        # self.plot_widget_2.setBackground('w')  # 设置绘图背景为白色

        self.curves = []
        self.data = [[] for _ in range(self.data_len)]
        self.time = 60
        self._data_lines = dict()  # 已存在的绘图线
        self._data_items = dict()  # 数据查看器的数据
        self._data_colors = dict()  # 绘图颜色
        self._data_visible = g_var.sensors.copy() # 选择要看的传感器


        self.colors = self.generate_random_color_list(self.data_len)
        self.color_cycle = cycle(self.colors)

        # 初始化传感器数据表
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(['Sensor', 'Value'])
        self.model.itemChanged.connect(self.check_check_state)  # 连接项目更改信号
        self.Senser_stableView.setModel(self.model)
        self.Senser_stableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)


        # 连接信号
        self.Dataclear_Button.clicked.connect(self.clear_data)
        self.Collectbegin_Button.clicked.connect(self.start_serial) # start_serial
        self.Gettep_Button.clicked.connect(self.Get_temp)  # start_serial
        self.Heat_Button.clicked.connect(self.Heat_temp)  # start_serial
        self.Setpos_Button.clicked.connect(self.Setpos)  # start_serial
        self.Getpos_Button.clicked.connect(self.Getpos)  # start_serial
        self.Stra_Button.clicked.connect(self.Stra)  # start_serial
        self.Startpos_Button.clicked.connect(self.Startpos)  # start_serial

    def _serialComboBoxResetItems(self, texts: list):
        self.ui.serialComboBox.clear()
        self.ui.serialComboBox.addItems(texts)
        self.ui.serialComboBox2.clear()
        self.ui.serialComboBox2.addItems(texts)

    def _serialComboBoxclear(self):
        self.ui.serialComboBox.clear()
        self.ui.serialComboBox2.clear()

    def open_serial(self, port, baudrate):
        if not self.ser1.read_flag: # 如果串口存在
            d = self.ser1.open(self.Showtemp, flag = 1)
            # d = self.ser1.open(self.process_data)  # 打开串口，成功返回0，失败返回1， + str信息
            print(d)

    def clear_data(self):
        self.time = self.Cleartime_spinBox.value()
        self.ser1.d.setDataTodo(4,self.time)
        print("clear_data:", self.ser1)
        self.ser1.serialSend()
        self.data = [[] for _ in range(self.data_len)]
        # print(self.time)
        if(self.time != 0):
            # 设置 x 轴的固定范围
            self.plot_widget.setXRange(0, self.time, padding=0)  # 设置 x 轴的范围为 0 到 300
        # self.open_serial(g_var.Port_select, g_var.Bund_select)

    def start_serial(self):
        print("start_serial")
        self.time = self.Inputtime_spinBox.value()
        self.volum = self.Volum_spinBox.value()
        self.ser1.d.setDataTodo(3, self.volum, self.time)
        self.ser1.serialSend()
        self.data = [[] for _ in range(self.data_len)]
        # print(self.time)
        if (self.time != 0):
            # 设置 x 轴的固定范围
            self.plot_widget.setXRange(0, self.time, padding=0)  # 设置 x 轴的范围为 0 到 300
        # self.open_serial(g_var.Port_select, g_var.Bund_select)

    def Get_temp(self):
        self.ser1.d.setDataTodo(2, self.Getchannel_spinBox.value())
        self.ser1.serialSend()

    def Heat_temp(self):
        self.ser1.d.setDataTodo(1, self.Getchannel_spinBox.value(), int(self.Heattep_SpinBox_2.value()*10))
        self.ser1.serialSend()

    def Showtemp(self, text):
        print("收到的信号:",text)
        parts = text.split()  # ['55','AA', ...]
        Frame = frame_data.FrameData()
        parts = parts[2 : Frame.pkgLen - 1]
        Frame.setDataToArray(parts)
        print(Frame.buf)
        print(Frame.buf[2])
        if (Frame.buf[2] == '02'): # 获取温度
            num = int.from_bytes(bytes.fromhex(Frame.buf[4] + Frame.buf[5]), byteorder='big')  # 1000
            lst_int = [int(x, 16) for x in text.split()]
            text = num / 10.0
            if lst_int[3] == self.Getchannel_spinBox.value():
                self.Gettep_spinBox.setValue(text)
            text = "获取温度为：" + str(text)
        if (Frame.buf[2] == '0B'): # 读取当前坐标
            x = int.from_bytes(bytes.fromhex(Frame.buf[3] + Frame.buf[4]), byteorder='big')
            y = int.from_bytes(bytes.fromhex(Frame.buf[5] + Frame.buf[6]), byteorder='big')
            z = int.from_bytes(bytes.fromhex(Frame.buf[7] + Frame.buf[8]), byteorder='big')
            text = '('+ str(x) + ','+ str(y) + ',' + str(z) + ')'
            self.Getpos_lineEdit.setText(text)
            text = "获取坐标为" + text
        if (Frame.buf[2] == '0D'): # 读取当前坐标
            x = Frame.buf[4]
            y = Frame.buf[6]
            z = Frame.buf[8]
            text = '('+ x + ','+ y + ',' + z + ')'
            if x == y == z == '01':
                self.Startpos_Button.setText("已初始化")
            elif x == y == z == '00':
                self.Startpos_Button.setText("未初始化")
            text = "获取初始化数据为：" + text
        print("转化后：", text)



    def Setpos(self):
        self.ser1.d.setDataTodo('0A', self.Posx_spinBox.value(), self.Posy_spinBox.value(),self.Posz_spinBox.value())
        self.ser1.serialSend()

    def Getpos(self): # 获取坐标
        self.ser1.d.setDataTodo('0B')
        self.ser1.serialSend()

    def Stra(self): # 运动轴回到原点
        self.ser1.d.setDataTodo('0C')
        self.ser1.serialSend()

    def Startpos(self): # 是否初始化
        self.ser1.d.setDataTodo('0D')
        self.ser1.serialSend()

    def process_data(self, data):
        print("process_data:", data)
        # 解析数据
        values = re.findall(r'\d+', data)
        if len(values) == self.data_len:
            values = [int(v) for v in values]
            for i, value in enumerate(values):
                self.data[i].append(value)
                if len(self.data[i]) > 300:  # 限制数据长度
                    self.data[i].pop(0)
            self.redraw()  # 更新图表
            self.update_table()  # 更新表格


    def Save_file(self):
        if self.ser.read_flag:
            self.ser1.d.setDataTodo(5,0)
            self.ser1.serialSend()
        self.savefile()

    def savefolder(self):
        foldername = QFileDialog.getExistingDirectory(None, "Select Folder", "/")
        if foldername:  # 如果用户选择了文件夹
            self.Folder_lineEdit.setText(foldername)  # 设置 QLineEdit 的文本为选择的文件夹路径
        else:  # 如果用户取消了操作
            print("用户取消了选择")

    def savefile(self):
        folder_path = self.Folder_lineEdit.text().strip()  # 获取文本内容并去除首尾空格
        if folder_path:  # 如果有内容
            filename = QFileDialog.getSaveFileName(None, "open file", folder_path, "TEXT Files(*.txt)")
        else:  # 如果没有内容
            filename = QFileDialog.getSaveFileName(None, "open file", "/", "TEXT Files(*.txt)")
        # print(filename)
        if filename[0] == "" or filename is None:
            return
        try:
            with open(filename[0], "w") as f:
                sensor_names_str = " ".join(self._data_visible)
                f.write(sensor_names_str + "\n")
                # 筛选出选中的传感器数据
                selected_data = [self.data[g_var.sensors.index(sensor)] for sensor in self._data_visible]

                # 转置筛选后的数据
                transposed_data = list(map(list, zip(*selected_data)))

                # 将转置后的数据写入文件
                for row in transposed_data:
                    row_str = " ".join(map(str, row))
                    f.write(row_str + "\n")
        except Exception as e:
            print("保存失败: " + str(e))

    def check_check_state(self, item):
        """
        检查并处理可复选项 item 的状态变化。
        """
        if item.column() == 0:
            sensor_name = item.text()
            checked = item.checkState() == Qt.CheckState.Checked

            if checked:
                if sensor_name not in self._data_visible:
                    self._data_visible.append(sensor_name)
            else:
                if sensor_name in self._data_visible:
                    self._data_visible.remove(sensor_name)
            self.redraw()

    def redraw(self):
        # print("redraw")
        """
        Process data from store and prefer to draw.
        :return:
        """
        # 清空所有绘图线
        for line in self._data_lines.values():
            line.setData([], [])  # 清空数据
        # 更新绘图
        for sensor_name in self._data_visible:  # 只处理选中的传感器
            index = g_var.sensors.index(sensor_name)  # 获取传感器在 g_var.sensors 中的索引
            data_list = self.data[index]  # 获取对应的数据列表
            if data_list:  # 如果数据列表不为空
                if sensor_name in self._data_lines:
                    self._data_lines[sensor_name].setData(range(len(data_list)), data_list)  # 更新已存在的绘图线
                else:
                    self._data_lines[sensor_name] = self.plot_widget.plot(
                        range(len(data_list)),
                        data_list,
                        pen=pg.mkPen(self.get_currency_color(sensor_name), width=3),
                    )  # 创建新的绘图线
        # print(len(data_list))
        if len(data_list) == self.time:
            self.ser.d.setDataTodo(5,0)
            self.ser1.stop()

    def update_table(self):
        for i, sensor_name in enumerate(g_var.sensors):
            value = self.data[i][-1] if self.data[i] else 0
            # color = self.get_currency_color(sensor_name)  # 获取传感器名称的颜色

            item_name = QStandardItem()  # 创建一个item_name对象，用于表示传感器名称
            item_name.setText(sensor_name)  # 设置传感器名称作为文本
            # item_name.setForeground(QBrush(QColor("red")))
            item_name.setForeground(QBrush(QColor(self.get_currency_color(sensor_name))))  # 设置传感器名称的前景色（文本颜色）
            item_name.setCheckable(True)  # 设置该传感器名称项为可复选
            item_name.setEditable(False)  # 设置传感器名称不可编辑
            if sensor_name in self._data_visible:
                item_name.setCheckState(Qt.CheckState.Checked)  # 如果传感器名称在默认显示列表中，则设置其复选框为选中状态

            item_value = QStandardItem(f"{value:.2f}")  # 创建一个item_value对象，用于表示传感器数据
            item_value.setTextAlignment(
                Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)  # 设置传感器数据的文本对齐方式为右对齐且垂直居中
            item_value.setEditable(False)  # 设置传感器数据不可编辑
            self.model.setColumnCount(2)  # 设置模型的列数为 2（货币名称和对应的值）
            self.model.setItem(i, 0, item_name)
            self.model.setItem(i, 1, item_value)


    def get_currency_color(self, sensor):
        if sensor not in self._data_colors:
            self._data_colors[sensor] = next(self.color_cycle)

        return self._data_colors[sensor]

    def generate_random_hex_color(self):
        """生成一个随机的十六进制颜色代码"""
        return "#{:02x}{:02x}{:02x}".format(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def generate_random_color_list(self, length):
        """生成一个指定长度的随机十六进制颜色代码列表"""
        return [self.generate_random_hex_color() for _ in range(length)]

    def closeEvent(self, event):
        # 1. 停所有串口线程
        if hasattr(self, 'smng'):
            for sop in self.smng.ser_arr:
                if hasattr(sop, 'read_flag'):
                    sop.read_flag = False
                    # 如果用了 QThread，也调 quit + wait
                    if hasattr(sop, 'thread') and sop.thread.isRunning():
                        sop.stop()
                        sop.thread.quit()
                        sop.thread.wait()

        event.accept()  # 允许窗口真正关闭


# #
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     app.setStyle("WindowsVista")  # 强制使用 WindowsVista 主题
#     window = GraphShowWindow()
#     window.show()
#     sys.exit(app.exec())