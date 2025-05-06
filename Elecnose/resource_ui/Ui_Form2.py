# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Form2.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from qfluentwidgets import PushButton
from qfluentwidgets import ComboBox


class Ui_Board(object):
    def setupUi(self, Board):
        if not Board.objectName():
            Board.setObjectName(u"Board")
        Board.resize(1312, 754)
        self.horizontalLayout = QHBoxLayout(Board)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_2)

        self.LH_label_2 = QLabel(Board)
        self.LH_label_2.setObjectName(u"LH_label_2")

        self.horizontalLayout_7.addWidget(self.LH_label_2)

        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.LH_labelY_2 = QLabel(Board)
        self.LH_labelY_2.setObjectName(u"LH_labelY_2")
        font = QFont()
        font.setPointSize(12)
        self.LH_labelY_2.setFont(font)

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.LH_labelY_2)

        self.LH_ComboBox_1Y_2 = ComboBox(Board)
        self.LH_ComboBox_1Y_2.setObjectName(u"LH_ComboBox_1Y_2")
        self.LH_ComboBox_1Y_2.setMaximumSize(QSize(16777215, 30))

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.LH_ComboBox_1Y_2)

        self.LH_labelX_2 = QLabel(Board)
        self.LH_labelX_2.setObjectName(u"LH_labelX_2")
        self.LH_labelX_2.setFont(font)

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.LH_labelX_2)

        self.LH_ComboBox_1X_2 = ComboBox(Board)
        self.LH_ComboBox_1X_2.setObjectName(u"LH_ComboBox_1X_2")
        self.LH_ComboBox_1X_2.setMaximumSize(QSize(16777215, 30))

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.LH_ComboBox_1X_2)

        self.LH_labelL_2 = QLabel(Board)
        self.LH_labelL_2.setObjectName(u"LH_labelL_2")
        self.LH_labelL_2.setFont(font)

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.LH_labelL_2)

        self.LH_ComboBox_1L_2 = ComboBox(Board)
        self.LH_ComboBox_1L_2.setObjectName(u"LH_ComboBox_1L_2")
        self.LH_ComboBox_1L_2.setMaximumSize(QSize(16777215, 30))

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.LH_ComboBox_1L_2)


        self.horizontalLayout_7.addLayout(self.formLayout_3)

        self.formLayout_4 = QFormLayout()
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.formLayout_4.setFormAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_5 = QLabel(Board)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.label_5)

        self.LH_ComboBox_2 = ComboBox(Board)
        self.LH_ComboBox_2.setObjectName(u"LH_ComboBox_2")
        self.LH_ComboBox_2.setMaximumSize(QSize(16777215, 30))

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.LH_ComboBox_2)

        self.label_6 = QLabel(Board)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.formLayout_4.setWidget(1, QFormLayout.LabelRole, self.label_6)

        self.comboBox_C1_2 = ComboBox(Board)
        self.comboBox_C1_2.setObjectName(u"comboBox_C1_2")
        self.comboBox_C1_2.setMaximumSize(QSize(16777215, 30))

        self.formLayout_4.setWidget(1, QFormLayout.FieldRole, self.comboBox_C1_2)


        self.horizontalLayout_7.addLayout(self.formLayout_4)

        self.LH_Button_2 = PushButton(Board)
        self.LH_Button_2.setObjectName(u"LH_Button_2")

        self.horizontalLayout_7.addWidget(self.LH_Button_2)

        self.horizontalLayout_7.setStretch(0, 1)
        self.horizontalLayout_7.setStretch(1, 2)
        self.horizontalLayout_7.setStretch(2, 2)
        self.horizontalLayout_7.setStretch(3, 2)
        self.horizontalLayout_7.setStretch(4, 1)

        self.verticalLayout_4.addLayout(self.horizontalLayout_7)

        self.graphicsView = QGraphicsView(Board)
        self.graphicsView.setObjectName(u"graphicsView")

        self.verticalLayout_4.addWidget(self.graphicsView)


        self.horizontalLayout.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label = QLabel(Board)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamily(u"\u5b8b\u4f53")
        font1.setPointSize(12)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label)

        self.textBrowser = QTextBrowser(Board)
        self.textBrowser.setObjectName(u"textBrowser")

        self.verticalLayout_5.addWidget(self.textBrowser)


        self.horizontalLayout.addLayout(self.verticalLayout_5)

        self.horizontalLayout.setStretch(0, 4)
        self.horizontalLayout.setStretch(1, 2)

        self.retranslateUi(Board)

        QMetaObject.connectSlotsByName(Board)
    # setupUi

    def retranslateUi(self, Board):
        Board.setWindowTitle(QCoreApplication.translate("Board", u"Form", None))
        self.LH_label_2.setText(QCoreApplication.translate("Board", u"\u5206\u6790\u56fe\u8868", None))
        self.LH_labelY_2.setText(QCoreApplication.translate("Board", u"\u6807\u7b7e", None))
        self.LH_labelX_2.setText(QCoreApplication.translate("Board", u"target", None))
        self.LH_labelL_2.setText(QCoreApplication.translate("Board", u"\u7ef4\u5ea6", None))
        self.label_5.setText(QCoreApplication.translate("Board", u"\u5206\u6790\u65b9\u6cd5", None))
        self.label_6.setText(QCoreApplication.translate("Board", u"\u989c\u8272", None))
        self.LH_Button_2.setText(QCoreApplication.translate("Board", u"\u786e\u5b9a", None))
        self.label.setText(QCoreApplication.translate("Board", u"\u5176\u4ed6\u5185\u5bb9", None))
    # retranslateUi

