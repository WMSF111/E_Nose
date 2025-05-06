# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Form3.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from resource.mycombobox import MyComboBox


class Ui_Board3(object):
    def setupUi(self, Board):
        if not Board.objectName():
            Board.setObjectName(u"Board")
        Board.resize(1257, 782)
        self.verticalLayout_17 = QVBoxLayout(Board)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.serial_widget = QWidget(Board)
        self.serial_widget.setObjectName(u"serial_widget")
        self.horizontalLayout_3 = QHBoxLayout(self.serial_widget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_ser_info = QLabel(self.serial_widget)
        self.label_ser_info.setObjectName(u"label_ser_info")
        font = QFont()
        font.setPointSize(10)
        self.label_ser_info.setFont(font)

        self.horizontalLayout.addWidget(self.label_ser_info)

        self.comboBox_ser_select_2 = MyComboBox(self.serial_widget)
        self.comboBox_ser_select_2.setObjectName(u"comboBox_ser_select_2")
        self.comboBox_ser_select_2.setMinimumSize(QSize(0, 0))
        self.comboBox_ser_select_2.setEditable(False)

        self.horizontalLayout.addWidget(self.comboBox_ser_select_2)


        self.horizontalLayout_3.addLayout(self.horizontalLayout)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.serial_widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 0))
        self.label_2.setMaximumSize(QSize(110, 16777215))
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.lineEdit_baud = QLineEdit(self.serial_widget)
        self.lineEdit_baud.setObjectName(u"lineEdit_baud")

        self.horizontalLayout_2.addWidget(self.lineEdit_baud)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.pushButton_ser_open = QPushButton(self.serial_widget)
        self.pushButton_ser_open.setObjectName(u"pushButton_ser_open")

        self.horizontalLayout_3.addWidget(self.pushButton_ser_open)

        self.horizontalLayout_3.setStretch(0, 5)
        self.horizontalLayout_3.setStretch(1, 1)
        self.horizontalLayout_3.setStretch(2, 5)
        self.horizontalLayout_3.setStretch(3, 1)
        self.horizontalLayout_3.setStretch(4, 2)

        self.verticalLayout_17.addWidget(self.serial_widget)

        self.left_widget = QWidget(Board)
        self.left_widget.setObjectName(u"left_widget")
        self.gridLayout_2 = QGridLayout(self.left_widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.L_widget9_2 = QWidget(self.left_widget)
        self.L_widget9_2.setObjectName(u"L_widget9_2")
        self.verticalLayout_30 = QVBoxLayout(self.L_widget9_2)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.LH_label9_2 = QLabel(self.L_widget9_2)
        self.LH_label9_2.setObjectName(u"LH_label9_2")

        self.verticalLayout_30.addWidget(self.LH_label9_2)

        self.scrollArea_26 = QScrollArea(self.L_widget9_2)
        self.scrollArea_26.setObjectName(u"scrollArea_26")
        self.scrollArea_26.setWidgetResizable(True)
        self.scrollAreaWidgetContents_36 = QWidget()
        self.scrollAreaWidgetContents_36.setObjectName(u"scrollAreaWidgetContents_36")
        self.scrollAreaWidgetContents_36.setGeometry(QRect(0, 0, 281, 132))
        self.scrollArea_26.setWidget(self.scrollAreaWidgetContents_36)

        self.verticalLayout_30.addWidget(self.scrollArea_26)


        self.gridLayout_2.addWidget(self.L_widget9_2, 2, 0, 1, 1)

        self.L_widget14_2 = QWidget(self.left_widget)
        self.L_widget14_2.setObjectName(u"L_widget14_2")
        self.verticalLayout_49 = QVBoxLayout(self.L_widget14_2)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.LH_label14_2 = QLabel(self.L_widget14_2)
        self.LH_label14_2.setObjectName(u"LH_label14_2")

        self.verticalLayout_49.addWidget(self.LH_label14_2)

        self.scrollArea_32 = QScrollArea(self.L_widget14_2)
        self.scrollArea_32.setObjectName(u"scrollArea_32")
        self.scrollArea_32.setWidgetResizable(True)
        self.scrollAreaWidgetContents_55 = QWidget()
        self.scrollAreaWidgetContents_55.setObjectName(u"scrollAreaWidgetContents_55")
        self.scrollAreaWidgetContents_55.setGeometry(QRect(0, 0, 281, 132))
        self.scrollArea_32.setWidget(self.scrollAreaWidgetContents_55)

        self.verticalLayout_49.addWidget(self.scrollArea_32)


        self.gridLayout_2.addWidget(self.L_widget14_2, 3, 1, 1, 1)

        self.L_widge15_2 = QWidget(self.left_widget)
        self.L_widge15_2.setObjectName(u"L_widge15_2")
        self.verticalLayout_47 = QVBoxLayout(self.L_widge15_2)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.LH_label15_2 = QLabel(self.L_widge15_2)
        self.LH_label15_2.setObjectName(u"LH_label15_2")

        self.verticalLayout_47.addWidget(self.LH_label15_2)

        self.scrollArea_25 = QScrollArea(self.L_widge15_2)
        self.scrollArea_25.setObjectName(u"scrollArea_25")
        self.scrollArea_25.setWidgetResizable(True)
        self.scrollAreaWidgetContents_53 = QWidget()
        self.scrollAreaWidgetContents_53.setObjectName(u"scrollAreaWidgetContents_53")
        self.scrollAreaWidgetContents_53.setGeometry(QRect(0, 0, 280, 132))
        self.scrollArea_25.setWidget(self.scrollAreaWidgetContents_53)

        self.verticalLayout_47.addWidget(self.scrollArea_25)


        self.gridLayout_2.addWidget(self.L_widge15_2, 3, 2, 1, 1)

        self.L_widget16_2 = QWidget(self.left_widget)
        self.L_widget16_2.setObjectName(u"L_widget16_2")
        self.verticalLayout_48 = QVBoxLayout(self.L_widget16_2)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.LH_label16_2 = QLabel(self.L_widget16_2)
        self.LH_label16_2.setObjectName(u"LH_label16_2")

        self.verticalLayout_48.addWidget(self.LH_label16_2)

        self.scrollArea_28 = QScrollArea(self.L_widget16_2)
        self.scrollArea_28.setObjectName(u"scrollArea_28")
        self.scrollArea_28.setWidgetResizable(True)
        self.scrollAreaWidgetContents_54 = QWidget()
        self.scrollAreaWidgetContents_54.setObjectName(u"scrollAreaWidgetContents_54")
        self.scrollAreaWidgetContents_54.setGeometry(QRect(0, 0, 281, 132))
        self.scrollArea_28.setWidget(self.scrollAreaWidgetContents_54)

        self.verticalLayout_48.addWidget(self.scrollArea_28)


        self.gridLayout_2.addWidget(self.L_widget16_2, 3, 3, 1, 1)

        self.L_widget13_2 = QWidget(self.left_widget)
        self.L_widget13_2.setObjectName(u"L_widget13_2")
        self.verticalLayout_28 = QVBoxLayout(self.L_widget13_2)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.LH_label13_2 = QLabel(self.L_widget13_2)
        self.LH_label13_2.setObjectName(u"LH_label13_2")

        self.verticalLayout_28.addWidget(self.LH_label13_2)

        self.scrollArea_18 = QScrollArea(self.L_widget13_2)
        self.scrollArea_18.setObjectName(u"scrollArea_18")
        self.scrollArea_18.setWidgetResizable(True)
        self.scrollAreaWidgetContents_34 = QWidget()
        self.scrollAreaWidgetContents_34.setObjectName(u"scrollAreaWidgetContents_34")
        self.scrollAreaWidgetContents_34.setGeometry(QRect(0, 0, 281, 132))
        self.scrollArea_18.setWidget(self.scrollAreaWidgetContents_34)

        self.verticalLayout_28.addWidget(self.scrollArea_18)


        self.gridLayout_2.addWidget(self.L_widget13_2, 3, 0, 1, 1)

        self.L_widget4_2 = QWidget(self.left_widget)
        self.L_widget4_2.setObjectName(u"L_widget4_2")
        self.verticalLayout_8 = QVBoxLayout(self.L_widget4_2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.LH_label4_2 = QLabel(self.L_widget4_2)
        self.LH_label4_2.setObjectName(u"LH_label4_2")

        self.verticalLayout_8.addWidget(self.LH_label4_2)

        self.scrollArea_20 = QScrollArea(self.L_widget4_2)
        self.scrollArea_20.setObjectName(u"scrollArea_20")
        self.scrollArea_20.setWidgetResizable(True)
        self.scrollAreaWidgetContents_14 = QWidget()
        self.scrollAreaWidgetContents_14.setObjectName(u"scrollAreaWidgetContents_14")
        self.scrollAreaWidgetContents_14.setGeometry(QRect(0, 0, 281, 132))
        self.scrollArea_20.setWidget(self.scrollAreaWidgetContents_14)

        self.verticalLayout_8.addWidget(self.scrollArea_20)


        self.gridLayout_2.addWidget(self.L_widget4_2, 0, 3, 1, 1)

        self.L_widget12_2 = QWidget(self.left_widget)
        self.L_widget12_2.setObjectName(u"L_widget12_2")
        self.verticalLayout_31 = QVBoxLayout(self.L_widget12_2)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.LH_label12_2 = QLabel(self.L_widget12_2)
        self.LH_label12_2.setObjectName(u"LH_label12_2")

        self.verticalLayout_31.addWidget(self.LH_label12_2)

        self.scrollArea_30 = QScrollArea(self.L_widget12_2)
        self.scrollArea_30.setObjectName(u"scrollArea_30")
        self.scrollArea_30.setWidgetResizable(True)
        self.scrollAreaWidgetContents_37 = QWidget()
        self.scrollAreaWidgetContents_37.setObjectName(u"scrollAreaWidgetContents_37")
        self.scrollAreaWidgetContents_37.setGeometry(QRect(0, 0, 281, 132))
        self.scrollArea_30.setWidget(self.scrollAreaWidgetContents_37)

        self.verticalLayout_31.addWidget(self.scrollArea_30)


        self.gridLayout_2.addWidget(self.L_widget12_2, 2, 3, 1, 1)

        self.L_widget1_2 = QWidget(self.left_widget)
        self.L_widget1_2.setObjectName(u"L_widget1_2")
        self.verticalLayout_5 = QVBoxLayout(self.L_widget1_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.LH_label1_2 = QLabel(self.L_widget1_2)
        self.LH_label1_2.setObjectName(u"LH_label1_2")

        self.verticalLayout_5.addWidget(self.LH_label1_2)

        self.scrollArea_17 = QScrollArea(self.L_widget1_2)
        self.scrollArea_17.setObjectName(u"scrollArea_17")
        self.scrollArea_17.setWidgetResizable(True)
        self.scrollAreaWidgetContents_13 = QWidget()
        self.scrollAreaWidgetContents_13.setObjectName(u"scrollAreaWidgetContents_13")
        self.scrollAreaWidgetContents_13.setGeometry(QRect(0, 0, 281, 132))
        self.scrollArea_17.setWidget(self.scrollAreaWidgetContents_13)

        self.verticalLayout_5.addWidget(self.scrollArea_17)


        self.gridLayout_2.addWidget(self.L_widget1_2, 0, 0, 1, 1)

        self.L_widget10_2 = QWidget(self.left_widget)
        self.L_widget10_2.setObjectName(u"L_widget10_2")
        self.verticalLayout_29 = QVBoxLayout(self.L_widget10_2)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.LH_label10_2 = QLabel(self.L_widget10_2)
        self.LH_label10_2.setObjectName(u"LH_label10_2")

        self.verticalLayout_29.addWidget(self.LH_label10_2)

        self.scrollArea_21 = QScrollArea(self.L_widget10_2)
        self.scrollArea_21.setObjectName(u"scrollArea_21")
        self.scrollArea_21.setWidgetResizable(True)
        self.scrollAreaWidgetContents_35 = QWidget()
        self.scrollAreaWidgetContents_35.setObjectName(u"scrollAreaWidgetContents_35")
        self.scrollAreaWidgetContents_35.setGeometry(QRect(0, 0, 281, 132))
        self.scrollArea_21.setWidget(self.scrollAreaWidgetContents_35)

        self.verticalLayout_29.addWidget(self.scrollArea_21)


        self.gridLayout_2.addWidget(self.L_widget10_2, 2, 1, 1, 1)

        self.L_widget6_2 = QWidget(self.left_widget)
        self.L_widget6_2.setObjectName(u"L_widget6_2")
        self.verticalLayout_13 = QVBoxLayout(self.L_widget6_2)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.LH_label6_2 = QLabel(self.L_widget6_2)
        self.LH_label6_2.setObjectName(u"LH_label6_2")

        self.verticalLayout_13.addWidget(self.LH_label6_2)

        self.scrollArea_24 = QScrollArea(self.L_widget6_2)
        self.scrollArea_24.setObjectName(u"scrollArea_24")
        self.scrollArea_24.setWidgetResizable(True)
        self.scrollAreaWidgetContents_19 = QWidget()
        self.scrollAreaWidgetContents_19.setObjectName(u"scrollAreaWidgetContents_19")
        self.scrollAreaWidgetContents_19.setGeometry(QRect(0, 0, 281, 133))
        self.scrollArea_24.setWidget(self.scrollAreaWidgetContents_19)

        self.verticalLayout_13.addWidget(self.scrollArea_24)


        self.gridLayout_2.addWidget(self.L_widget6_2, 1, 1, 1, 1)

        self.L_widget3_2 = QWidget(self.left_widget)
        self.L_widget3_2.setObjectName(u"L_widget3_2")
        self.verticalLayout_11 = QVBoxLayout(self.L_widget3_2)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.LH_label3_2 = QLabel(self.L_widget3_2)
        self.LH_label3_2.setObjectName(u"LH_label3_2")

        self.verticalLayout_11.addWidget(self.LH_label3_2)

        self.scrollArea_22 = QScrollArea(self.L_widget3_2)
        self.scrollArea_22.setObjectName(u"scrollArea_22")
        self.scrollArea_22.setWidgetResizable(True)
        self.scrollAreaWidgetContents_17 = QWidget()
        self.scrollAreaWidgetContents_17.setObjectName(u"scrollAreaWidgetContents_17")
        self.scrollAreaWidgetContents_17.setGeometry(QRect(0, 0, 280, 132))
        self.scrollArea_22.setWidget(self.scrollAreaWidgetContents_17)

        self.verticalLayout_11.addWidget(self.scrollArea_22)


        self.gridLayout_2.addWidget(self.L_widget3_2, 0, 2, 1, 1)

        self.L_widget5_2 = QWidget(self.left_widget)
        self.L_widget5_2.setObjectName(u"L_widget5_2")
        self.verticalLayout_12 = QVBoxLayout(self.L_widget5_2)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.LH_label5_2 = QLabel(self.L_widget5_2)
        self.LH_label5_2.setObjectName(u"LH_label5_2")

        self.verticalLayout_12.addWidget(self.LH_label5_2)

        self.scrollArea_23 = QScrollArea(self.L_widget5_2)
        self.scrollArea_23.setObjectName(u"scrollArea_23")
        self.scrollArea_23.setWidgetResizable(True)
        self.scrollAreaWidgetContents_18 = QWidget()
        self.scrollAreaWidgetContents_18.setObjectName(u"scrollAreaWidgetContents_18")
        self.scrollAreaWidgetContents_18.setGeometry(QRect(0, 0, 281, 133))
        self.scrollArea_23.setWidget(self.scrollAreaWidgetContents_18)

        self.verticalLayout_12.addWidget(self.scrollArea_23)


        self.gridLayout_2.addWidget(self.L_widget5_2, 1, 0, 1, 1)

        self.L_widget11_2 = QWidget(self.left_widget)
        self.L_widget11_2.setObjectName(u"L_widget11_2")
        self.verticalLayout_26 = QVBoxLayout(self.L_widget11_2)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.LH_label11_2 = QLabel(self.L_widget11_2)
        self.LH_label11_2.setObjectName(u"LH_label11_2")

        self.verticalLayout_26.addWidget(self.LH_label11_2)

        self.scrollArea_19 = QScrollArea(self.L_widget11_2)
        self.scrollArea_19.setObjectName(u"scrollArea_19")
        self.scrollArea_19.setWidgetResizable(True)
        self.scrollAreaWidgetContents_32 = QWidget()
        self.scrollAreaWidgetContents_32.setObjectName(u"scrollAreaWidgetContents_32")
        self.scrollAreaWidgetContents_32.setGeometry(QRect(0, 0, 280, 132))
        self.scrollArea_19.setWidget(self.scrollAreaWidgetContents_32)

        self.verticalLayout_26.addWidget(self.scrollArea_19)


        self.gridLayout_2.addWidget(self.L_widget11_2, 2, 2, 1, 1)

        self.L_widget7_2 = QWidget(self.left_widget)
        self.L_widget7_2.setObjectName(u"L_widget7_2")
        self.verticalLayout_14 = QVBoxLayout(self.L_widget7_2)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.LH_label7_2 = QLabel(self.L_widget7_2)
        self.LH_label7_2.setObjectName(u"LH_label7_2")

        self.verticalLayout_14.addWidget(self.LH_label7_2)

        self.scrollArea_27 = QScrollArea(self.L_widget7_2)
        self.scrollArea_27.setObjectName(u"scrollArea_27")
        self.scrollArea_27.setWidgetResizable(True)
        self.scrollAreaWidgetContents_20 = QWidget()
        self.scrollAreaWidgetContents_20.setObjectName(u"scrollAreaWidgetContents_20")
        self.scrollAreaWidgetContents_20.setGeometry(QRect(0, 0, 280, 133))
        self.scrollArea_27.setWidget(self.scrollAreaWidgetContents_20)

        self.verticalLayout_14.addWidget(self.scrollArea_27)


        self.gridLayout_2.addWidget(self.L_widget7_2, 1, 2, 1, 1)

        self.L_widget8_2 = QWidget(self.left_widget)
        self.L_widget8_2.setObjectName(u"L_widget8_2")
        self.verticalLayout_16 = QVBoxLayout(self.L_widget8_2)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.LH_label8_2 = QLabel(self.L_widget8_2)
        self.LH_label8_2.setObjectName(u"LH_label8_2")

        self.verticalLayout_16.addWidget(self.LH_label8_2)

        self.scrollArea_31 = QScrollArea(self.L_widget8_2)
        self.scrollArea_31.setObjectName(u"scrollArea_31")
        self.scrollArea_31.setWidgetResizable(True)
        self.scrollAreaWidgetContents_22 = QWidget()
        self.scrollAreaWidgetContents_22.setObjectName(u"scrollAreaWidgetContents_22")
        self.scrollAreaWidgetContents_22.setGeometry(QRect(0, 0, 281, 133))
        self.scrollArea_31.setWidget(self.scrollAreaWidgetContents_22)

        self.verticalLayout_16.addWidget(self.scrollArea_31)


        self.gridLayout_2.addWidget(self.L_widget8_2, 1, 3, 1, 1)

        self.L_widget2_2 = QWidget(self.left_widget)
        self.L_widget2_2.setObjectName(u"L_widget2_2")
        self.verticalLayout_15 = QVBoxLayout(self.L_widget2_2)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.LH_label2_2 = QLabel(self.L_widget2_2)
        self.LH_label2_2.setObjectName(u"LH_label2_2")

        self.verticalLayout_15.addWidget(self.LH_label2_2)

        self.scrollArea_29 = QScrollArea(self.L_widget2_2)
        self.scrollArea_29.setObjectName(u"scrollArea_29")
        self.scrollArea_29.setWidgetResizable(True)
        self.scrollAreaWidgetContents_21 = QWidget()
        self.scrollAreaWidgetContents_21.setObjectName(u"scrollAreaWidgetContents_21")
        self.scrollAreaWidgetContents_21.setGeometry(QRect(0, 0, 281, 132))
        self.scrollArea_29.setWidget(self.scrollAreaWidgetContents_21)

        self.verticalLayout_15.addWidget(self.scrollArea_29)


        self.gridLayout_2.addWidget(self.L_widget2_2, 0, 1, 1, 1)


        self.verticalLayout_17.addWidget(self.left_widget)

        self.verticalLayout_17.setStretch(0, 1)
        self.verticalLayout_17.setStretch(1, 20)

        self.retranslateUi(Board)

        QMetaObject.connectSlotsByName(Board)
    # setupUi

    def retranslateUi(self, Board):
        Board.setWindowTitle(QCoreApplication.translate("Board", u"Form", None))
        self.label_ser_info.setText(QCoreApplication.translate("Board", u"\u4e32\u53e3\u4fe1\u606f", None))
        self.comboBox_ser_select_2.setCurrentText("")
        self.comboBox_ser_select_2.setPlaceholderText(QCoreApplication.translate("Board", u"\u9009\u62e9\u7aef\u53e3", None))
        self.label_2.setText(QCoreApplication.translate("Board", u"\u6ce2\u7279\u7387", None))
        self.lineEdit_baud.setText(QCoreApplication.translate("Board", u"115200", None))
        self.pushButton_ser_open.setText(QCoreApplication.translate("Board", u"\u6253\u5f00\u4e32\u53e3", None))
        self.LH_label9_2.setText(QCoreApplication.translate("Board", u"\u56fe\u88683", None))
        self.LH_label14_2.setText(QCoreApplication.translate("Board", u"\u56fe\u88681", None))
        self.LH_label15_2.setText(QCoreApplication.translate("Board", u"\u56fe\u88683", None))
        self.LH_label16_2.setText(QCoreApplication.translate("Board", u"\u56fe\u88681", None))
        self.LH_label13_2.setText(QCoreApplication.translate("Board", u"\u56fe\u88683", None))
        self.LH_label4_2.setText(QCoreApplication.translate("Board", u"\u56fe\u88682", None))
        self.LH_label12_2.setText(QCoreApplication.translate("Board", u"\u56fe\u88683", None))
        self.LH_label1_2.setText(QCoreApplication.translate("Board", u"\u56fe\u88681", None))
        self.LH_label10_2.setText(QCoreApplication.translate("Board", u"\u56fe\u88681", None))
        self.LH_label6_2.setText(QCoreApplication.translate("Board", u"\u56fe\u88681", None))
        self.LH_label3_2.setText(QCoreApplication.translate("Board", u"\u56fe\u88681", None))
        self.LH_label5_2.setText(QCoreApplication.translate("Board", u"\u56fe\u88683", None))
        self.LH_label11_2.setText(QCoreApplication.translate("Board", u"\u56fe\u88683", None))
        self.LH_label7_2.setText(QCoreApplication.translate("Board", u"\u56fe\u88681", None))
        self.LH_label8_2.setText(QCoreApplication.translate("Board", u"\u56fe\u88684", None))
        self.LH_label2_2.setText(QCoreApplication.translate("Board", u"\u56fe\u88681", None))
    # retranslateUi

