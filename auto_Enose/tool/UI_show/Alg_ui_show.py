'''测试算法页面'''

import sys
from PySide6.QtWidgets import QApplication, QWidget, QFileDialog
from PySide6.QtGui import QKeySequence, QAction
from resource_ui.alg_puifile.Alg_show import Ui_Alg_show  # 导入生成的 UI 类
import data_file.transfo as transfo
import matplotlib.pyplot as plt
import global_var as glov
from data_file.alg_tabadd import ALG_TAB_ADD

plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置字体为 SimHei
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题


class AlgShow_Init(QWidget, Ui_Alg_show):
    def __init__(self):
        super(AlgShow_Init, self).__init__()
        self.setupUi(self)  # 设置 UI 界面
        self.tabadd = ALG_TAB_ADD(self)
        self.ButInit()
        self.ComboInit()


    def ButInit(self):
        # 绑定按钮点击事件
        self.toolButton.clicked.connect(self.select_file)
        # 设置 TabWidget 的关闭按钮策略
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.tabCloseRequested.connect(self.remove_tab)

    def remove_tab(self, index):
        """删除指定的 Tab"""
        self.tabWidget.removeTab(index)

    def ComboInit(self):
        self.Dimension_ComboBox.addItems(["无", "PCA", "LDA"])  # 聚类算法
        self.Dimension_ComboBox.setCurrentIndex(0)  # 设置默认选择为第一个选项（"无"）
        self.Dimension_ComboBox.activated.connect(self.tabadd.Di_Re_Combo_select)
        self.Reg_ComboBox.addItems(["无", "线性回归"])  # 回归算法
        self.Reg_ComboBox.setCurrentIndex(0)  # 设置默认选择为第一个选项（"无"）
        self.Reg_ComboBox.activated.connect(self.tabadd.Region_Combo_select)
        self.Pre_Button.clicked.connect(self.tabadd.Filter_Combo_select)
        self.Classify_ComboBox.addItems(["无", "SVM", "KNN", "逻辑回归"])  # 添加选项
        self.Classify_ComboBox.setCurrentIndex(0)  # 设置默认选择为第一个选项（"无"）
        self.Classify_ComboBox.activated.connect(self.tabadd.Classify_Combo_select)
    def select_file(self):
        """弹出文件夹选择对话框"""
        folder_path = QFileDialog.getExistingDirectory(
            self,
            "选择文件夹",  # 对话框标题
            "",  # 默认打开的目录（空表示当前目录）
        )
        if folder_path:  # 如果用户选择了文件夹（而不是取消）
            self.FilePath_lineEdit.setText(folder_path)  # 显示到 QLineEdit
            textEdit_DataFrame = transfo.UI_TXT_TO.merge_files_to_dataframe(folder_path) # 遍历文件夹中的.txt合并成trainfile.txt
            self.tabadd.tabset.add_text_tab(textEdit_DataFrame, "原始数据", html=True)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = AlgShow_Init()
    main_window.show()
    sys.exit(app.exec())
