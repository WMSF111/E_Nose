import sys
from Gragn_uishow import GraphShowWindow
from PySide6.QtWidgets import QApplication

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("WindowsVista")  # 强制使用 WindowsVista 主题
    window = GraphShowWindow()
    window.show()
    sys.exit(app.exec())



