# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Gragh_show.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QGridLayout, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QSpinBox,
    QTabWidget, QTableView, QToolButton, QVBoxLayout,
    QWidget)
# import icon_rc

class Ui_Gragh_show(object):
    def setupUi(self, Gragh_show):
        if not Gragh_show.objectName():
            Gragh_show.setObjectName(u"Gragh_show")
        Gragh_show.resize(1246, 802)
        self.horizontalLayout_3 = QHBoxLayout(Gragh_show)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox = QGroupBox(Gragh_show)
        self.groupBox.setObjectName(u"groupBox")
        font = QFont()
        font.setBold(False)
        self.groupBox.setFont(font)
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox_2 = QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.Folder_lineEdit = QLineEdit(self.groupBox_2)
        self.Folder_lineEdit.setObjectName(u"Folder_lineEdit")

        self.horizontalLayout_2.addWidget(self.Folder_lineEdit)

        self.Folder_Button = QToolButton(self.groupBox_2)
        self.Folder_Button.setObjectName(u"Folder_Button")

        self.horizontalLayout_2.addWidget(self.Folder_Button)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.groupBox)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_4 = QGridLayout(self.groupBox_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setVerticalSpacing(9)
        self.label_3 = QLabel(self.groupBox_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout_4.addWidget(self.label_3, 2, 0, 1, 1)

        self.label_4 = QLabel(self.groupBox_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout_4.addWidget(self.label_4, 3, 0, 1, 1)

        self.Flowtime_spinBox = QSpinBox(self.groupBox_3)
        self.Flowtime_spinBox.setObjectName(u"Flowtime_spinBox")
        self.Flowtime_spinBox.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.Flowtime_spinBox.setValue(10)

        self.gridLayout_4.addWidget(self.Flowtime_spinBox, 3, 1, 1, 1)

        self.label_2 = QLabel(self.groupBox_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout_4.addWidget(self.label_2, 0, 0, 1, 1)

        self.Inputtime_spinBox = QSpinBox(self.groupBox_3)
        self.Inputtime_spinBox.setObjectName(u"Inputtime_spinBox")
        self.Inputtime_spinBox.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.Inputtime_spinBox.setValue(60)

        self.gridLayout_4.addWidget(self.Inputtime_spinBox, 2, 1, 1, 1)

        self.Cleartime_spinBox = QSpinBox(self.groupBox_3)
        self.Cleartime_spinBox.setObjectName(u"Cleartime_spinBox")
        self.Cleartime_spinBox.setFocusPolicy(Qt.WheelFocus)
        self.Cleartime_spinBox.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.Cleartime_spinBox.setValue(60)

        self.gridLayout_4.addWidget(self.Cleartime_spinBox, 0, 1, 1, 1)

        self.gridLayout_4.setColumnStretch(0, 1)
        self.gridLayout_4.setColumnStretch(1, 4)

        self.verticalLayout.addWidget(self.groupBox_3)

        self.groupBox_4 = QGroupBox(self.groupBox)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.gridLayout_2 = QGridLayout(self.groupBox_4)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.Senser_stableView = QTableView(self.groupBox_4)
        self.Senser_stableView.setObjectName(u"Senser_stableView")
        self.Senser_stableView.setMinimumSize(QSize(226, 0))
        self.Senser_stableView.setMaximumSize(QSize(226, 16777215))

        self.gridLayout_2.addWidget(self.Senser_stableView, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.groupBox_4)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 2)
        self.verticalLayout.setStretch(2, 8)

        self.gridLayout.addWidget(self.groupBox, 0, 0, 2, 1)

        self.widget = QWidget(Gragh_show)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 0, -1, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.Dataclear_Button = QPushButton(self.widget)
        self.Dataclear_Button.setObjectName(u"Dataclear_Button")
        self.Dataclear_Button.setMaximumSize(QSize(100, 32))
        self.Dataclear_Button.setAutoFillBackground(False)

        self.horizontalLayout.addWidget(self.Dataclear_Button)

        self.Collectbegin_Button = QPushButton(self.widget)
        self.Collectbegin_Button.setObjectName(u"Collectbegin_Button")
        self.Collectbegin_Button.setMaximumSize(QSize(100, 32))

        self.horizontalLayout.addWidget(self.Collectbegin_Button)

        self.Pause_Button = QPushButton(self.widget)
        self.Pause_Button.setObjectName(u"Pause_Button")
        self.Pause_Button.setMaximumSize(QSize(100, 32))

        self.horizontalLayout.addWidget(self.Pause_Button)

        self.Save_Button = QPushButton(self.widget)
        self.Save_Button.setObjectName(u"Save_Button")
        self.Save_Button.setMaximumSize(QSize(100, 32))

        self.horizontalLayout.addWidget(self.Save_Button)


        self.gridLayout.addWidget(self.widget, 0, 1, 1, 1)

        self.tabWidget = QTabWidget(Gragh_show)
        self.tabWidget.setObjectName(u"tabWidget")
        self.Line_Show = QWidget()
        self.Line_Show.setObjectName(u"Line_Show")
        self.gridLayout_5 = QGridLayout(self.Line_Show)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.Linegragh_Layout = QVBoxLayout()
        self.Linegragh_Layout.setObjectName(u"Linegragh_Layout")

        self.gridLayout_5.addLayout(self.Linegragh_Layout, 0, 0, 1, 1)

        self.tabWidget.addTab(self.Line_Show, "")

        self.gridLayout.addWidget(self.tabWidget, 1, 1, 1, 1)

        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 4)

        self.horizontalLayout_3.addLayout(self.gridLayout)


        self.retranslateUi(Gragh_show)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Gragh_show)
    # setupUi

    def retranslateUi(self, Gragh_show):
        Gragh_show.setWindowTitle(QCoreApplication.translate("Gragh_show", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("Gragh_show", u"\u5b9e\u9a8c\u4fe1\u606f", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Gragh_show", u"\u5b58\u50a8\u5730\u5740", None))
        self.Folder_Button.setText(QCoreApplication.translate("Gragh_show", u"...", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Gragh_show", u"\u91c7\u6837\u8bbe\u7f6e", None))
        self.label_3.setText(QCoreApplication.translate("Gragh_show", u"\u8fdb\u6837\u65f6\u957f(s)", None))
        self.label_4.setText(QCoreApplication.translate("Gragh_show", u"\u6d41\u91cf(L/min)", None))
        self.label_2.setText(QCoreApplication.translate("Gragh_show", u"\u6e05\u6d17\u65f6\u957f(s)", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Gragh_show", u"\u4f20\u611f\u5668\u5217\u8868", None))
        self.Dataclear_Button.setText(QCoreApplication.translate("Gragh_show", u"\u6570\u636e\u6e05\u6d17", None))
        self.Collectbegin_Button.setText(QCoreApplication.translate("Gragh_show", u"\u5f00\u59cb\u91c7\u96c6", None))
        self.Pause_Button.setText(QCoreApplication.translate("Gragh_show", u"\u6682\u505c\u91c7\u96c6", None))
        self.Save_Button.setText(QCoreApplication.translate("Gragh_show", u"\u4fdd\u5b58\u6570\u636e", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Line_Show), QCoreApplication.translate("Gragh_show", u"\u66f2\u7ebf\u56fe", None))
    # retranslateUi

