# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Form5.ui'
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
from qfluentwidgets import CheckBox
from qfluentwidgets import LineEdit
from qfluentwidgets import TogglePushButton


class Ui_Form5(object):
    def setupUi(self, Form5):
        if not Form5.objectName():
            Form5.setObjectName(u"Form5")
        Form5.resize(596, 513)
        self.verticalLayout = QVBoxLayout(Form5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.serialLabel = QLabel(Form5)
        self.serialLabel.setObjectName(u"serialLabel")

        self.horizontalLayout.addWidget(self.serialLabel)

        self.serialComboBox = ComboBox(Form5)
        self.serialComboBox.setObjectName(u"serialComboBox")

        self.horizontalLayout.addWidget(self.serialComboBox)

        self.baudLabel = QLabel(Form5)
        self.baudLabel.setObjectName(u"baudLabel")

        self.horizontalLayout.addWidget(self.baudLabel)

        self.baudComboBox = ComboBox(Form5)
        self.baudComboBox.setObjectName(u"baudComboBox")

        self.horizontalLayout.addWidget(self.baudComboBox)

        self.connectButton = TogglePushButton(Form5)
        self.connectButton.setObjectName(u"connectButton")

        self.horizontalLayout.addWidget(self.connectButton)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 2)
        self.horizontalLayout.setStretch(2, 1)
        self.horizontalLayout.setStretch(3, 2)
        self.horizontalLayout.setStretch(4, 1)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.tb = QTextBrowser(Form5)
        self.tb.setObjectName(u"tb")

        self.verticalLayout.addWidget(self.tb)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.sendEdit = LineEdit(Form5)
        self.sendEdit.setObjectName(u"sendEdit")

        self.horizontalLayout_2.addWidget(self.sendEdit)

        self.sendButton = PushButton(Form5)
        self.sendButton.setObjectName(u"sendButton")

        self.horizontalLayout_2.addWidget(self.sendButton)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.autoWrapCheckBox = CheckBox(Form5)
        self.autoWrapCheckBox.setObjectName(u"autoWrapCheckBox")

        self.horizontalLayout_3.addWidget(self.autoWrapCheckBox)

        self.showTimeCheckBox = CheckBox(Form5)
        self.showTimeCheckBox.setObjectName(u"showTimeCheckBox")

        self.horizontalLayout_3.addWidget(self.showTimeCheckBox)

        self.saveButton = PushButton(Form5)
        self.saveButton.setObjectName(u"saveButton")

        self.horizontalLayout_3.addWidget(self.saveButton)

        self.clearButton = PushButton(Form5)
        self.clearButton.setObjectName(u"clearButton")

        self.horizontalLayout_3.addWidget(self.clearButton)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.retranslateUi(Form5)

        QMetaObject.connectSlotsByName(Form5)
    # setupUi

    def retranslateUi(self, Form5):
        Form5.setWindowTitle(QCoreApplication.translate("Form5", u"Form", None))
        self.serialLabel.setText(QCoreApplication.translate("Form5", u"\u4e32\u53e3\uff1a", None))
        self.baudLabel.setText(QCoreApplication.translate("Form5", u"\u6ce2\u7279\u7387\uff1a", None))
        self.connectButton.setText(QCoreApplication.translate("Form5", u"\u8fde\u63a5", None))
        self.sendButton.setText(QCoreApplication.translate("Form5", u"\u53d1\u9001", None))
        self.autoWrapCheckBox.setText(QCoreApplication.translate("Form5", u"\u81ea\u52a8\u8ddf\u8e2a", None))
        self.showTimeCheckBox.setText(QCoreApplication.translate("Form5", u"\u663e\u793a\u65f6\u95f4", None))
        self.saveButton.setText(QCoreApplication.translate("Form5", u"\u4fdd\u5b58\u4e3a\u6587\u4ef6", None))
        self.clearButton.setText(QCoreApplication.translate("Form5", u"\u6e05\u7a7a\u8f93\u51fa", None))
    # retranslateUi

