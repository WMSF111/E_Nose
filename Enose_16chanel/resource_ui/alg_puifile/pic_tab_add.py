'''算法显示'''
from resource_ui.alg_puifile.Predict_uishow import Ui_Pre_show
from resource_ui.alg_puifile.Classify_uishow import Ui_Classify as Classify_uishow  # 导入生成的 UI 类
from resource_ui.alg_puifile.Regression_uishow import Ui_Regression as Regression_uishow  # 导入生成的 UI 类
from PySide6.QtWidgets import QDialog, QTextEdit, QVBoxLayout, QWidget, QFileDialog, QHBoxLayout # 改为继承 QDialog
from PySide6.QtGui import QKeySequence, QAction
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import global_var as global_var
from matplotlib.figure import Figure
import numpy as np
import pandas as pd
from matplotlib import cm
import matplotlib.pyplot as plt
# from mplcursors import cursor as mplcursors

class ADDTAB():
    def __init__(self, The_QTabWidget):
        self.The_QTabWidget = The_QTabWidget

    # 新建新的绘图TAB
    def add_plot_tab(self, Dnum=2, title="Plot", plot_function=None, plot_function2=None, *args, **kwargs):
        new_tab = QWidget()

        # 创建主垂直布局
        layout = QVBoxLayout(new_tab)

        # 创建一个垂直布局来放置图表
        horizontal_layout = QVBoxLayout()

        # 创建第一个Matplotlib图表
        fig1 = Figure(figsize=(6, 4))
        canvas1 = FigureCanvas(fig1)
        if Dnum == 3:
            ax1 = fig1.add_subplot(111, projection='3d')
        else:
            ax1 = fig1.add_subplot(111)

        # 如果提供了绘图函数，调用它
        if plot_function:
            plot_function(ax1, *args, **kwargs)

        # 将第一个图表添加到水平布局
        horizontal_layout.addWidget(canvas1)

        # 如果需要创建第二个图表
        if plot_function2 != None:
            # 创建第二个Matplotlib图表
            fig2 = Figure(figsize=(6, 4))
            canvas2 = FigureCanvas(fig2)
            if Dnum == 3:
                ax2 = fig2.add_subplot(111, projection='3d')
            else:
                ax2 = fig2.add_subplot(111)

            # 如果提供了绘图函数，调用它
            if plot_function2:
                plot_function2(ax2, *args, **kwargs)

            # 将第二个图表添加到水平布局
            horizontal_layout.addWidget(canvas2)

        # 将水平布局添加到主垂直布局中
        layout.addLayout(horizontal_layout)

        # 添加新的 Tab 到 QTabWidget
        self.The_QTabWidget.addTab(new_tab, title)

        # 切换到新添加的 Tab
        self.The_QTabWidget.setCurrentIndex(self.The_QTabWidget.count() - 1)

    # def add_plot_tab(self, Dnum = 2, title="Plot", plot_function=None, *args, **kwargs):
    #     new_tab = QWidget()
    #     layout = QVBoxLayout(new_tab)
    #
    #     # 创建 Matplotlib 图表
    #     fig = Figure(figsize=(6, 4))
    #     canvas = FigureCanvas(fig)
    #     # 将图表添加到布局
    #     if Dnum == 3:
    #         ax = fig.add_subplot(111, projection='3d')
    #     else:
    #         ax = fig.add_subplot(111)
    #
    #     # 如果提供了绘图函数，调用它
    #     if plot_function:
    #         plot_function(ax, *args, **kwargs)
    #
    #     # 将图表添加到布局
    #     layout.addWidget(canvas)
    #
    #     # 添加新的 Tab 到 QTabWidget
    #     self.The_QTabWidget.addTab(new_tab, title)
    #     # 切换到新添加的 Tab
    #     self.The_QTabWidget.setCurrentIndex(self.The_QTabWidget.count() - 1)

    # 创建一个新的文本Tab
    def add_text_tab(self, finaldata, title="Plot"):
        new_tab = QWidget()
        layout = QVBoxLayout(new_tab)
        new_textedit = QTextEdit()
        new_textedit.setFontFamily("Consolas")  # 设置为固定宽度字体（Courier）
        # 将图表添加到布局
        layout.addWidget(new_textedit)
        title = title

        new_textedit.append(finaldata)

        # 添加新的 Tab 到 QTabWidget
        self.The_QTabWidget.addTab(new_tab, title)
        self.The_QTabWidget.setCurrentIndex(self.The_QTabWidget.count() - 1)  # 切换到新添加的 Tab
        # 设置保存快捷键
        self.set_save_shortcut(new_tab, str(finaldata))

    def set_save_shortcut(self, new_tab, text):
        """为新 Tab 设置保存快捷键"""
        # 创建一个 QAction
        save_action = QAction("Save", self.The_QTabWidget)
        save_action.setShortcut(QKeySequence("Ctrl+S"))
        save_action.triggered.connect(lambda: self.save_text(text))

        # 将 QAction 添加到新 Tab 的上下文菜单
        new_tab.addAction(save_action)

    def save_text(self, text):
        """保存当前图表"""
        file_path, _ = QFileDialog.getSaveFileName(None, "Save result", global_var.folder_path, "TXT Files (*.txt);;All Files (*)")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(text)
            print(f"Plot saved to {file_path}")
        # if file_path:
        #     file_path.write(text)
        #     print(f"Plot saved to {file_path}")

def draw_scatter(ax, name, num, target, finalData, data=None):
    """
            绘制不同维度的散点图。

            参数:
            ax: Matplotlib 的 Axes 对象
            name: 主成分名称列表
            num: 维度数量（2 或 3）
            target: 目标变量（类别标签）
            finalData: PCA 转换后的数据
            data: 原始数据（仅在 num==0 时使用）
            """
    print(finalData)
    if num == 3:
        # 创建一个颜色映射对象
        cmap = cm.get_cmap('tab10')

        # 获取类别值的唯一值和对应的索引
        unique_categories = np.unique(target)

        # 绘制所有数据点，并为每个类别使用不同的颜色
        for i, category in enumerate(unique_categories):
            category_data = finalData[target == category]  # 提取出 finalData 中对应当前类别的数据行
            color = cmap(i % cmap.N)
            scatter = ax.scatter(category_data[:, 0], category_data[:, 1], category_data[:, 2], color=color,
                                 label=f"Category {category}")

        # 添加图例，只显示每种颜色的标签
        handles, labels = ax.get_legend_handles_labels()
        unique_handles = list(set(handles))
        unique_labels = [label for handle, label in zip(handles, labels) if handle in unique_handles]
        ax.legend(unique_handles, unique_labels, title="Category", loc='upper right', bbox_to_anchor=(1.4, 1))

        # 设置坐标轴标签
        if len(name) != 0:
            ax.set_xlabel("PC" + name[0])
            ax.set_ylabel("PC" + name[1])
            ax.set_zlabel("PC" + name[2])
        else:
            ax.set_xlabel("PC1")
            ax.set_ylabel("PC2")
            ax.set_zlabel("PC3")

    elif num == 2:
        # 创建一个颜色映射对象
        cmap = cm.get_cmap('tab10')

        # 获取类别值的唯一值和对应的索引
        unique_categories = np.unique(target)

        # 绘制所有数据点，并为每个类别使用不同的颜色
        for i, category in enumerate(unique_categories):
            category_data = finalData[target == category]
            color = cmap(i % cmap.N)
            scatter = ax.scatter(category_data[:, 0], category_data[:, 1], color=color, label=f'{category}')

        # 添加图例，只显示每种颜色的标签
        handles, labels = ax.get_legend_handles_labels()
        unique_handles = list(set(handles))
        unique_labels = [label for handle, label in zip(handles, labels) if handle in unique_handles]
        ax.legend(unique_handles, unique_labels, title="Category", loc='upper right')

        # 设置坐标轴标签
        if len(name) != 0:
            ax.set_xlabel("PC" + name[0])
            ax.set_ylabel("PC" + name[1])
        else:
            ax.set_xlabel("PC1")
            ax.set_ylabel("PC2")

    elif num == 0:
        cols = data.columns[1:]  # 假设第一列是目标变量
        for column in cols:
            ax.scatter(data[column], target, label=column)

        # 添加标题和标签
        ax.set_title('Scatter Plot of Specific Columns with Target Variable')
        ax.set_xlabel('Independent Variables')
        ax.set_ylabel('Dependent Variable')

        # 添加图例
        ax.legend()

class PCASHOW(QDialog, Classify_uishow):  # 继承 QDialog
    def __init__(self, parent=None):
        super(PCASHOW, self).__init__(parent)  # 设置父窗口
        self.setupUi(self)  # 设置 UI 界面
        self.ButInit()
        self.Dinum = self.Di_spinBox.value()
        self.Contrnum = self.Di_spinBox_2.value()
        self.file_path = ' '

    def ButInit(self):
        # 绑定按钮点击事件
        self.pushButton.clicked.connect(self.num_select)
        self.toolButton.clicked.connect(self.select_file)


    def num_select(self):
        """弹出文件夹选择对话框"""
        self.Dinum = self.Di_spinBox.value()
        self.Contrnum = self.Di_spinBox_2.value()
        self.accept()  # 关闭对话框并返回 QDialog.Accepted

    def select_file(self):
        """弹出文件夹选择对话框"""
        folder_path, _ = QFileDialog.getOpenFileName(None, "Open File", "", "All Files (*)")
        if folder_path:  # 如果用户选择了文件夹（而不是取消）
            self.FilePath_lineEdit.setText(folder_path)  # 显示到 QLineEdit
            self.file_path = folder_path

    def plot_scree_plot(self, ax, variance_ratios):
        # fig, ax = plt.subplots()  # 正确解包
        """绘制 PCA 碎石图"""
        ax.plot(range(1, len(variance_ratios) + 1), variance_ratios, 'o-', label='单个主成分贡献率')
        ax.plot(range(1, len(variance_ratios) + 1), np.cumsum(variance_ratios), 's-', label='累积贡献率')
        ax.axhline(y=0.8, color='r', linestyle='--', label='80% 阈值')  # 标记目标阈值
        ax.set_xlabel("主成分数量")
        ax.set_ylabel("方差贡献率")
        ax.set_title("PCA 碎石图")
        ax.legend()
        ax.grid()


class LDASHOW(QDialog, Classify_uishow):  # 继承 QDialog
    def __init__(self, parent=None):
        super(LDASHOW, self).__init__(parent)  # 设置父窗口
        self.setupUi(self)  # 设置 UI 界面
        self.label.setText("LDA维度（2-传感器数）")
        self.ButInit()
        self.Dinum = self.Di_spinBox.value()
        self.Contrnum = self.Di_spinBox_2.value()

    def ButInit(self):
        # 绑定按钮点击事件
        self.pushButton.clicked.connect(self.num_select)
        self.toolButton.clicked.connect(self.select_file)

    def num_select(self):
        """弹出文件夹选择对话框"""
        self.Dinum = self.Di_spinBox.value()
        self.Contrnum = self.Di_spinBox_2.value()
        self.accept()  # 关闭对话框并返回 QDialog.Accepted

    def select_file(self):
        """弹出文件夹选择对话框"""
        folder_path, _ = QFileDialog.getOpenFileName(None, "Open File", "", "All Files (*)")
        if folder_path:  # 如果用户选择了文件夹（而不是取消）
            self.FilePath_lineEdit.setText(folder_path)  # 显示到 QLineEdit
            self.file_path = folder_path

    def plot_lda_variance_ratio(self, ax, variance_ratios, Contrnum):
        """绘制 LDA 解释方差比图"""
        # 绘制单个主成分的解释方差比
        # fig, ax = plt.subplots()  # 正确解包
        ax.plot(range(1, len(variance_ratios) + 1), variance_ratios, 'o-', label='单个主成分解释方差比')

        # 绘制累积解释方差比
        cumulative_variance_ratios = np.cumsum(variance_ratios)
        ax.plot(range(1, len(cumulative_variance_ratios) + 1), cumulative_variance_ratios, 's-', label='累积解释方差比')

        # 标记目标阈值（例如 80%）
        ax.axhline(y=0.8, color='r', linestyle='--', label=f"{Contrnum}% 阈值")

        # 设置坐标轴标签和标题
        ax.set_xlabel("主成分数量")
        ax.set_ylabel("解释方差比")
        ax.set_title("LDA 解释方差比图")

        # 添加图例
        ax.legend()

        # 添加网格
        ax.grid()


class LRSHOW(QDialog, Regression_uishow):  # 继承 QDialog
    def __init__(self, parent=None):
        super(LRSHOW, self).__init__(parent)  # 设置父窗口
        self.setupUi(self)  # 设置 UI 界面
        self.ButInit()
        self.desize = self.doubleSpinBox.value()


    def ButInit(self):
        # 绑定按钮点击事件
        self.pushButton_2.clicked.connect(self.num_select)
        self.toolButton.clicked.connect(self.select_file)

    def num_select(self):
        """选择了选择模型：关闭对话框"""
        self.desize = self.doubleSpinBox.value()
        self.accept()  # 关闭对话框并返回 QDialog.Accepted

    def select_file(self):
        """弹出文件夹选择对话框"""
        folder_path, _ = QFileDialog.getOpenFileName(None, "Open File", "", "All Files (*)")
        if folder_path:  # 如果用户选择了文件夹（而不是取消）
            self.FilePath_lineEdit.setText(folder_path)  # 显示到 QLineEdit
            self.file_path = folder_path

    def plot_confusion(self, ax, confusion , labels_name):
        """绘制混淆矩阵"""
        confusion = np.array(confusion)  # 将list类型转换成数组类型，如果已经是numpy数组类型，则忽略此步骤。
        # 归一化，防止除以零
        row_sums = confusion.sum(axis=1, keepdims=True)
        confusion_normalized = confusion / row_sums if row_sums.all() != 0 else confusion
        # 显示归一化后的混淆矩阵
        im = ax.imshow(confusion_normalized, interpolation='nearest', cmap=plt.cm.Blues)

        # 设置标题
        ax.set_title("混淆矩阵")

        # 添加颜色条
        plt.colorbar(im, ax=ax)

        # 获取标签的间隔数
        num_class = np.arange(len(labels_name))

        # 设置坐标轴
        ax.set_xticks(num_class)
        ax.set_xticklabels(labels_name, rotation=90)
        ax.set_yticks(num_class)
        ax.set_yticklabels(labels_name)

        # 设置坐标轴标签
        ax.set_ylabel('True label')
        ax.set_xlabel('Predicted label')


class PRESHOW(QDialog, Ui_Pre_show):  # 继承 QDialog
    def __init__(self, parent=None):
        super(PRESHOW, self).__init__(parent)  # 设置父窗口
        self.setupUi(self)  # 设置 UI 界面
        self.ButInit()
        self.Pre_ComboBox.addItems(["不选", "算术平均滤波法", "递推平均滤波法", "中位值平均滤波法",
                           "一阶滞后滤波法", "加权递推平均滤波法", "消抖滤波法", "限幅消抖滤波法"])
        self.Valchoose_ComboBox.addItems(["不选", "平均值", "中位数", "众数"])
        self.PreAlg = self.Pre_ComboBox.currentText()
        self.ValAlg = self.Valchoose_ComboBox.currentText()
        self.file_path = ' '

    def ButInit(self):
        # 绑定按钮点击事件
        self.pushButton.clicked.connect(self.Alg_select) # 完成设置
        self.toolButton.clicked.connect(self.select_file) # 选择文件

    def Alg_select(self):
        """弹出文件夹选择对话框"""
        self.PreAlg = self.Pre_ComboBox.currentText()
        self.ValAlg = self.Valchoose_ComboBox.currentText()
        self.accept()  # 关闭对话框并返回 QDialog.Accepted

    def select_file(self):
        """弹出文件夹选择对话框"""
        folder_path, _ = QFileDialog.getOpenFileName(None, "Open File", "", "All Files (*)")
        if folder_path:  # 如果用户选择了文件夹（而不是取消）
            self.FilePath_lineEdit.setText(folder_path)  # 显示到 QLineEdit
            self.file_path = folder_path

    def plot_data(self, ax, data, result):
        data = data.iloc[1:, 1:]
        data = data.apply(pd.to_numeric, errors='coerce')
        # ax = data.plot()  # 直接使用 DataFrame 的 plot 方法,按列绘制
        data.plot(ax=ax)  # 在传入的 ax 上绘图
        ax.set_title("原始数据")

    def plot_result(self, ax, data, result):
        data = result.iloc[1:, 1:]
        data = data.apply(pd.to_numeric, errors='coerce')
        # ax = data.plot()  # 直接使用 DataFrame 的 plot 方法,按列绘制
        data.plot(ax=ax)  # 在传入的 ax 上绘图
        ax.set_title("滤波后数据")