# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Form.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from qfluentwidgets import ComboBox
from qfluentwidgets import PushButton
from qfluentwidgets import label


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1885, 1117)
        self.verticalLayout_5 = QVBoxLayout(Form)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"background-image: url(:/111.png);")
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.verticalLayout_8 = QVBoxLayout(self.tab_7)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label = QLabel(self.tab_7)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamily(u"\u9ed1\u4f53")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet(u"font: 22pt \"Agency FB\";\n"
"font: 18pt \"\u9ed1\u4f53\";")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label)

        self.label_2 = QLabel(self.tab_7)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setFamily(u"Microsoft YaHei")
        font1.setPointSize(9)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(3)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"font: 9pt \"Agency FB\";\n"
"font: 25 9pt \"Microsoft YaHei\";")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_2)

        self.line_2 = QFrame(self.tab_7)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_7.addWidget(self.line_2)

        self.textEdit = QTextEdit(self.tab_7)
        self.textEdit.setObjectName(u"textEdit")

        self.verticalLayout_7.addWidget(self.textEdit)


        self.verticalLayout_8.addLayout(self.verticalLayout_7)

        self.tabWidget.addTab(self.tab_7, "")
        self.tab_8 = QWidget()
        self.tab_8.setObjectName(u"tab_8")
        self.gridLayout_7 = QGridLayout(self.tab_8)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.Top_widget = QWidget(self.tab_8)
        self.Top_widget.setObjectName(u"Top_widget")
        self.verticalLayout = QVBoxLayout(self.Top_widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Title = label.PixmapLabel(self.Top_widget)
        self.Title.setObjectName(u"Title")
        self.Title.setStyleSheet(u"font: 18pt \"\u9ed1\u4f53\";")
        self.Title.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.Title)

        self.Title_littel = label.PixmapLabel(self.Top_widget)
        self.Title_littel.setObjectName(u"Title_littel")
        self.Title_littel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.Title_littel)

        self.line = QFrame(self.Top_widget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)


        self.gridLayout_7.addWidget(self.Top_widget, 0, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.left_widget = QWidget(self.tab_8)
        self.left_widget.setObjectName(u"left_widget")
        self.gridLayout = QGridLayout(self.left_widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.l_widget1_4 = QWidget(self.left_widget)
        self.l_widget1_4.setObjectName(u"l_widget1_4")
        self.verticalLayout_4 = QVBoxLayout(self.l_widget1_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_4)

        self.LH_label_4 = label.PixmapLabel(self.l_widget1_4)
        self.LH_label_4.setObjectName(u"LH_label_4")

        self.horizontalLayout_9.addWidget(self.LH_label_4)

        self.formLayout_7 = QFormLayout()
        self.formLayout_7.setObjectName(u"formLayout_7")
        self.LH_labelY_4 = QLabel(self.l_widget1_4)
        self.LH_labelY_4.setObjectName(u"LH_labelY_4")

        self.formLayout_7.setWidget(0, QFormLayout.LabelRole, self.LH_labelY_4)

        self.LH_ComboBox_4Y = ComboBox(self.l_widget1_4)
        self.LH_ComboBox_4Y.setObjectName(u"LH_ComboBox_4Y")

        self.formLayout_7.setWidget(0, QFormLayout.FieldRole, self.LH_ComboBox_4Y)

        self.LH_labelX_4 = QLabel(self.l_widget1_4)
        self.LH_labelX_4.setObjectName(u"LH_labelX_4")

        self.formLayout_7.setWidget(1, QFormLayout.LabelRole, self.LH_labelX_4)

        self.LH_ComboBox_4X = ComboBox(self.l_widget1_4)
        self.LH_ComboBox_4X.setObjectName(u"LH_ComboBox_4X")

        self.formLayout_7.setWidget(1, QFormLayout.FieldRole, self.LH_ComboBox_4X)

        self.LH_labelL_4 = QLabel(self.l_widget1_4)
        self.LH_labelL_4.setObjectName(u"LH_labelL_4")

        self.formLayout_7.setWidget(2, QFormLayout.LabelRole, self.LH_labelL_4)

        self.LH_ComboBox_4L = ComboBox(self.l_widget1_4)
        self.LH_ComboBox_4L.setObjectName(u"LH_ComboBox_4L")

        self.formLayout_7.setWidget(2, QFormLayout.FieldRole, self.LH_ComboBox_4L)


        self.horizontalLayout_9.addLayout(self.formLayout_7)

        self.formLayout_8 = QFormLayout()
        self.formLayout_8.setObjectName(u"formLayout_8")
        self.formLayout_8.setFormAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_10 = QLabel(self.l_widget1_4)
        self.label_10.setObjectName(u"label_10")

        self.formLayout_8.setWidget(0, QFormLayout.LabelRole, self.label_10)

        self.LH_ComboBox_4 = ComboBox(self.l_widget1_4)
        self.LH_ComboBox_4.setObjectName(u"LH_ComboBox_4")

        self.formLayout_8.setWidget(0, QFormLayout.FieldRole, self.LH_ComboBox_4)

        self.label_9 = QLabel(self.l_widget1_4)
        self.label_9.setObjectName(u"label_9")

        self.formLayout_8.setWidget(1, QFormLayout.LabelRole, self.label_9)

        self.comboBox_C4 = ComboBox(self.l_widget1_4)
        self.comboBox_C4.setObjectName(u"comboBox_C4")

        self.formLayout_8.setWidget(1, QFormLayout.FieldRole, self.comboBox_C4)


        self.horizontalLayout_9.addLayout(self.formLayout_8)

        self.LH_Button_4 = PushButton(self.l_widget1_4)
        self.LH_Button_4.setObjectName(u"LH_Button_4")

        self.horizontalLayout_9.addWidget(self.LH_Button_4)

        self.horizontalLayout_9.setStretch(0, 1)
        self.horizontalLayout_9.setStretch(1, 2)
        self.horizontalLayout_9.setStretch(2, 2)
        self.horizontalLayout_9.setStretch(3, 2)
        self.horizontalLayout_9.setStretch(4, 1)

        self.verticalLayout_4.addLayout(self.horizontalLayout_9)

        self.widget_8 = QWidget(self.l_widget1_4)
        self.widget_8.setObjectName(u"widget_8")

        self.verticalLayout_4.addWidget(self.widget_8)

        self.verticalLayout_4.setStretch(1, 10)

        self.gridLayout.addWidget(self.l_widget1_4, 1, 1, 1, 1)

        self.l_widget1_3 = QWidget(self.left_widget)
        self.l_widget1_3.setObjectName(u"l_widget1_3")
        self.verticalLayout_2 = QVBoxLayout(self.l_widget1_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_3)

        self.LH_label_3 = label.PixmapLabel(self.l_widget1_3)
        self.LH_label_3.setObjectName(u"LH_label_3")

        self.horizontalLayout_8.addWidget(self.LH_label_3)

        self.formLayout_5 = QFormLayout()
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.LH_labelY_3 = QLabel(self.l_widget1_3)
        self.LH_labelY_3.setObjectName(u"LH_labelY_3")

        self.formLayout_5.setWidget(0, QFormLayout.LabelRole, self.LH_labelY_3)

        self.LH_ComboBox_3Y = ComboBox(self.l_widget1_3)
        self.LH_ComboBox_3Y.setObjectName(u"LH_ComboBox_3Y")

        self.formLayout_5.setWidget(0, QFormLayout.FieldRole, self.LH_ComboBox_3Y)

        self.LH_labelX_3 = QLabel(self.l_widget1_3)
        self.LH_labelX_3.setObjectName(u"LH_labelX_3")

        self.formLayout_5.setWidget(1, QFormLayout.LabelRole, self.LH_labelX_3)

        self.LH_ComboBox_3X = ComboBox(self.l_widget1_3)
        self.LH_ComboBox_3X.setObjectName(u"LH_ComboBox_3X")

        self.formLayout_5.setWidget(1, QFormLayout.FieldRole, self.LH_ComboBox_3X)

        self.LH_labelL_3 = QLabel(self.l_widget1_3)
        self.LH_labelL_3.setObjectName(u"LH_labelL_3")

        self.formLayout_5.setWidget(2, QFormLayout.LabelRole, self.LH_labelL_3)

        self.LH_ComboBox_3L = ComboBox(self.l_widget1_3)
        self.LH_ComboBox_3L.setObjectName(u"LH_ComboBox_3L")

        self.formLayout_5.setWidget(2, QFormLayout.FieldRole, self.LH_ComboBox_3L)


        self.horizontalLayout_8.addLayout(self.formLayout_5)

        self.formLayout_6 = QFormLayout()
        self.formLayout_6.setObjectName(u"formLayout_6")
        self.formLayout_6.setFormAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_8 = QLabel(self.l_widget1_3)
        self.label_8.setObjectName(u"label_8")

        self.formLayout_6.setWidget(0, QFormLayout.LabelRole, self.label_8)

        self.LH_ComboBox_3 = ComboBox(self.l_widget1_3)
        self.LH_ComboBox_3.setObjectName(u"LH_ComboBox_3")

        self.formLayout_6.setWidget(0, QFormLayout.FieldRole, self.LH_ComboBox_3)

        self.label_7 = QLabel(self.l_widget1_3)
        self.label_7.setObjectName(u"label_7")

        self.formLayout_6.setWidget(1, QFormLayout.LabelRole, self.label_7)

        self.comboBox_C3 = ComboBox(self.l_widget1_3)
        self.comboBox_C3.setObjectName(u"comboBox_C3")

        self.formLayout_6.setWidget(1, QFormLayout.FieldRole, self.comboBox_C3)


        self.horizontalLayout_8.addLayout(self.formLayout_6)

        self.LH_Button_3 = PushButton(self.l_widget1_3)
        self.LH_Button_3.setObjectName(u"LH_Button_3")

        self.horizontalLayout_8.addWidget(self.LH_Button_3)

        self.horizontalLayout_8.setStretch(0, 1)
        self.horizontalLayout_8.setStretch(1, 2)
        self.horizontalLayout_8.setStretch(2, 2)
        self.horizontalLayout_8.setStretch(3, 2)
        self.horizontalLayout_8.setStretch(4, 1)

        self.verticalLayout_2.addLayout(self.horizontalLayout_8)

        self.widget_7 = QWidget(self.l_widget1_3)
        self.widget_7.setObjectName(u"widget_7")

        self.verticalLayout_2.addWidget(self.widget_7)

        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 10)

        self.gridLayout.addWidget(self.l_widget1_3, 1, 0, 1, 1)

        self.L_widget1 = QWidget(self.left_widget)
        self.L_widget1.setObjectName(u"L_widget1")
        self.verticalLayout_3 = QVBoxLayout(self.L_widget1)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)

        self.LH_label = label.PixmapLabel(self.L_widget1)
        self.LH_label.setObjectName(u"LH_label")

        self.horizontalLayout_6.addWidget(self.LH_label)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.LH_labelY = QLabel(self.L_widget1)
        self.LH_labelY.setObjectName(u"LH_labelY")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.LH_labelY)

        self.LH_ComboBox_1Y = ComboBox(self.L_widget1)
        self.LH_ComboBox_1Y.setObjectName(u"LH_ComboBox_1Y")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.LH_ComboBox_1Y)

        self.LH_labelX = QLabel(self.L_widget1)
        self.LH_labelX.setObjectName(u"LH_labelX")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.LH_labelX)

        self.LH_ComboBox_1X = ComboBox(self.L_widget1)
        self.LH_ComboBox_1X.setObjectName(u"LH_ComboBox_1X")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.LH_ComboBox_1X)

        self.LH_labelL = QLabel(self.L_widget1)
        self.LH_labelL.setObjectName(u"LH_labelL")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.LH_labelL)

        self.LH_ComboBox_1L = ComboBox(self.L_widget1)
        self.LH_ComboBox_1L.setObjectName(u"LH_ComboBox_1L")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.LH_ComboBox_1L)


        self.horizontalLayout_6.addLayout(self.formLayout)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setFormAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_3 = QLabel(self.L_widget1)
        self.label_3.setObjectName(u"label_3")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_3)

        self.LH_ComboBox_1 = ComboBox(self.L_widget1)
        self.LH_ComboBox_1.setObjectName(u"LH_ComboBox_1")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.LH_ComboBox_1)

        self.label_4 = QLabel(self.L_widget1)
        self.label_4.setObjectName(u"label_4")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_4)

        self.comboBox_C1 = ComboBox(self.L_widget1)
        self.comboBox_C1.setObjectName(u"comboBox_C1")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.comboBox_C1)


        self.horizontalLayout_6.addLayout(self.formLayout_2)

        self.LH_Button = PushButton(self.L_widget1)
        self.LH_Button.setObjectName(u"LH_Button")

        self.horizontalLayout_6.addWidget(self.LH_Button)

        self.horizontalLayout_6.setStretch(0, 1)
        self.horizontalLayout_6.setStretch(1, 2)
        self.horizontalLayout_6.setStretch(2, 2)
        self.horizontalLayout_6.setStretch(3, 2)
        self.horizontalLayout_6.setStretch(4, 1)

        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.widget_5 = QWidget(self.L_widget1)
        self.widget_5.setObjectName(u"widget_5")

        self.verticalLayout_3.addWidget(self.widget_5)

        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 10)

        self.gridLayout.addWidget(self.L_widget1, 0, 0, 1, 1)

        self.l_widget1_2 = QWidget(self.left_widget)
        self.l_widget1_2.setObjectName(u"l_widget1_2")
        self.verticalLayout_6 = QVBoxLayout(self.l_widget1_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_2)

        self.LH_label_2 = label.PixmapLabel(self.l_widget1_2)
        self.LH_label_2.setObjectName(u"LH_label_2")

        self.horizontalLayout_7.addWidget(self.LH_label_2)

        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.LH_labelY_2 = QLabel(self.l_widget1_2)
        self.LH_labelY_2.setObjectName(u"LH_labelY_2")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.LH_labelY_2)

        self.LH_ComboBox_2Y = ComboBox(self.l_widget1_2)
        self.LH_ComboBox_2Y.setObjectName(u"LH_ComboBox_2Y")

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.LH_ComboBox_2Y)

        self.LH_labelX_2 = QLabel(self.l_widget1_2)
        self.LH_labelX_2.setObjectName(u"LH_labelX_2")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.LH_labelX_2)

        self.LH_ComboBox_2X = ComboBox(self.l_widget1_2)
        self.LH_ComboBox_2X.setObjectName(u"LH_ComboBox_2X")

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.LH_ComboBox_2X)

        self.LH_labelL_2 = QLabel(self.l_widget1_2)
        self.LH_labelL_2.setObjectName(u"LH_labelL_2")

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.LH_labelL_2)

        self.LH_ComboBox_2L = ComboBox(self.l_widget1_2)
        self.LH_ComboBox_2L.setObjectName(u"LH_ComboBox_2L")

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.LH_ComboBox_2L)


        self.horizontalLayout_7.addLayout(self.formLayout_3)

        self.formLayout_4 = QFormLayout()
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.formLayout_4.setFormAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_5 = QLabel(self.l_widget1_2)
        self.label_5.setObjectName(u"label_5")

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.label_5)

        self.LH_ComboBox_2 = ComboBox(self.l_widget1_2)
        self.LH_ComboBox_2.setObjectName(u"LH_ComboBox_2")

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.LH_ComboBox_2)

        self.label_6 = QLabel(self.l_widget1_2)
        self.label_6.setObjectName(u"label_6")

        self.formLayout_4.setWidget(1, QFormLayout.LabelRole, self.label_6)

        self.comboBox_C2 = ComboBox(self.l_widget1_2)
        self.comboBox_C2.setObjectName(u"comboBox_C2")

        self.formLayout_4.setWidget(1, QFormLayout.FieldRole, self.comboBox_C2)


        self.horizontalLayout_7.addLayout(self.formLayout_4)

        self.LH_Button_2 = PushButton(self.l_widget1_2)
        self.LH_Button_2.setObjectName(u"LH_Button_2")

        self.horizontalLayout_7.addWidget(self.LH_Button_2)

        self.horizontalLayout_7.setStretch(0, 1)
        self.horizontalLayout_7.setStretch(1, 2)
        self.horizontalLayout_7.setStretch(2, 2)
        self.horizontalLayout_7.setStretch(3, 2)
        self.horizontalLayout_7.setStretch(4, 1)

        self.verticalLayout_6.addLayout(self.horizontalLayout_7)

        self.widget_6 = QWidget(self.l_widget1_2)
        self.widget_6.setObjectName(u"widget_6")

        self.verticalLayout_6.addWidget(self.widget_6)

        self.verticalLayout_6.setStretch(0, 1)
        self.verticalLayout_6.setStretch(1, 10)

        self.gridLayout.addWidget(self.l_widget1_2, 0, 1, 1, 1)


        self.horizontalLayout.addWidget(self.left_widget)

        self.groupBox = QGroupBox(self.tab_8)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.widget_2 = QWidget(self.groupBox)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_10 = QVBoxLayout(self.widget_2)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.comboBox = ComboBox(self.widget_2)
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout_2.addWidget(self.comboBox)

        self.pushButton = PushButton(self.widget_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_2.addWidget(self.pushButton)


        self.verticalLayout_10.addLayout(self.horizontalLayout_2)

        self.scrollArea = QScrollArea(self.widget_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMinimumSize(QSize(50, 100))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 143, 239))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_10.addWidget(self.scrollArea)

        self.verticalLayout_10.setStretch(0, 1)
        self.verticalLayout_10.setStretch(1, 10)

        self.gridLayout_2.addWidget(self.widget_2, 0, 0, 1, 1)

        self.widget_17 = QWidget(self.groupBox)
        self.widget_17.setObjectName(u"widget_17")
        self.verticalLayout_13 = QVBoxLayout(self.widget_17)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.comboBox_4 = ComboBox(self.widget_17)
        self.comboBox_4.setObjectName(u"comboBox_4")

        self.horizontalLayout_5.addWidget(self.comboBox_4)

        self.pushButton_4 = PushButton(self.widget_17)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_5.addWidget(self.pushButton_4)

        self.horizontalLayout_5.setStretch(0, 4)
        self.horizontalLayout_5.setStretch(1, 1)

        self.verticalLayout_13.addLayout(self.horizontalLayout_5)

        self.scrollArea_4 = QScrollArea(self.widget_17)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 143, 238))
        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)

        self.verticalLayout_13.addWidget(self.scrollArea_4)

        self.verticalLayout_13.setStretch(0, 1)
        self.verticalLayout_13.setStretch(1, 10)

        self.gridLayout_2.addWidget(self.widget_17, 1, 1, 1, 1)

        self.widget_15 = QWidget(self.groupBox)
        self.widget_15.setObjectName(u"widget_15")
        self.verticalLayout_12 = QVBoxLayout(self.widget_15)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.comboBox_3 = ComboBox(self.widget_15)
        self.comboBox_3.setObjectName(u"comboBox_3")

        self.horizontalLayout_4.addWidget(self.comboBox_3)

        self.pushButton_3 = PushButton(self.widget_15)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_4.addWidget(self.pushButton_3)

        self.horizontalLayout_4.setStretch(0, 4)
        self.horizontalLayout_4.setStretch(1, 1)

        self.verticalLayout_12.addLayout(self.horizontalLayout_4)

        self.scrollArea_3 = QScrollArea(self.widget_15)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 143, 238))
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_12.addWidget(self.scrollArea_3)

        self.verticalLayout_12.setStretch(0, 1)
        self.verticalLayout_12.setStretch(1, 10)

        self.gridLayout_2.addWidget(self.widget_15, 1, 0, 1, 1)

        self.widget_3 = QWidget(self.groupBox)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_14 = QVBoxLayout(self.widget_3)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.comboBox_5 = ComboBox(self.widget_3)
        self.comboBox_5.setObjectName(u"comboBox_5")

        self.horizontalLayout_10.addWidget(self.comboBox_5)

        self.pushButton_5 = PushButton(self.widget_3)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_10.addWidget(self.pushButton_5)

        self.horizontalLayout_10.setStretch(0, 4)

        self.verticalLayout_14.addLayout(self.horizontalLayout_10)

        self.scrollArea_5 = QScrollArea(self.widget_3)
        self.scrollArea_5.setObjectName(u"scrollArea_5")
        self.scrollArea_5.setMinimumSize(QSize(50, 100))
        self.scrollArea_5.setWidgetResizable(True)
        self.scrollAreaWidgetContents_5 = QWidget()
        self.scrollAreaWidgetContents_5.setObjectName(u"scrollAreaWidgetContents_5")
        self.scrollAreaWidgetContents_5.setGeometry(QRect(0, 0, 143, 239))
        self.scrollArea_5.setWidget(self.scrollAreaWidgetContents_5)

        self.verticalLayout_14.addWidget(self.scrollArea_5)

        self.verticalLayout_14.setStretch(0, 1)
        self.verticalLayout_14.setStretch(1, 10)

        self.gridLayout_2.addWidget(self.widget_3, 2, 0, 1, 1)

        self.widget_16 = QWidget(self.groupBox)
        self.widget_16.setObjectName(u"widget_16")
        self.verticalLayout_15 = QVBoxLayout(self.widget_16)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.comboBox_6 = ComboBox(self.widget_16)
        self.comboBox_6.setObjectName(u"comboBox_6")

        self.horizontalLayout_11.addWidget(self.comboBox_6)

        self.pushButton_6 = PushButton(self.widget_16)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_11.addWidget(self.pushButton_6)

        self.horizontalLayout_11.setStretch(0, 4)
        self.horizontalLayout_11.setStretch(1, 1)

        self.verticalLayout_15.addLayout(self.horizontalLayout_11)

        self.scrollArea_6 = QScrollArea(self.widget_16)
        self.scrollArea_6.setObjectName(u"scrollArea_6")
        self.scrollArea_6.setWidgetResizable(True)
        self.scrollAreaWidgetContents_6 = QWidget()
        self.scrollAreaWidgetContents_6.setObjectName(u"scrollAreaWidgetContents_6")
        self.scrollAreaWidgetContents_6.setGeometry(QRect(0, 0, 143, 239))
        self.scrollArea_6.setWidget(self.scrollAreaWidgetContents_6)

        self.verticalLayout_15.addWidget(self.scrollArea_6)

        self.verticalLayout_15.setStretch(0, 1)
        self.verticalLayout_15.setStretch(1, 10)

        self.gridLayout_2.addWidget(self.widget_16, 2, 1, 1, 1)

        self.widget_13 = QWidget(self.groupBox)
        self.widget_13.setObjectName(u"widget_13")
        self.verticalLayout_11 = QVBoxLayout(self.widget_13)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.comboBox_2 = ComboBox(self.widget_13)
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.horizontalLayout_3.addWidget(self.comboBox_2)

        self.pushButton_2 = PushButton(self.widget_13)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_3.addWidget(self.pushButton_2)

        self.horizontalLayout_3.setStretch(0, 4)
        self.horizontalLayout_3.setStretch(1, 1)

        self.verticalLayout_11.addLayout(self.horizontalLayout_3)

        self.scrollArea_2 = QScrollArea(self.widget_13)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 143, 239))
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_11.addWidget(self.scrollArea_2)

        self.verticalLayout_11.setStretch(0, 1)
        self.verticalLayout_11.setStretch(1, 10)

        self.gridLayout_2.addWidget(self.widget_13, 0, 1, 1, 1)


        self.horizontalLayout.addWidget(self.groupBox)

        self.horizontalLayout.setStretch(0, 4)
        self.horizontalLayout.setStretch(1, 1)

        self.gridLayout_7.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.tabWidget.addTab(self.tab_8, "")

        self.verticalLayout_5.addWidget(self.tabWidget)


        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u6570\u636e\u6e90", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"TextLabel\u6570\u636e\u4e3a\u7528\" t\"\u5206\u9694\u7684\u683c\u5f0f(\u53ef\u76f4\u63a5\u590d\u5236excel\u5728\u4efb\u610f\u6587\u4ef6\uff0c\u518d\u590d\u5236\u81f3\u6b64\u754c\u9762\uff09", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), QCoreApplication.translate("Form", u"\u6570\u636e\u6e90", None))
        self.Title.setText(QCoreApplication.translate("Form", u"\u6570\u636e\u770b\u677f", None))
        self.Title_littel.setText(QCoreApplication.translate("Form", u"\u57fa\u4e8e2014-2023\u5e74\u5168\u56fd\u9500\u552e\u6570\u636e\u62a5", None))
        self.LH_label_4.setText(QCoreApplication.translate("Form", u"\u56fe\u88684", None))
        self.LH_labelY_4.setText(QCoreApplication.translate("Form", u"\u7eb5\u8f74", None))
        self.LH_labelX_4.setText(QCoreApplication.translate("Form", u"\u6a2a\u8f74", None))
        self.LH_labelL_4.setText(QCoreApplication.translate("Form", u"\u6807\u7b7e", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"\u7c7b\u578b", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"\u989c\u8272", None))
        self.LH_Button_4.setText(QCoreApplication.translate("Form", u"\u786e\u5b9a", None))
        self.LH_label_3.setText(QCoreApplication.translate("Form", u"\u56fe\u88683", None))
        self.LH_labelY_3.setText(QCoreApplication.translate("Form", u"\u7eb5\u8f74", None))
        self.LH_labelX_3.setText(QCoreApplication.translate("Form", u"\u6a2a\u8f74", None))
        self.LH_labelL_3.setText(QCoreApplication.translate("Form", u"\u6807\u7b7e", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"\u7c7b\u578b", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"\u989c\u8272", None))
        self.LH_Button_3.setText(QCoreApplication.translate("Form", u"\u786e\u5b9a", None))
        self.LH_label.setText(QCoreApplication.translate("Form", u"\u56fe\u88681", None))
        self.LH_labelY.setText(QCoreApplication.translate("Form", u"\u7eb5\u8f74", None))
        self.LH_labelX.setText(QCoreApplication.translate("Form", u"\u6a2a\u8f74", None))
        self.LH_labelL.setText(QCoreApplication.translate("Form", u"\u6807\u7b7e", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u7c7b\u578b", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u989c\u8272", None))
        self.LH_Button.setText(QCoreApplication.translate("Form", u"\u786e\u5b9a", None))
        self.LH_label_2.setText(QCoreApplication.translate("Form", u"\u56fe\u88682", None))
        self.LH_labelY_2.setText(QCoreApplication.translate("Form", u"\u7eb5\u8f74", None))
        self.LH_labelX_2.setText(QCoreApplication.translate("Form", u"\u6a2a\u8f74", None))
        self.LH_labelL_2.setText(QCoreApplication.translate("Form", u"\u6807\u7b7e", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u7c7b\u578b", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"\u989c\u8272", None))
        self.LH_Button_2.setText(QCoreApplication.translate("Form", u"\u786e\u5b9a", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"GroupBox", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"OK", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"OK", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"OK", None))
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"OK", None))
        self.pushButton_6.setText(QCoreApplication.translate("Form", u"OK", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"OK", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_8), QCoreApplication.translate("Form", u"\u56fe\u8868", None))
    # retranslateUi

