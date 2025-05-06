# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pca_show.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpinBox,
    QToolButton, QVBoxLayout, QWidget)

class Ui_PCA_show(object):
    def setupUi(self, PCA_show):
        if not PCA_show.objectName():
            PCA_show.setObjectName(u"PCA_show")
        PCA_show.resize(300, 238)
        self.verticalLayout = QVBoxLayout(PCA_show)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton = QPushButton(PCA_show)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(PCA_show)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.FilePath_lineEdit = QLineEdit(PCA_show)
        self.FilePath_lineEdit.setObjectName(u"FilePath_lineEdit")

        self.horizontalLayout_2.addWidget(self.FilePath_lineEdit)

        self.toolButton = QToolButton(PCA_show)
        self.toolButton.setObjectName(u"toolButton")

        self.horizontalLayout_2.addWidget(self.toolButton)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setLabelAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.formLayout.setFormAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.formLayout.setHorizontalSpacing(10)
        self.formLayout.setVerticalSpacing(10)
        self.formLayout.setContentsMargins(-1, 10, -1, 10)
        self.label = QLabel(PCA_show)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.Di_spinBox = QSpinBox(PCA_show)
        self.Di_spinBox.setObjectName(u"Di_spinBox")
        self.Di_spinBox.setMinimum(2)
        self.Di_spinBox.setDisplayIntegerBase(10)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.Di_spinBox)

        self.label_2 = QLabel(PCA_show)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.Di_spinBox_2 = QSpinBox(PCA_show)
        self.Di_spinBox_2.setObjectName(u"Di_spinBox_2")
        self.Di_spinBox_2.setMinimum(50)
        self.Di_spinBox_2.setMaximum(99)
        self.Di_spinBox_2.setValue(80)
        self.Di_spinBox_2.setDisplayIntegerBase(10)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.Di_spinBox_2)


        self.verticalLayout.addLayout(self.formLayout)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 4)

        self.retranslateUi(PCA_show)

        QMetaObject.connectSlotsByName(PCA_show)
    # setupUi

    def retranslateUi(self, PCA_show):
        PCA_show.setWindowTitle(QCoreApplication.translate("PCA_show", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("PCA_show", u"\u786e\u5b9a", None))
        self.label_3.setText(QCoreApplication.translate("PCA_show", u"\u6587\u4ef6\u8def\u5f84", None))
        self.toolButton.setText(QCoreApplication.translate("PCA_show", u"...", None))
        self.label.setText(QCoreApplication.translate("PCA_show", u"PCA\u7ef4\u5ea6\uff082-\u4f20\u611f\u5668\u6570\uff09", None))
        self.label_2.setText(QCoreApplication.translate("PCA_show", u"\u8d21\u732e\u5ea6\u9700\u6c42\uff0850-99%\uff09", None))
    # retranslateUi

