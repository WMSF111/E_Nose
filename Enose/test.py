import sys
from PySide6.QtWidgets import QApplication, QWidget, QTableView, QVBoxLayout, QHeaderView
from PySide6.QtGui import QColor, QStandardItemModel, QStandardItem, QBrush
from PySide6.QtCore import Qt

class ColorTestWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(['Sensor', 'Value'])

        sensors = ["Sensor1", "Sensor2", "Sensor3"]
        values = [10.5, 20.3, 30.7]
        colors = ["red", "green", "blue"]  # 或使用 "#FF0000", "#00FF00", "#0000FF"

        for i, sensor in enumerate(sensors):
            item_name = QStandardItem(sensor)
            item_name.setForeground(QBrush(QColor(colors[i])))  # 设置颜色
            item_name.setCheckable(True)
            item_name.setEditable(False)
            item_name.setFlags(item_name.flags() | Qt.ItemIsEnabled)  # 确保可渲染

            item_value = QStandardItem(f"{values[i]:.2f}")
            item_value.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
            item_value.setEditable(False)

            self.model.appendRow([item_name, item_value])

        self.tableView = QTableView()
        self.tableView.setModel(self.model)
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableView.setStyleSheet("")  # 清空样式表

        layout = QVBoxLayout(self)
        layout.addWidget(self.tableView)
        self.setLayout(layout)

        self.setWindowTitle("Color Test")
        self.resize(400, 300)

if __name__ == "__main__":
    app = QApplication(sys.argv)


    window = ColorTestWindow()
    window.show()
    sys.exit(app.exec())