# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Serial.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QTextBrowser, QVBoxLayout,
    QWidget)

class Ui_Serial(object):
    def setupUi(self, Serial):
        if not Serial.objectName():
            Serial.setObjectName(u"Serial")
        Serial.resize(641, 490)
        self.gridLayout = QGridLayout(Serial)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(Serial)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.formLayout = QFormLayout(self.groupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.CheckButton = QPushButton(self.groupBox)
        self.CheckButton.setObjectName(u"CheckButton")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.CheckButton)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_5)

        self.serialComboBox = QComboBox(self.groupBox)
        self.serialComboBox.setObjectName(u"serialComboBox")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.serialComboBox)

        self.statues = QLabel(self.groupBox)
        self.statues.setObjectName(u"statues")
        self.statues.setTextFormat(Qt.AutoText)

        self.formLayout.setWidget(2, QFormLayout.SpanningRole, self.statues)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_6)

        self.baudComboBox = QComboBox(self.groupBox)
        self.baudComboBox.addItem("")
        self.baudComboBox.addItem("")
        self.baudComboBox.addItem("")
        self.baudComboBox.addItem("")
        self.baudComboBox.addItem("")
        self.baudComboBox.addItem("")
        self.baudComboBox.addItem("")
        self.baudComboBox.addItem("")
        self.baudComboBox.addItem("")
        self.baudComboBox.addItem("")
        self.baudComboBox.addItem("")
        self.baudComboBox.addItem("")
        self.baudComboBox.setObjectName(u"baudComboBox")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.baudComboBox)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_7)

        self.dataComboBox = QComboBox(self.groupBox)
        self.dataComboBox.addItem("")
        self.dataComboBox.addItem("")
        self.dataComboBox.addItem("")
        self.dataComboBox.addItem("")
        self.dataComboBox.setObjectName(u"dataComboBox")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.dataComboBox)

        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_8)

        self.checkComboBox = QComboBox(self.groupBox)
        self.checkComboBox.addItem("")
        self.checkComboBox.setObjectName(u"checkComboBox")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.checkComboBox)

        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_9)

        self.stopComboBox = QComboBox(self.groupBox)
        self.stopComboBox.addItem("")
        self.stopComboBox.addItem("")
        self.stopComboBox.addItem("")
        self.stopComboBox.setObjectName(u"stopComboBox")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.stopComboBox)

        self.connectButton = QPushButton(self.groupBox)
        self.connectButton.setObjectName(u"connectButton")

        self.formLayout.setWidget(7, QFormLayout.SpanningRole, self.connectButton)


        self.verticalLayout.addWidget(self.groupBox)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.sendEdit = QLineEdit(Serial)
        self.sendEdit.setObjectName(u"sendEdit")

        self.horizontalLayout_2.addWidget(self.sendEdit)

        self.sendButton = QPushButton(Serial)
        self.sendButton.setObjectName(u"sendButton")

        self.horizontalLayout_2.addWidget(self.sendButton)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.saveButton = QPushButton(Serial)
        self.saveButton.setObjectName(u"saveButton")

        self.horizontalLayout_3.addWidget(self.saveButton)

        self.clearButton = QPushButton(Serial)
        self.clearButton.setObjectName(u"clearButton")

        self.horizontalLayout_3.addWidget(self.clearButton)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.verticalLayout.setStretch(0, 4)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 1)

        self.horizontalLayout.addLayout(self.verticalLayout)

        self.tb = QTextBrowser(Serial)
        self.tb.setObjectName(u"tb")

        self.horizontalLayout.addWidget(self.tb)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 2)

        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)


        self.retranslateUi(Serial)

        self.baudComboBox.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Serial)
    # setupUi

    def retranslateUi(self, Serial):
        Serial.setWindowTitle(QCoreApplication.translate("Serial", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("Serial", u"\u4e32\u53e3\u8bbe\u7f6e", None))
        self.label.setText(QCoreApplication.translate("Serial", u"\u4e32\u53e3\u68c0\u6d4b", None))
        self.CheckButton.setText(QCoreApplication.translate("Serial", u"\u5f00\u59cb\u68c0\u6d4b", None))
        self.label_5.setText(QCoreApplication.translate("Serial", u"<html><head/><body><p align=\"center\">\u4e32\u53e3\u9009\u62e9</p></body></html>", None))
        self.statues.setText(QCoreApplication.translate("Serial", u"<html><head/><body><p align=\"center\"><span style=\" color:#ff0000;\"><br/></span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("Serial", u"<html><head/><body><p align=\"justify\">\u6ce2\u7279\u7387:</p></body></html>", None))
        self.baudComboBox.setItemText(0, QCoreApplication.translate("Serial", u"9600", None))
        self.baudComboBox.setItemText(1, QCoreApplication.translate("Serial", u"2400", None))
        self.baudComboBox.setItemText(2, QCoreApplication.translate("Serial", u"4800", None))
        self.baudComboBox.setItemText(3, QCoreApplication.translate("Serial", u"12800", None))
        self.baudComboBox.setItemText(4, QCoreApplication.translate("Serial", u"14400", None))
        self.baudComboBox.setItemText(5, QCoreApplication.translate("Serial", u"19200", None))
        self.baudComboBox.setItemText(6, QCoreApplication.translate("Serial", u"38400", None))
        self.baudComboBox.setItemText(7, QCoreApplication.translate("Serial", u"57600", None))
        self.baudComboBox.setItemText(8, QCoreApplication.translate("Serial", u"76800", None))
        self.baudComboBox.setItemText(9, QCoreApplication.translate("Serial", u"115200", None))
        self.baudComboBox.setItemText(10, QCoreApplication.translate("Serial", u"230400", None))
        self.baudComboBox.setItemText(11, QCoreApplication.translate("Serial", u"460800", None))

        self.baudComboBox.setCurrentText(QCoreApplication.translate("Serial", u"9600", None))
        self.label_7.setText(QCoreApplication.translate("Serial", u"<html><head/><body><p align=\"justify\">\u6570\u636e\u4f4d\uff1a</p></body></html>", None))
        self.dataComboBox.setItemText(0, QCoreApplication.translate("Serial", u"8", None))
        self.dataComboBox.setItemText(1, QCoreApplication.translate("Serial", u"7", None))
        self.dataComboBox.setItemText(2, QCoreApplication.translate("Serial", u"6", None))
        self.dataComboBox.setItemText(3, QCoreApplication.translate("Serial", u"5", None))

        self.label_8.setText(QCoreApplication.translate("Serial", u"<html><head/><body><p align=\"justify\">\u6821\u9a8c\u4f4d:</p></body></html>", None))
        self.checkComboBox.setItemText(0, QCoreApplication.translate("Serial", u"N", None))

        self.label_9.setText(QCoreApplication.translate("Serial", u"<html><head/><body><p align=\"justify\">\u505c\u6b62\u4f4d:</p></body></html>", None))
        self.stopComboBox.setItemText(0, QCoreApplication.translate("Serial", u"1", None))
        self.stopComboBox.setItemText(1, QCoreApplication.translate("Serial", u"1.5", None))
        self.stopComboBox.setItemText(2, QCoreApplication.translate("Serial", u"2", None))

        self.connectButton.setText(QCoreApplication.translate("Serial", u"\u8fde\u63a5", None))
        self.sendButton.setText(QCoreApplication.translate("Serial", u"\u53d1\u9001", None))
        self.saveButton.setText(QCoreApplication.translate("Serial", u"\u4fdd\u5b58\u4e3a\u6587\u4ef6", None))
        self.clearButton.setText(QCoreApplication.translate("Serial", u"\u6e05\u7a7a\u8f93\u51fa", None))
    # retranslateUi

