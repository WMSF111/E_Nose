from PySide2.QtWidgets import QWidget
from resource_ui.Ui_Form2 import Ui_Board
from resource_ui.Ui_Form1 import Ui_date_get
from resource_ui.Ui_Form5 import Ui_Form5
from resource_ui.Ui_ChatGPTClient import Ui_Frame

class The_tab1(QWidget, Ui_date_get):
     def __init__(self,parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)


class The_tab2(QWidget, Ui_Board):
     
     def __init__(self,parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)

class The_tab4(QWidget, Ui_Form5):
     
     def __init__(self,parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.baudComboBox.addItems(["115200", "9600", "921600", "19200", "38400", "4800"])


class The_tab5(QWidget, Ui_Frame):

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
