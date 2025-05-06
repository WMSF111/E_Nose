# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Form4.ui'
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
from qfluentwidgets import LineEdit
from qfluentwidgets import TogglePushButton


class Ui_Board1(object):
    def setupUi(self, Board1):
        if not Board1.objectName():
            Board1.setObjectName(u"Board1")
        Board1.resize(1709, 1115)
        self.verticalLayout_5 = QVBoxLayout(Board1)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.serial_widget = QWidget(Board1)
        self.serial_widget.setObjectName(u"serial_widget")
        self.horizontalLayout_12 = QHBoxLayout(self.serial_widget)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_ser_info = QLabel(self.serial_widget)
        self.label_ser_info.setObjectName(u"label_ser_info")
        font = QFont()
        font.setPointSize(10)
        self.label_ser_info.setFont(font)

        self.horizontalLayout_13.addWidget(self.label_ser_info)

        self.comboBox_ser_select = ComboBox(self.serial_widget)
        self.comboBox_ser_select.setObjectName(u"comboBox_ser_select")
        self.comboBox_ser_select.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_13.addWidget(self.comboBox_ser_select)


        self.horizontalLayout_12.addLayout(self.horizontalLayout_13)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_5)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_2 = QLabel(self.serial_widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 0))
        self.label_2.setMaximumSize(QSize(110, 16777215))
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_14.addWidget(self.label_2)

        self.lineEdit_baud = LineEdit(self.serial_widget)
        self.lineEdit_baud.setObjectName(u"lineEdit_baud")

        self.horizontalLayout_14.addWidget(self.lineEdit_baud)


        self.horizontalLayout_12.addLayout(self.horizontalLayout_14)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_6)

        self.pushButton_ser_open = TogglePushButton(self.serial_widget)
        self.pushButton_ser_open.setObjectName(u"pushButton_ser_open")

        self.horizontalLayout_12.addWidget(self.pushButton_ser_open)

        self.horizontalLayout_12.setStretch(0, 5)
        self.horizontalLayout_12.setStretch(1, 1)
        self.horizontalLayout_12.setStretch(2, 5)
        self.horizontalLayout_12.setStretch(3, 1)
        self.horizontalLayout_12.setStretch(4, 2)

        self.verticalLayout_5.addWidget(self.serial_widget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.left_widget = QWidget(Board1)
        self.left_widget.setObjectName(u"left_widget")
        self.gridLayout = QGridLayout(self.left_widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.L_widget1 = QWidget(self.left_widget)
        self.L_widget1.setObjectName(u"L_widget1")
        self.verticalLayout_2 = QVBoxLayout(self.L_widget1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)

        self.LH_label = QLabel(self.L_widget1)
        self.LH_label.setObjectName(u"LH_label")

        self.horizontalLayout_6.addWidget(self.LH_label)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.LH_labelY = QLabel(self.L_widget1)
        self.LH_labelY.setObjectName(u"LH_labelY")

        self.horizontalLayout_2.addWidget(self.LH_labelY)

        self.LH_ComboBox_1Y = ComboBox(self.L_widget1)
        self.LH_ComboBox_1Y.setObjectName(u"LH_ComboBox_1Y")
        self.LH_ComboBox_1Y.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_2.addWidget(self.LH_ComboBox_1Y)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 3)

        self.horizontalLayout_6.addLayout(self.horizontalLayout_2)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setFormAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_4 = QLabel(self.L_widget1)
        self.label_4.setObjectName(u"label_4")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_4)

        self.comboBox_C1 = ComboBox(self.L_widget1)
        self.comboBox_C1.setObjectName(u"comboBox_C1")
        self.comboBox_C1.setMaximumSize(QSize(16777215, 30))

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.comboBox_C1)


        self.horizontalLayout_6.addLayout(self.formLayout_2)

        self.LH_Button = PushButton(self.L_widget1)
        self.LH_Button.setObjectName(u"LH_Button")

        self.horizontalLayout_6.addWidget(self.LH_Button)

        self.horizontalLayout_6.setStretch(0, 1)
        self.horizontalLayout_6.setStretch(1, 2)
        self.horizontalLayout_6.setStretch(2, 2)
        self.horizontalLayout_6.setStretch(3, 2)
        self.horizontalLayout_6.setStretch(4, 1)

        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.scrollArea_L1 = QScrollArea(self.L_widget1)
        self.scrollArea_L1.setObjectName(u"scrollArea_L1")
        self.scrollArea_L1.setWidgetResizable(True)
        self.scrollAreaWidgetContents_7 = QWidget()
        self.scrollAreaWidgetContents_7.setObjectName(u"scrollAreaWidgetContents_7")
        self.scrollAreaWidgetContents_7.setGeometry(QRect(0, 0, 672, 461))
        self.scrollArea_L1.setWidget(self.scrollAreaWidgetContents_7)

        self.verticalLayout_2.addWidget(self.scrollArea_L1)


        self.gridLayout.addWidget(self.L_widget1, 1, 0, 1, 1)

        self.l_widget1_4 = QWidget(self.left_widget)
        self.l_widget1_4.setObjectName(u"l_widget1_4")
        self.verticalLayout_6 = QVBoxLayout(self.l_widget1_4)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_4)

        self.LH_label_4 = QLabel(self.l_widget1_4)
        self.LH_label_4.setObjectName(u"LH_label_4")

        self.horizontalLayout_9.addWidget(self.LH_label_4)

        self.formLayout_7 = QFormLayout()
        self.formLayout_7.setObjectName(u"formLayout_7")
        self.LH_labelY_4 = QLabel(self.l_widget1_4)
        self.LH_labelY_4.setObjectName(u"LH_labelY_4")

        self.formLayout_7.setWidget(0, QFormLayout.LabelRole, self.LH_labelY_4)

        self.LH_ComboBox_4Y = ComboBox(self.l_widget1_4)
        self.LH_ComboBox_4Y.setObjectName(u"LH_ComboBox_4Y")
        self.LH_ComboBox_4Y.setMaximumSize(QSize(16777215, 30))

        self.formLayout_7.setWidget(0, QFormLayout.FieldRole, self.LH_ComboBox_4Y)


        self.horizontalLayout_9.addLayout(self.formLayout_7)

        self.formLayout_8 = QFormLayout()
        self.formLayout_8.setObjectName(u"formLayout_8")
        self.formLayout_8.setFormAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_9 = QLabel(self.l_widget1_4)
        self.label_9.setObjectName(u"label_9")

        self.formLayout_8.setWidget(0, QFormLayout.LabelRole, self.label_9)

        self.comboBox_C4 = ComboBox(self.l_widget1_4)
        self.comboBox_C4.setObjectName(u"comboBox_C4")
        self.comboBox_C4.setMaximumSize(QSize(16777215, 30))

        self.formLayout_8.setWidget(0, QFormLayout.FieldRole, self.comboBox_C4)


        self.horizontalLayout_9.addLayout(self.formLayout_8)

        self.LH_Button_4 = PushButton(self.l_widget1_4)
        self.LH_Button_4.setObjectName(u"LH_Button_4")

        self.horizontalLayout_9.addWidget(self.LH_Button_4)

        self.horizontalLayout_9.setStretch(0, 1)
        self.horizontalLayout_9.setStretch(1, 2)
        self.horizontalLayout_9.setStretch(2, 2)
        self.horizontalLayout_9.setStretch(3, 2)
        self.horizontalLayout_9.setStretch(4, 1)

        self.verticalLayout_6.addLayout(self.horizontalLayout_9)

        self.scrollArea_L4 = QScrollArea(self.l_widget1_4)
        self.scrollArea_L4.setObjectName(u"scrollArea_L4")
        self.scrollArea_L4.setWidgetResizable(True)
        self.scrollAreaWidgetContents_10 = QWidget()
        self.scrollAreaWidgetContents_10.setObjectName(u"scrollAreaWidgetContents_10")
        self.scrollAreaWidgetContents_10.setGeometry(QRect(0, 0, 671, 461))
        self.scrollArea_L4.setWidget(self.scrollAreaWidgetContents_10)

        self.verticalLayout_6.addWidget(self.scrollArea_L4)


        self.gridLayout.addWidget(self.l_widget1_4, 2, 1, 1, 1)

        self.l_widget1_2 = QWidget(self.left_widget)
        self.l_widget1_2.setObjectName(u"l_widget1_2")
        self.verticalLayout_3 = QVBoxLayout(self.l_widget1_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_2)

        self.LH_label_2 = QLabel(self.l_widget1_2)
        self.LH_label_2.setObjectName(u"LH_label_2")

        self.horizontalLayout_7.addWidget(self.LH_label_2)

        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.LH_labelY_2 = QLabel(self.l_widget1_2)
        self.LH_labelY_2.setObjectName(u"LH_labelY_2")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.LH_labelY_2)

        self.LH_ComboBox_2Y = ComboBox(self.l_widget1_2)
        self.LH_ComboBox_2Y.setObjectName(u"LH_ComboBox_2Y")
        self.LH_ComboBox_2Y.setMaximumSize(QSize(16777215, 30))

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.LH_ComboBox_2Y)


        self.horizontalLayout_7.addLayout(self.formLayout_3)

        self.formLayout_4 = QFormLayout()
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.formLayout_4.setFormAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_5 = QLabel(self.l_widget1_2)
        self.label_5.setObjectName(u"label_5")

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.label_5)

        self.LH_ComboBox_2 = ComboBox(self.l_widget1_2)
        self.LH_ComboBox_2.setObjectName(u"LH_ComboBox_2")
        self.LH_ComboBox_2.setMaximumSize(QSize(16777215, 30))

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.LH_ComboBox_2)


        self.horizontalLayout_7.addLayout(self.formLayout_4)

        self.LH_Button_2 = PushButton(self.l_widget1_2)
        self.LH_Button_2.setObjectName(u"LH_Button_2")

        self.horizontalLayout_7.addWidget(self.LH_Button_2)

        self.horizontalLayout_7.setStretch(0, 1)
        self.horizontalLayout_7.setStretch(1, 2)
        self.horizontalLayout_7.setStretch(2, 2)
        self.horizontalLayout_7.setStretch(3, 2)
        self.horizontalLayout_7.setStretch(4, 1)

        self.verticalLayout_3.addLayout(self.horizontalLayout_7)

        self.scrollArea_L2 = QScrollArea(self.l_widget1_2)
        self.scrollArea_L2.setObjectName(u"scrollArea_L2")
        self.scrollArea_L2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_8 = QWidget()
        self.scrollAreaWidgetContents_8.setObjectName(u"scrollAreaWidgetContents_8")
        self.scrollAreaWidgetContents_8.setGeometry(QRect(0, 0, 671, 461))
        self.scrollArea_L2.setWidget(self.scrollAreaWidgetContents_8)

        self.verticalLayout_3.addWidget(self.scrollArea_L2)


        self.gridLayout.addWidget(self.l_widget1_2, 1, 1, 1, 1)

        self.l_widget1_3 = QWidget(self.left_widget)
        self.l_widget1_3.setObjectName(u"l_widget1_3")
        self.verticalLayout_4 = QVBoxLayout(self.l_widget1_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_3)

        self.LH_label_3 = QLabel(self.l_widget1_3)
        self.LH_label_3.setObjectName(u"LH_label_3")

        self.horizontalLayout_8.addWidget(self.LH_label_3)

        self.formLayout_5 = QFormLayout()
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.LH_labelY_3 = QLabel(self.l_widget1_3)
        self.LH_labelY_3.setObjectName(u"LH_labelY_3")

        self.formLayout_5.setWidget(0, QFormLayout.LabelRole, self.LH_labelY_3)

        self.LH_ComboBox_3Y = ComboBox(self.l_widget1_3)
        self.LH_ComboBox_3Y.setObjectName(u"LH_ComboBox_3Y")
        self.LH_ComboBox_3Y.setMaximumSize(QSize(16777215, 30))

        self.formLayout_5.setWidget(0, QFormLayout.FieldRole, self.LH_ComboBox_3Y)


        self.horizontalLayout_8.addLayout(self.formLayout_5)

        self.formLayout_6 = QFormLayout()
        self.formLayout_6.setObjectName(u"formLayout_6")
        self.formLayout_6.setFormAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_7 = QLabel(self.l_widget1_3)
        self.label_7.setObjectName(u"label_7")

        self.formLayout_6.setWidget(0, QFormLayout.LabelRole, self.label_7)

        self.comboBox_C3 = ComboBox(self.l_widget1_3)
        self.comboBox_C3.setObjectName(u"comboBox_C3")
        self.comboBox_C3.setMaximumSize(QSize(16777215, 30))

        self.formLayout_6.setWidget(0, QFormLayout.FieldRole, self.comboBox_C3)


        self.horizontalLayout_8.addLayout(self.formLayout_6)

        self.LH_Button_3 = PushButton(self.l_widget1_3)
        self.LH_Button_3.setObjectName(u"LH_Button_3")

        self.horizontalLayout_8.addWidget(self.LH_Button_3)

        self.horizontalLayout_8.setStretch(0, 1)
        self.horizontalLayout_8.setStretch(1, 2)
        self.horizontalLayout_8.setStretch(2, 2)
        self.horizontalLayout_8.setStretch(3, 2)
        self.horizontalLayout_8.setStretch(4, 1)

        self.verticalLayout_4.addLayout(self.horizontalLayout_8)

        self.scrollArea_L3 = QScrollArea(self.l_widget1_3)
        self.scrollArea_L3.setObjectName(u"scrollArea_L3")
        self.scrollArea_L3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_9 = QWidget()
        self.scrollAreaWidgetContents_9.setObjectName(u"scrollAreaWidgetContents_9")
        self.scrollAreaWidgetContents_9.setGeometry(QRect(0, 0, 672, 461))
        self.scrollArea_L3.setWidget(self.scrollAreaWidgetContents_9)

        self.verticalLayout_4.addWidget(self.scrollArea_L3)


        self.gridLayout.addWidget(self.l_widget1_3, 2, 0, 1, 1)


        self.horizontalLayout.addWidget(self.left_widget)

        self.groupBox = QGroupBox(Board1)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.textBrowser = QTextBrowser(self.groupBox)
        self.textBrowser.setObjectName(u"textBrowser")

        self.gridLayout_2.addWidget(self.textBrowser, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.groupBox)

        self.horizontalLayout.setStretch(0, 4)

        self.verticalLayout_5.addLayout(self.horizontalLayout)


        self.retranslateUi(Board1)

        QMetaObject.connectSlotsByName(Board1)
    # setupUi

    def retranslateUi(self, Board1):
        Board1.setWindowTitle(QCoreApplication.translate("Board1", u"Form", None))
        self.label_ser_info.setText(QCoreApplication.translate("Board1", u"\u4e32\u53e3\u4fe1\u606f", None))
        self.label_2.setText(QCoreApplication.translate("Board1", u"\u6ce2\u7279\u7387", None))
        self.lineEdit_baud.setText(QCoreApplication.translate("Board1", u"115200", None))
        self.pushButton_ser_open.setText(QCoreApplication.translate("Board1", u"\u6253\u5f00\u4e32\u53e3", None))
        self.LH_label.setText(QCoreApplication.translate("Board1", u"\u56fe\u88681", None))
        self.LH_labelY.setText(QCoreApplication.translate("Board1", u"\u7eb5\u8f74", None))
        self.label_4.setText(QCoreApplication.translate("Board1", u"\u989c\u8272", None))
        self.LH_Button.setText(QCoreApplication.translate("Board1", u"\u786e\u5b9a", None))
        self.LH_label_4.setText(QCoreApplication.translate("Board1", u"\u56fe\u88684", None))
        self.LH_labelY_4.setText(QCoreApplication.translate("Board1", u"\u7eb5\u8f74", None))
        self.label_9.setText(QCoreApplication.translate("Board1", u"\u989c\u8272", None))
        self.LH_Button_4.setText(QCoreApplication.translate("Board1", u"\u786e\u5b9a", None))
        self.LH_label_2.setText(QCoreApplication.translate("Board1", u"\u56fe\u88682", None))
        self.LH_labelY_2.setText(QCoreApplication.translate("Board1", u"\u7eb5\u8f74", None))
        self.label_5.setText(QCoreApplication.translate("Board1", u"\u7c7b\u578b", None))
        self.LH_Button_2.setText(QCoreApplication.translate("Board1", u"\u786e\u5b9a", None))
        self.LH_label_3.setText(QCoreApplication.translate("Board1", u"\u56fe\u88683", None))
        self.LH_labelY_3.setText(QCoreApplication.translate("Board1", u"\u7eb5\u8f74", None))
        self.label_7.setText(QCoreApplication.translate("Board1", u"\u989c\u8272", None))
        self.LH_Button_3.setText(QCoreApplication.translate("Board1", u"\u786e\u5b9a", None))
        self.groupBox.setTitle(QCoreApplication.translate("Board1", u"\u6570\u636e\u6e90\u7b5b\u9009\u533a", None))
    # retranslateUi

