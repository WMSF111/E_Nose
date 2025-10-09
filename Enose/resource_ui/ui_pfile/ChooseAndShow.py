# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ChooseAndShow.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QDoubleSpinBox, QGridLayout,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpinBox,
    QTabWidget, QTableView, QToolButton, QVBoxLayout,
    QWidget)

class Ui_Gragh_show(object):
    def setupUi(self, Gragh_show):
        if not Gragh_show.objectName():
            Gragh_show.setObjectName(u"Gragh_show")
        Gragh_show.resize(997, 662)
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
        self.verticalLayout.setContentsMargins(3, -1, 3, -1)
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
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_2 = QLabel(self.groupBox_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_7.addWidget(self.label_2)

        self.Cleartime_spinBox = QSpinBox(self.groupBox_3)
        self.Cleartime_spinBox.setObjectName(u"Cleartime_spinBox")
        self.Cleartime_spinBox.setFocusPolicy(Qt.WheelFocus)
        self.Cleartime_spinBox.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.Cleartime_spinBox.setMinimum(10)
        self.Cleartime_spinBox.setMaximum(256)
        self.Cleartime_spinBox.setValue(10)

        self.horizontalLayout_7.addWidget(self.Cleartime_spinBox)

        self.label_34 = QLabel(self.groupBox_3)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_7.addWidget(self.label_34)

        self.label_4 = QLabel(self.groupBox_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_7.addWidget(self.label_4)

        self.Sample_spinBox = QSpinBox(self.groupBox_3)
        self.Sample_spinBox.setObjectName(u"Sample_spinBox")
        self.Sample_spinBox.setFocusPolicy(Qt.WheelFocus)
        self.Sample_spinBox.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.Sample_spinBox.setMinimum(0)
        self.Sample_spinBox.setMaximum(256)
        self.Sample_spinBox.setValue(10)

        self.horizontalLayout_7.addWidget(self.Sample_spinBox)

        self.label_35 = QLabel(self.groupBox_3)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_7.addWidget(self.label_35)

        self.horizontalLayout_7.setStretch(0, 3)
        self.horizontalLayout_7.setStretch(1, 2)
        self.horizontalLayout_7.setStretch(2, 1)
        self.horizontalLayout_7.setStretch(3, 3)
        self.horizontalLayout_7.setStretch(4, 2)
        self.horizontalLayout_7.setStretch(5, 1)

        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_10 = QLabel(self.groupBox_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_6.addWidget(self.label_10)

        self.Volum_spinBox = QSpinBox(self.groupBox_3)
        self.Volum_spinBox.setObjectName(u"Volum_spinBox")
        self.Volum_spinBox.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.Volum_spinBox.setMinimum(0)
        self.Volum_spinBox.setMaximum(256)
        self.Volum_spinBox.setValue(1)
        self.Volum_spinBox.setDisplayIntegerBase(10)

        self.horizontalLayout_6.addWidget(self.Volum_spinBox)

        self.label_20 = QLabel(self.groupBox_3)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_6.addWidget(self.label_20)

        self.label_6 = QLabel(self.groupBox_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_6.addWidget(self.label_6)

        self.Simnum_spinBox = QSpinBox(self.groupBox_3)
        self.Simnum_spinBox.setObjectName(u"Simnum_spinBox")
        self.Simnum_spinBox.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.Simnum_spinBox.setMinimum(1)
        self.Simnum_spinBox.setMaximum(16)
        self.Simnum_spinBox.setValue(1)
        self.Simnum_spinBox.setDisplayIntegerBase(10)

        self.horizontalLayout_6.addWidget(self.Simnum_spinBox)

        self.horizontalLayout_6.setStretch(0, 3)
        self.horizontalLayout_6.setStretch(1, 2)
        self.horizontalLayout_6.setStretch(2, 1)
        self.horizontalLayout_6.setStretch(3, 3)
        self.horizontalLayout_6.setStretch(4, 3)

        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_12 = QLabel(self.groupBox_3)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_8.addWidget(self.label_12)

        self.Heattep_SpinBox = QDoubleSpinBox(self.groupBox_3)
        self.Heattep_SpinBox.setObjectName(u"Heattep_SpinBox")
        self.Heattep_SpinBox.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.Heattep_SpinBox.setDecimals(1)
        self.Heattep_SpinBox.setMinimum(-1.000000000000000)
        self.Heattep_SpinBox.setValue(50.000000000000000)

        self.horizontalLayout_8.addWidget(self.Heattep_SpinBox)

        self.label_19 = QLabel(self.groupBox_3)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_8.addWidget(self.label_19)

        self.label_9 = QLabel(self.groupBox_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_8.addWidget(self.label_9)

        self.Standtime_spinBox = QSpinBox(self.groupBox_3)
        self.Standtime_spinBox.setObjectName(u"Standtime_spinBox")
        self.Standtime_spinBox.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.Standtime_spinBox.setMinimum(1)
        self.Standtime_spinBox.setMaximum(60)
        self.Standtime_spinBox.setValue(1)
        self.Standtime_spinBox.setDisplayIntegerBase(10)

        self.horizontalLayout_8.addWidget(self.Standtime_spinBox)

        self.horizontalLayout_8.setStretch(0, 3)
        self.horizontalLayout_8.setStretch(1, 2)
        self.horizontalLayout_8.setStretch(2, 1)
        self.horizontalLayout_8.setStretch(3, 3)
        self.horizontalLayout_8.setStretch(4, 3)

        self.verticalLayout_2.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_11 = QLabel(self.groupBox_3)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_10.addWidget(self.label_11)

        self.Currtem_spinBox = QSpinBox(self.groupBox_3)
        self.Currtem_spinBox.setObjectName(u"Currtem_spinBox")
        self.Currtem_spinBox.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.Currtem_spinBox.setMinimum(1)
        self.Currtem_spinBox.setMaximum(65535)
        self.Currtem_spinBox.setValue(1)
        self.Currtem_spinBox.setDisplayIntegerBase(10)

        self.horizontalLayout_10.addWidget(self.Currtem_spinBox)

        self.label_21 = QLabel(self.groupBox_3)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_10.addWidget(self.label_21)

        self.label_13 = QLabel(self.groupBox_3)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_10.addWidget(self.label_13)

        self.attendtime_spinBox = QSpinBox(self.groupBox_3)
        self.attendtime_spinBox.setObjectName(u"attendtime_spinBox")
        self.attendtime_spinBox.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.attendtime_spinBox.setMinimum(1)
        self.attendtime_spinBox.setMaximum(65535)
        self.attendtime_spinBox.setValue(1)
        self.attendtime_spinBox.setDisplayIntegerBase(10)

        self.horizontalLayout_10.addWidget(self.attendtime_spinBox)

        self.horizontalLayout_10.setStretch(0, 3)
        self.horizontalLayout_10.setStretch(1, 2)
        self.horizontalLayout_10.setStretch(2, 1)
        self.horizontalLayout_10.setStretch(3, 3)
        self.horizontalLayout_10.setStretch(4, 3)

        self.verticalLayout_2.addLayout(self.horizontalLayout_10)


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

        self.verticalLayout.setStretch(2, 10)

        self.gridLayout.addWidget(self.groupBox, 0, 0, 2, 1)

        self.widget = QWidget(Gragh_show)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 0, -1, 0)
        self.label_37 = QLabel(self.widget)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setLayoutDirection(Qt.LeftToRight)
        self.label_37.setTextFormat(Qt.AutoText)
        self.label_37.setScaledContents(False)

        self.horizontalLayout.addWidget(self.label_37)

        self.statues_label = QLabel(self.widget)
        self.statues_label.setObjectName(u"statues_label")

        self.horizontalLayout.addWidget(self.statues_label)

        self.InitPos_Button = QPushButton(self.widget)
        self.InitPos_Button.setObjectName(u"InitPos_Button")
        self.InitPos_Button.setMaximumSize(QSize(100, 32))

        self.horizontalLayout.addWidget(self.InitPos_Button)

        self.Clear_Button = QPushButton(self.widget)
        self.Clear_Button.setObjectName(u"Clear_Button")
        self.Clear_Button.setMaximumSize(QSize(100, 32))

        self.horizontalLayout.addWidget(self.Clear_Button)

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

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 10)
        self.horizontalLayout.setStretch(4, 1)
        self.horizontalLayout.setStretch(5, 1)
        self.horizontalLayout.setStretch(6, 1)

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
        self.groupBox_2.setTitle(QCoreApplication.translate("Gragh_show", u"\u4fdd\u5b58\u8def\u5f84", None))
        self.Folder_Button.setText(QCoreApplication.translate("Gragh_show", u"...", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Gragh_show", u"\u91c7\u6837\u8bbe\u7f6e", None))
        self.label_2.setText(QCoreApplication.translate("Gragh_show", u"\u6d17\u6c14\u65f6\u957f", None))
        self.label_34.setText(QCoreApplication.translate("Gragh_show", u"s", None))
        self.label_4.setText(QCoreApplication.translate("Gragh_show", u"\u91c7\u6837\u65f6\u957f: ", None))
        self.label_35.setText(QCoreApplication.translate("Gragh_show", u"s", None))
        self.label_10.setText(QCoreApplication.translate("Gragh_show", u"\u91c7\u96c6\u4f53\u79ef", None))
        self.label_20.setText(QCoreApplication.translate("Gragh_show", u"ml", None))
        self.label_6.setText(QCoreApplication.translate("Gragh_show", u"\u6837\u54c1\u4e2a\u6570", None))
        self.label_12.setText(QCoreApplication.translate("Gragh_show", u"\u52a0\u70ed\u6e29\u5ea6", None))
        self.label_19.setText(QCoreApplication.translate("Gragh_show", u"\u2103", None))
        self.label_9.setText(QCoreApplication.translate("Gragh_show", u"\u4fdd\u6301\u65f6\u95f4", None))
        self.label_11.setText(QCoreApplication.translate("Gragh_show", u"\u5f53\u524d\u5ba4\u6e29", None))
        self.label_21.setText(QCoreApplication.translate("Gragh_show", u"\u2103", None))
        self.label_13.setText(QCoreApplication.translate("Gragh_show", u"\u8fbe\u6e29\u65f6\u95f4", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Gragh_show", u"\u4f20\u611f\u5668\u5217\u8868", None))
        self.label_37.setText(QCoreApplication.translate("Gragh_show", u"\u5f53\u524d\u72b6\u6001:", None))
        self.statues_label.setText("")
        self.InitPos_Button.setText(QCoreApplication.translate("Gragh_show", u"\u521d\u59cb\u5316\u4f4d\u7f6e", None))
        self.Clear_Button.setText(QCoreApplication.translate("Gragh_show", u"\u57fa\u7ebf\u8c03\u6574", None))
        self.Collectbegin_Button.setText(QCoreApplication.translate("Gragh_show", u"\u5f00\u59cb\u91c7\u96c6", None))
        self.Pause_Button.setText(QCoreApplication.translate("Gragh_show", u"\u6682\u505c\u91c7\u96c6", None))
        self.Save_Button.setText(QCoreApplication.translate("Gragh_show", u"\u4fdd\u5b58\u6570\u636e", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Line_Show), QCoreApplication.translate("Gragh_show", u"\u66f2\u7ebf\u56fe", None))
    # retranslateUi

