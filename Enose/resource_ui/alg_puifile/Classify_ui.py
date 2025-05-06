# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Classify_ui.ui'
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
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QToolButton,
    QVBoxLayout, QWidget)

class Ui_Classify_ui(object):
    def setupUi(self, Classify_ui):
        if not Classify_ui.objectName():
            Classify_ui.setObjectName(u"Classify_ui")
        Classify_ui.resize(306, 238)
        self.verticalLayout = QVBoxLayout(Classify_ui)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton_2 = QPushButton(Classify_ui)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout.addWidget(self.pushButton_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(Classify_ui)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.FilePath_lineEdit = QLineEdit(Classify_ui)
        self.FilePath_lineEdit.setObjectName(u"FilePath_lineEdit")

        self.horizontalLayout_2.addWidget(self.FilePath_lineEdit)

        self.toolButton = QToolButton(Classify_ui)
        self.toolButton.setObjectName(u"toolButton")

        self.horizontalLayout_2.addWidget(self.toolButton)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(Classify_ui)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.doubleSpinBox = QDoubleSpinBox(Classify_ui)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")
        self.doubleSpinBox.setDecimals(1)
        self.doubleSpinBox.setMinimum(0.100000000000000)
        self.doubleSpinBox.setMaximum(0.500000000000000)
        self.doubleSpinBox.setSingleStep(0.100000000000000)
        self.doubleSpinBox.setValue(0.200000000000000)

        self.horizontalLayout.addWidget(self.doubleSpinBox)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 4)

        self.retranslateUi(Classify_ui)

        QMetaObject.connectSlotsByName(Classify_ui)
    # setupUi

    def retranslateUi(self, Classify_ui):
        Classify_ui.setWindowTitle(QCoreApplication.translate("Classify_ui", u"Form", None))
        self.pushButton_2.setText(QCoreApplication.translate("Classify_ui", u"\u4f7f\u7528\u6a21\u578b", None))
        self.label_2.setText(QCoreApplication.translate("Classify_ui", u"\u6587\u4ef6\u8def\u5f84", None))
        self.toolButton.setText(QCoreApplication.translate("Classify_ui", u"...", None))
        self.label.setText(QCoreApplication.translate("Classify_ui", u"\u8bbe\u7f6e\u6d4b\u8bd5\u96c6\u5360\u6bd4(0.1-0.5)", None))
    # retranslateUi

