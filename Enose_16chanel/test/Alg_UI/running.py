import sys
from Alg_ui_show import AlgShow_Init
from PySide6.QtWidgets import QApplication

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("WindowsVista")  # 强制使用 WindowsVista 主题
    window = AlgShow_Init()
    window.show()
    sys.exit(app.exec())

    

