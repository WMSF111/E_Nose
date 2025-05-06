import sys
from PySide6.QtWidgets import QApplication, QWidget, QFileDialog
import PySide6.QtCore as QtCore
from resource_ui.ui_pfile.Alg_show import Ui_Alg_show  # 导入生成的 UI 类

class AlgShow_Init(QWidget):
    def __init__(self):
        super(AlgShow_Init, self).__init__()
        self.ui = Ui_Alg_show()
        self.ui.setupUi(self)  # 设置 UI 界面
        self.ui.Di_Re_ComboBox.setStyleSheet("QComboBox { combobox-popup: 0; } " + self.ui.Di_Re_ComboBox.styleSheet())
        self.ui.Di_Re_ComboBox.setIconSize(QtCore.QSize(16, 16))  # 设置合适的图标大小

        # 绑定按钮点击事件
        self.ui.toolButton.clicked.connect(self.select_file)

    def select_file(self):
        # 弹出文件选择对话框，允许选择文件或文件夹
        file_path, _ = QFileDialog.getOpenFileName(self, "选择文件", "", "All Files (*)")
        if not file_path:  # 如果用户取消选择
            return

        # 将选择的文件路径显示到 FilePath_lineEdit 中
        self.ui.FilePath_lineEdit.setText(file_path)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = AlgShow_Init()
    main_window.show()
    sys.exit(app.exec())