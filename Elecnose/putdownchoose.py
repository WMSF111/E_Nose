from qfluentwidgets import (Flyout, InfoBarIcon, FlyoutAnimationType)
from PySide2.QtWidgets import QWidget, QVBoxLayout
import global_vars
from matplotlib.backends.backend_qtagg import FigureCanvas
import Picture.echart_P as echart_P
import Picture.Show_pic as Show_pic
import Picture.figureCanvas as fc
import train.algorithm as algorithm


class Demo(QWidget):

    def __init__(self, LH_Button, ui, stats1, stats2, stats3, stats4, stats5, logger):
        super().__init__()
        self.Button = LH_Button
        self.logger = logger
        self.stats1 = stats1
        self.stats2 = stats2
        self.stats3 = stats3
        self.stats4 = stats4
        self.stats5 = stats5
        the_end = algorithm.alg(global_vars.file_text_DataFrame)
        whindow = fc.MainWindow(ui, the_end.fig)  # 创建画布
        self.Button.clicked.connect(lambda: self.on_button_click(whindow, the_end, ui))
        self.plotter = echart_P.Plotter(global_vars.file_text_DataFrame, logger)

    def Get_value(self, ui):
        # 获取不同下拉框所选的内容及索引
        selected_value1, selected_index1 = self.stats1.value, self.stats1.index
        selected_value2, selected_index2 = self.stats2.value, self.stats2.index
        selected_value3, selected_index3 = self.stats3.value, self.stats3.index
        selected_value4, selected_index4 = self.stats4.value, self.stats4.index
        selected_value5, selected_index5 = self.stats5.value, self.stats5.index
        # 将内容和索引保存至全局变量中，方便右侧选择后直接进行图片绘制
        global_vars.selected_value1_1, global_vars.selected_index1_1 = selected_value1, selected_index1
        global_vars.selected_value2_1, global_vars.selected_index2_1 = selected_value2, selected_index2
        global_vars.selected_value3_1, global_vars.selected_index3_1 = selected_value3, selected_index3
        global_vars.selected_value4_1, global_vars.selected_index4_1 = selected_value4, selected_index4
        global_vars.selected_value5_1, global_vars.selected_index5_1 = selected_value5, selected_index5

        return selected_index1, selected_index2, selected_index3, selected_index5, selected_value1, selected_value2, selected_value3, selected_value4, selected_value5

    def on_button_click(self, window, the_end, ui):
        window.clear_canvas()
        selected_index1, selected_index2, selected_index3, selected_index5, selected_value1, selected_value2, selected_value3, selected_value4, selected_value5 = self.Get_value(
            ui)
        the_end.choose_al(selected_value4, int(selected_value3))
        if (selected_value3 != ' '):
            the_end.num = int(selected_value3)
        Show_pic.draw_line(ui, the_end.name, the_end.num, the_end.fig, the_end.target, the_end.finalData, the_end.data)
        # 重新绘制画布
        window.canvas.draw()
        self.logger.info("左边四个开始画图（按钮按下）")
        if the_end.num != 0:
            the_end.train_data()
        # 格式化文本
        result_text = (
            f"模型准确率: {the_end.accuracy_score}\n\n"
            f"混淆矩阵:\n{the_end.confusion_matrix}\n\n"
            f"分类报告:\n{the_end.classification_report}"
        )
        # 使用setPlainText()设置文本
        ui.textBrowser.setPlainText(result_text)
        # 使用append()追加文本
        # 如果必要的几个选项已经选择了，则进行图表绘制

        # if type(global_vars.df.iloc[1, selected_index1]) == str:
        #     new_widget = QWidget()
        #     widget.setWidget(new_widget)
        #     self.showFlyout2()
        #     print(type(global_vars.df.iloc[1, selected_index1]))
        # if selected_value5 == "不选" or selected_value4 == "不选":
        #     new_widget = QWidget()
        #     widget.setWidget(new_widget)
        #     self.showFlyout1()
        # elif (selected_value1 is not (None or "不选") and selected_value2 is not (None or "不选")) and (selected_index1 is not -1 and selected_index2 is not -1):
        #     if (selected_value3 is (None or "不选") or selected_index3 is -1) and selected_value4 == "radar":
        #         new_widget = QWidget()
        #         widget.setWidget(new_widget)
        #         self.showFlyout1()
        #         print("缺少第三个标签数据支持")
        #     else:
        #         width,height = widget.width(), widget.height()
        #         #图表绘制函数
        #         self.plotter.plot_chart(selected_index1, selected_index2, selected_index3, selected_index5, selected_value1, selected_value2, selected_value3, selected_value4, width*0.98, height*0.98)
        #         widget.setWidget(self.plotter.bro)
        # else:
        #     new_widget = QWidget()
        #     widget.setWidget(new_widget)
        #     self.showFlyout1()
        #     print("缺少参数")
        # self.logger.info("左边四个画图完毕（按钮按下）")

    def showFlyout1(self):
        Flyout.create(
            icon=InfoBarIcon.SUCCESS,
            title=' ',
            content="缺少必要参数",
            target=self.Button,
            parent=self,
            isClosable=True,
            aniType=FlyoutAnimationType.PULL_UP
        )

    def showFlyout2(self):
        Flyout.create(
            icon=InfoBarIcon.SUCCESS,
            title=' ',
            content="纵轴必须为int类型",
            target=self.Button,
            parent=self,
            isClosable=True,
            aniType=FlyoutAnimationType.PULL_UP
        )


class ComboCheckbox:
    def __init__(self, data, ComboBox, The_ui, num, logger):
        self.logger = logger
        self.logger.info("ComboCheckbox 下拉框开始初始化")
        self.ui = The_ui
        self.radio_buttons = []
        self.selected_column = None
        self.setup_ui(ComboBox, data, num)
        self.index = ComboBox.currentIndex()
        self.value = ComboBox.currentText()

    def setup_ui(self, ComboBox, data, num):
        if data == 0:
            self.items = global_vars.headers_list
        else:
            self.items = data
        ComboBox.clear()
        ComboBox.addItems(self.items)
        ComboBox.addItems(["不选"])
        # 当前选项的索引改变信号
        ComboBox.currentIndexChanged.connect(lambda index: print(ComboBox.currentText()))
        if num != 0:
            # 设置提示文本
            ComboBox.setPlaceholderText("下拉选择")
            # 选中对应项
            if num < len(self.items):
                ComboBox.setCurrentIndex(num)
            else:
                ComboBox.setCurrentIndex(-1)

        # 当前选项的索引改变信号
        ComboBox.currentIndexChanged.connect(lambda index: self.select(ComboBox))

    def select(self, ComboBox):
        self.index = ComboBox.currentIndex()
        self.value = ComboBox.currentText()

    @staticmethod
    def read_df_return_header(df):
        header = df.columns.tolist()
        header_dict = {col_name: index for index, col_name in enumerate(header)}
        return header_dict, header


# 检查左侧框图所选的显示图片的种类
class MainApplication:
    def __init__(self, ui, LH_ComboBox_Y, LH_ComboBox_X, LH_ComboBox_L, LH_ComboBox, ComboBox_C, LH_Button, logger):
        super().__init__()
        self.logger = logger
        self.ui = ui
        self.Button = LH_Button
        # 给下拉框输入选项
        self.stats1 = ComboCheckbox(0, LH_ComboBox_Y, self.ui, -1, logger)
        self.stats2 = ComboCheckbox(0, LH_ComboBox_X, self.ui, -1, logger)
        self.stats3 = ComboCheckbox(['2', '3'], LH_ComboBox_L, self.ui, 0, logger)
        self.stats4 = ComboCheckbox(['LDA', 'PCA'], LH_ComboBox, self.ui, 0,
                                    logger)
        self.stats5 = ComboCheckbox(global_vars.color, ComboBox_C, self.ui, 0, logger)
        w = Demo(LH_Button, ui, self.stats1, self.stats2, self.stats3, self.stats4, self.stats5, self.logger)
