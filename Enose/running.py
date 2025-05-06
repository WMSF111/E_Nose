import sys
import Enose.tool.UI_show.MainWindow_ui_show as Main_Win
from PySide6.QtWidgets import QApplication

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main_Win.MianWindow_Init()
    window.show()
    sys.exit(app.exec())

    

