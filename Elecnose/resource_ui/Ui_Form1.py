# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Form1.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from qfluentwidgets import PushButton


class Ui_date_get(object):
    def setupUi(self, date_get):
        if not date_get.objectName():
            date_get.setObjectName(u"date_get")
        date_get.resize(1059, 672)
        date_get.setStyleSheet(u"background-color: rgba(255, 255, 255, 0)")
        self.gridLayout = QGridLayout(date_get)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.label = QLabel(date_get)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamily(u"\u9ed1\u4f53")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet(u"font: 22pt \"Agency FB\";\n"
"font: 18pt \"\u9ed1\u4f53\";\n"
"")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.Button = PushButton(date_get)
        self.Button.setObjectName(u"Button")

        self.horizontalLayout.addWidget(self.Button)

        self.horizontalLayout.setStretch(0, 5)
        self.horizontalLayout.setStretch(1, 2)
        self.horizontalLayout.setStretch(2, 3)
        self.horizontalLayout.setStretch(3, 2)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.line_2 = QFrame(date_get)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_2)

        self.textEdit = QTextEdit(date_get)
        self.textEdit.setObjectName(u"textEdit")
        font1 = QFont()
        font1.setPointSize(10)
        self.textEdit.setFont(font1)

        self.verticalLayout.addWidget(self.textEdit)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.retranslateUi(date_get)

        QMetaObject.connectSlotsByName(date_get)
    # setupUi

    def retranslateUi(self, date_get):
        date_get.setWindowTitle(QCoreApplication.translate("date_get", u"Form", None))
#if QT_CONFIG(accessibility)
        self.label.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.label.setText(QCoreApplication.translate("date_get", u"\u6570\u636e\u6e90", None))
#if QT_CONFIG(accessibility)
        self.Button.setAccessibleDescription(QCoreApplication.translate("date_get", u"background-color: rgba(255, 255, 255, 0)", None))
#endif // QT_CONFIG(accessibility)
        self.Button.setText(QCoreApplication.translate("date_get", u"\u5f00\u59cb\u5904\u7406", None))
    # retranslateUi

