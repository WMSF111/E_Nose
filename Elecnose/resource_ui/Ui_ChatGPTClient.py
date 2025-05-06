# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ChatGPTClient.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from qfluentwidgets import PushButton
from qfluentwidgets import ListWidget
from qfluentwidgets import DoubleSpinBox
from qfluentwidgets import SpinBox
from qfluentwidgets import TextEdit


class Ui_Frame(object):
    def setupUi(self, Frame):
        if not Frame.objectName():
            Frame.setObjectName(u"Frame")
        Frame.resize(1100, 900)
        Frame.setMaximumSize(QSize(1100, 900))
        self.horizontalLayout_2 = QHBoxLayout(Frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.btnNewSession = PushButton(Frame)
        self.btnNewSession.setObjectName(u"btnNewSession")

        self.verticalLayout.addWidget(self.btnNewSession)

        self.lwSessions = ListWidget(Frame)
        self.lwSessions.setObjectName(u"lwSessions")
        self.lwSessions.setStyleSheet(u"backgtound rgb(255, 255, 255,255)")

        self.verticalLayout.addWidget(self.lwSessions)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 8)

        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_2 = QLabel(Frame)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)

        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)

        self.dsbTemperature = DoubleSpinBox(Frame)
        self.dsbTemperature.setObjectName(u"dsbTemperature")
        self.dsbTemperature.setDecimals(1)
        self.dsbTemperature.setMaximum(2.000000000000000)
        self.dsbTemperature.setSingleStep(0.100000000000000)
        self.dsbTemperature.setValue(1.000000000000000)

        self.gridLayout_2.addWidget(self.dsbTemperature, 0, 1, 1, 1)

        self.label_3 = QLabel(Frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)

        self.dsbTopP = DoubleSpinBox(Frame)
        self.dsbTopP.setObjectName(u"dsbTopP")
        self.dsbTopP.setDecimals(1)
        self.dsbTopP.setMaximum(2.000000000000000)
        self.dsbTopP.setSingleStep(0.100000000000000)
        self.dsbTopP.setValue(1.000000000000000)

        self.gridLayout_2.addWidget(self.dsbTopP, 1, 1, 1, 1)

        self.label_4 = QLabel(Frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.gridLayout_2.addWidget(self.label_4, 2, 0, 1, 1)

        self.sbMaxTokens = SpinBox(Frame)
        self.sbMaxTokens.setObjectName(u"sbMaxTokens")
        self.sbMaxTokens.setMinimum(1)
        self.sbMaxTokens.setMaximum(200)
        self.sbMaxTokens.setValue(16)

        self.gridLayout_2.addWidget(self.sbMaxTokens, 2, 1, 1, 1)

        self.label_9 = QLabel(Frame)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)

        self.gridLayout_2.addWidget(self.label_9, 3, 0, 1, 1)

        self.sbBestOf = SpinBox(Frame)
        self.sbBestOf.setObjectName(u"sbBestOf")
        self.sbBestOf.setMinimum(1)
        self.sbBestOf.setMaximum(10)

        self.gridLayout_2.addWidget(self.sbBestOf, 3, 1, 1, 1)

        self.label_6 = QLabel(Frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)

        self.gridLayout_2.addWidget(self.label_6, 4, 0, 1, 1)

        self.sbN = SpinBox(Frame)
        self.sbN.setObjectName(u"sbN")
        self.sbN.setMinimum(1)
        self.sbN.setMaximum(10)

        self.gridLayout_2.addWidget(self.sbN, 4, 1, 1, 1)

        self.label_7 = QLabel(Frame)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_2.addWidget(self.label_7, 5, 0, 1, 1)

        self.dsbPresencePenalty = DoubleSpinBox(Frame)
        self.dsbPresencePenalty.setObjectName(u"dsbPresencePenalty")
        self.dsbPresencePenalty.setDecimals(1)
        self.dsbPresencePenalty.setMinimum(-2.000000000000000)
        self.dsbPresencePenalty.setMaximum(2.000000000000000)
        self.dsbPresencePenalty.setSingleStep(0.100000000000000)

        self.gridLayout_2.addWidget(self.dsbPresencePenalty, 5, 1, 1, 1)

        self.label_8 = QLabel(Frame)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_2.addWidget(self.label_8, 6, 0, 1, 1)

        self.dsbFrequencyPenalty = DoubleSpinBox(Frame)
        self.dsbFrequencyPenalty.setObjectName(u"dsbFrequencyPenalty")
        self.dsbFrequencyPenalty.setDecimals(1)
        self.dsbFrequencyPenalty.setMinimum(-2.000000000000000)
        self.dsbFrequencyPenalty.setMaximum(2.000000000000000)
        self.dsbFrequencyPenalty.setSingleStep(0.100000000000000)

        self.gridLayout_2.addWidget(self.dsbFrequencyPenalty, 6, 1, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout_2)

        self.verticalLayout_3.setStretch(0, 2)
        self.verticalLayout_3.setStretch(1, 1)

        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.tbChat = QTextBrowser(Frame)
        self.tbChat.setObjectName(u"tbChat")
        font1 = QFont()
        font1.setPointSize(14)
        self.tbChat.setFont(font1)
        self.tbChat.setStyleSheet(u"backgtound rgb(255, 255, 255,255)")

        self.verticalLayout_4.addWidget(self.tbChat)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.teMessage = TextEdit(Frame)
        self.teMessage.setObjectName(u"teMessage")
        self.teMessage.setFont(font1)

        self.horizontalLayout.addWidget(self.teMessage)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.btnSend = PushButton(Frame)
        self.btnSend.setObjectName(u"btnSend")

        self.verticalLayout_2.addWidget(self.btnSend)

        self.btnStop = PushButton(Frame)
        self.btnStop.setObjectName(u"btnStop")

        self.verticalLayout_2.addWidget(self.btnStop)

        self.verticalLayout_2.setStretch(0, 8)
        self.verticalLayout_2.setStretch(1, 1)

        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.horizontalLayout.setStretch(0, 6)
        self.horizontalLayout.setStretch(1, 1)

        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.verticalLayout_4.setStretch(0, 4)
        self.verticalLayout_4.setStretch(1, 1)

        self.horizontalLayout_2.addLayout(self.verticalLayout_4)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 4)

        self.retranslateUi(Frame)

        QMetaObject.connectSlotsByName(Frame)
    # setupUi

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(QCoreApplication.translate("Frame", u"ChatGPT", None))
        self.btnNewSession.setText(QCoreApplication.translate("Frame", u"\u65b0\u5efa\u4f1a\u8bdd", None))
        self.label_2.setText(QCoreApplication.translate("Frame", u"temperature", None))
        self.label_3.setText(QCoreApplication.translate("Frame", u"top_p", None))
        self.label_4.setText(QCoreApplication.translate("Frame", u"max_tokens", None))
        self.label_9.setText(QCoreApplication.translate("Frame", u"best_of", None))
        self.label_6.setText(QCoreApplication.translate("Frame", u"n", None))
        self.label_7.setText(QCoreApplication.translate("Frame", u"presence_penalty", None))
        self.label_8.setText(QCoreApplication.translate("Frame", u"frequency_penalty", None))
        self.btnSend.setText(QCoreApplication.translate("Frame", u"\u53d1 \u9001", None))
        self.btnStop.setText(QCoreApplication.translate("Frame", u"\u505c \u6b62", None))
    # retranslateUi

