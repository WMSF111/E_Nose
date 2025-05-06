from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import numpy as np
from PySide2.QtWidgets import QMainWindow, QGraphicsScene, QGraphicsView, QVBoxLayout, QWidget, QApplication
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile

class MainWindow(QMainWindow):
    def __init__(self, ui ,fig):
        super().__init__()
        self.canvas = FigureCanvas(fig)
        layout = QVBoxLayout(ui.graphicsView)
        layout.addWidget(self.canvas)
        self.canvas.draw()

    
    def clear_canvas(self):
        # 清除图形
        self.canvas.figure.clf()
        # 重新绘制画布
        self.canvas.draw()


# if __name__ == "__main__":


#     app = QApplication(sys.argv)
#     mainWindow = MainWindow()
#     mainWindow.show()
#     sys.exit(app.exec_())
