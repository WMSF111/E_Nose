from PySide2.QtWidgets import QApplication, QRadioButton, QLineEdit, QListWidget, QListWidgetItem, QVBoxLayout
import csv
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import global_vars
import Picture.echart_P as plotter


class ComboCheckbox:
    def __init__(self, data, ComboBox, The_ui):
        self.ui = The_ui
        self.items = data
        self.radio_buttons = []
        self.selected_column = None
        self.setup_ui(ComboBox)

    def setup_ui(self, ComboBox):
        self.text = QLineEdit()
        q = QListWidget()

        for i in range(len(self.items)):
            self.radio_buttons.append(QRadioButton(self.items[i]))
            item = QListWidgetItem(q)
            q.setItemWidget(item, self.radio_buttons[i])

            self.radio_buttons[i].clicked.connect(self.show_selected)

        self.text.setReadOnly(True)
        ComboBox.setLineEdit(self.text)
        ComboBox.setModel(q.model())
        ComboBox.setView(q)

    def get_selected(self) -> tuple:
        for i in range(len(self.items)):
            if self.radio_buttons[i].isChecked():
                return self.radio_buttons[i].text(), i
        return None, None

    def show_selected(self):
        self.text.clear()
        result, i = self.get_selected()
        if result:
            self.text.setText(result)
            return result, i

    @staticmethod
    def read_csv_return_header(csv_file):
        with open(csv_file, 'r', encoding='utf-8-sig') as file:
            csv_reader = csv.reader(file)
            header = next(csv_reader)
            header_dict = {col_name: index for index, col_name in enumerate(header)}
            return header_dict, header


class MainApplication:
    def __init__(self, df, ui, LH_Button, widget, logger):
        self.ui = ui
        self.logger = logger
        # self.connect_signals(LH_Button, widget, df, ui)
        self.plotter = plotter.Plotter(df, logger)
        self.on_button_click(widget, df, ui)
        

    def connect_signals(self, LH_Button, widget, df, ui):
        LH_Button.clicked.connect(lambda: self.on_button_click(widget, df, ui))

    def clear_previous_plot(self, layout, widget):
        # 删除之前的绘图
        layout = widget.layout()
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget_to_remove = item.widget()
                if widget_to_remove is not None:
                    widget_to_remove.setParent(None)
                    widget_to_remove.deleteLater()


    def on_button_click(self, widget, df, ui):

        if widget == ui.scrollArea_L1:
            selected_value1, selected_index1 = global_vars.selected_value1_1, global_vars.selected_index1_1
            selected_value2, selected_index2 = global_vars.selected_value2_1, global_vars.selected_index2_1
            selected_value3, selected_index3 = global_vars.selected_value3_1, global_vars.selected_index3_1
            selected_value4, selected_index4 = global_vars.selected_value4_1, global_vars.selected_index4_1
            selected_value5, selected_index5 = global_vars.selected_value5_1, global_vars.selected_index5_1
        if widget == ui.scrollArea_L2:
            selected_value1, selected_index1 = global_vars.selected_value1_2, global_vars.selected_index1_2
            selected_value2, selected_index2 = global_vars.selected_value2_2, global_vars.selected_index2_2
            selected_value3, selected_index3 = global_vars.selected_value3_2, global_vars.selected_index3_2
            selected_value4, selected_index4 = global_vars.selected_value4_2, global_vars.selected_index4_2
            selected_value5, selected_index5 = global_vars.selected_value5_2, global_vars.selected_index5_2
        if widget == ui.scrollArea_L3:
            selected_value1, selected_index1 = global_vars.selected_value1_3, global_vars.selected_index1_3
            selected_value2, selected_index2 = global_vars.selected_value2_3, global_vars.selected_index2_3
            selected_value3, selected_index3 = global_vars.selected_value3_3, global_vars.selected_index3_3
            selected_value4, selected_index4 = global_vars.selected_value4_3, global_vars.selected_index4_3
            selected_value5, selected_index5 = global_vars.selected_value5_3, global_vars.selected_index5_3
        if widget == ui.scrollArea_L4:
            selected_value1, selected_index1 = global_vars.selected_value1_4, global_vars.selected_index1_4
            selected_value2, selected_index2 = global_vars.selected_value2_4, global_vars.selected_index2_4
            selected_value3, selected_index3 = global_vars.selected_value3_4, global_vars.selected_index3_4
            selected_value4, selected_index4 = global_vars.selected_value4_4, global_vars.selected_index4_4
            selected_value5, selected_index5 = global_vars.selected_value5_4, global_vars.selected_index5_4

        if selected_value1 is not None and selected_value2 is not None and selected_value4 is not None:
            width,height = widget.width(), widget.height()
            # 清除之前的画布
            layout = widget.layout()
            self.clear_previous_plot(layout, widget)
            if global_vars.headers_flag == 0:
                self.plotter.plot_chart(selected_index1, selected_index2, selected_index3, selected_index5, selected_value1, selected_value2, selected_value3, selected_value4, width*0.98, height*0.98)
            widget.setWidget(self.plotter.bro)  
        else:
            print("缺少参数")

# if __name__ == '__main__':
#     app = QApplication(sys.argv)

#     file_path = (os.path.dirname(__file__) + '\\abc.csv')
#     df = pd.read_csv(file_path)
#     ui_file_path = (os.path.dirname(__file__) + '\\Form - untitled.ui')
#     ylabel = '合同额(百万)'
#     title = '不同年份对应的合同额柱状图'
#     ui = QUiLoader().load(ui_file_path)
#     header_dict, headers = ComboCheckbox.read_csv_return_header(file_path)
#     main_app1 = MainApplication(df, headers, ui, ui.LH_ComboBox_1Y, ui.LH_ComboBox_1X, ui.LH_ComboBox_1L, ui.LH_ComboBox_1, ui.LH_Button, ui.widget_5)
#     main_app2 = MainApplication(df, headers, ui, ui.LH_ComboBox_2Y, ui.LH_ComboBox_2X, ui.LH_ComboBox_2L, ui.LH_ComboBox_2, ui.LH_Button_2,ui.widget_6)
#     main_app1 = MainApplication(df, headers, ui, ui.LH_ComboBox_3Y, ui.LH_ComboBox_3X, ui.LH_ComboBox_3L, ui.LH_ComboBox_3, ui.LH_Button_3, ui.widget_7)
#     main_app2 = MainApplication(df, headers, ui, ui.LH_ComboBox_4Y, ui.LH_ComboBox_4X, ui.LH_ComboBox_4L, ui.LH_ComboBox_4, ui.LH_Button_4,ui.widget_8)
#     app.exec_()