# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QAbstractSpinBox, QApplication,
    QCheckBox, QComboBox, QCommandLinkButton, QFormLayout,
    QFrame, QGridLayout, QGroupBox, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPlainTextEdit, QPushButton, QRadioButton, QScrollArea,
    QScrollBar, QSizePolicy, QSlider, QSpacerItem,
    QSpinBox, QStackedWidget, QTabWidget, QTableView,
    QTableWidget, QTableWidgetItem, QTextBrowser, QTextEdit,
    QToolButton, QVBoxLayout, QWidget)
from .resources_rc import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setMinimumSize(QSize(940, 560))
        font = QFont()
        font.setFamilies([u"\u9ed1\u4f53"])
        MainWindow.setFont(font)
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        font1 = QFont()
        font1.setFamilies([u"\u5b8b\u4f53"])
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setItalic(False)
        self.styleSheet.setFont(font1)
        self.styleSheet.setStyleSheet(u"")
        self.appMargins = QVBoxLayout(self.styleSheet)
        self.appMargins.setSpacing(0)
        self.appMargins.setObjectName(u"appMargins")
        self.appMargins.setContentsMargins(10, 10, 10, 10)
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Raised)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(60, 0))
        self.leftMenuBg.setMaximumSize(QSize(60, 16777215))
        self.leftMenuBg.setFrameShape(QFrame.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.topLogoInfo = QFrame(self.leftMenuBg)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setMinimumSize(QSize(0, 50))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 50))
        self.topLogoInfo.setFrameShape(QFrame.NoFrame)
        self.topLogoInfo.setFrameShadow(QFrame.Raised)
        self.topLogo = QFrame(self.topLogoInfo)
        self.topLogo.setObjectName(u"topLogo")
        self.topLogo.setGeometry(QRect(10, 5, 42, 42))
        self.topLogo.setMinimumSize(QSize(42, 42))
        self.topLogo.setMaximumSize(QSize(42, 42))
        self.topLogo.setAutoFillBackground(False)
        self.topLogo.setStyleSheet(u"background-color: transparent;\n"
"background-image: url(:/images/images/images/Enose_50_50.png);\n"
"background-position: centered;\n"
"background-repeat: no-repeat;\n"
"")
        self.topLogo.setFrameShape(QFrame.NoFrame)
        self.topLogo.setFrameShadow(QFrame.Raised)
        self.titleLeftApp = QLabel(self.topLogoInfo)
        self.titleLeftApp.setObjectName(u"titleLeftApp")
        self.titleLeftApp.setGeometry(QRect(70, 15, 160, 20))
        self.titleLeftApp.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_3.addWidget(self.topLogoInfo)

        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setFrameShape(QFrame.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Raised)
        self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.toggleBox = QFrame(self.leftMenuFrame)
        self.toggleBox.setObjectName(u"toggleBox")
        self.toggleBox.setMaximumSize(QSize(16777215, 45))
        self.toggleBox.setFrameShape(QFrame.NoFrame)
        self.toggleBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.toggleBox)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.toggleButton = QPushButton(self.toggleBox)
        self.toggleButton.setObjectName(u"toggleButton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toggleButton.sizePolicy().hasHeightForWidth())
        self.toggleButton.setSizePolicy(sizePolicy)
        self.toggleButton.setMinimumSize(QSize(0, 45))
        font2 = QFont()
        font2.setFamilies([u"SimSun"])
        font2.setPointSize(10)
        font2.setBold(False)
        font2.setItalic(False)
        self.toggleButton.setFont(font2)
        self.toggleButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.toggleButton.setLayoutDirection(Qt.LeftToRight)
        self.toggleButton.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_menu.png);")

        self.verticalLayout_4.addWidget(self.toggleButton)


        self.verticalMenuLayout.addWidget(self.toggleBox)

        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setFrameShape(QFrame.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.topMenu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btn_serial = QPushButton(self.topMenu)
        self.btn_serial.setObjectName(u"btn_serial")
        sizePolicy.setHeightForWidth(self.btn_serial.sizePolicy().hasHeightForWidth())
        self.btn_serial.setSizePolicy(sizePolicy)
        self.btn_serial.setMinimumSize(QSize(0, 45))
        self.btn_serial.setFont(font2)
        self.btn_serial.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_serial.setLayoutDirection(Qt.LeftToRight)
        self.btn_serial.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-home.png);")

        self.verticalLayout_8.addWidget(self.btn_serial)

        self.btn_test = QPushButton(self.topMenu)
        self.btn_test.setObjectName(u"btn_test")
        sizePolicy.setHeightForWidth(self.btn_test.sizePolicy().hasHeightForWidth())
        self.btn_test.setSizePolicy(sizePolicy)
        self.btn_test.setMinimumSize(QSize(0, 45))
        self.btn_test.setFont(font2)
        self.btn_test.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_test.setLayoutDirection(Qt.LeftToRight)
        self.btn_test.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-gamepad.png);")

        self.verticalLayout_8.addWidget(self.btn_test)

        self.btn_alg = QPushButton(self.topMenu)
        self.btn_alg.setObjectName(u"btn_alg")
        sizePolicy.setHeightForWidth(self.btn_alg.sizePolicy().hasHeightForWidth())
        self.btn_alg.setSizePolicy(sizePolicy)
        self.btn_alg.setMinimumSize(QSize(0, 45))
        self.btn_alg.setFont(font2)
        self.btn_alg.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_alg.setLayoutDirection(Qt.LeftToRight)
        self.btn_alg.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-file.png);")

        self.verticalLayout_8.addWidget(self.btn_alg)

        self.btn_ai = QPushButton(self.topMenu)
        self.btn_ai.setObjectName(u"btn_ai")
        sizePolicy.setHeightForWidth(self.btn_ai.sizePolicy().hasHeightForWidth())
        self.btn_ai.setSizePolicy(sizePolicy)
        self.btn_ai.setMinimumSize(QSize(0, 45))
        self.btn_ai.setFont(font2)
        self.btn_ai.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_ai.setLayoutDirection(Qt.LeftToRight)
        self.btn_ai.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-save.png)")

        self.verticalLayout_8.addWidget(self.btn_ai)


        self.verticalMenuLayout.addWidget(self.topMenu, 0, Qt.AlignTop)

        self.bottomMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setFrameShape(QFrame.NoFrame)
        self.bottomMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)

        self.verticalMenuLayout.addWidget(self.bottomMenu)


        self.verticalLayout_3.addWidget(self.leftMenuFrame)


        self.appLayout.addWidget(self.leftMenuBg)

        self.extraLeftBox = QFrame(self.bgApp)
        self.extraLeftBox.setObjectName(u"extraLeftBox")
        self.extraLeftBox.setMinimumSize(QSize(0, 0))
        self.extraLeftBox.setMaximumSize(QSize(0, 16777215))
        self.extraLeftBox.setFrameShape(QFrame.NoFrame)
        self.extraLeftBox.setFrameShadow(QFrame.Raised)
        self.extraColumLayout = QVBoxLayout(self.extraLeftBox)
        self.extraColumLayout.setSpacing(0)
        self.extraColumLayout.setObjectName(u"extraColumLayout")
        self.extraColumLayout.setContentsMargins(0, 0, 0, 0)
        self.extraTopBg = QFrame(self.extraLeftBox)
        self.extraTopBg.setObjectName(u"extraTopBg")
        self.extraTopBg.setMinimumSize(QSize(0, 50))
        self.extraTopBg.setMaximumSize(QSize(16777215, 50))
        self.extraTopBg.setFrameShape(QFrame.NoFrame)
        self.extraTopBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.extraTopBg)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.extraTopLayout = QGridLayout()
        self.extraTopLayout.setObjectName(u"extraTopLayout")
        self.extraTopLayout.setHorizontalSpacing(10)
        self.extraTopLayout.setVerticalSpacing(0)
        self.extraTopLayout.setContentsMargins(10, -1, 10, -1)
        self.extraLabel = QLabel(self.extraTopBg)
        self.extraLabel.setObjectName(u"extraLabel")
        self.extraLabel.setMinimumSize(QSize(150, 0))

        self.extraTopLayout.addWidget(self.extraLabel, 0, 0, 1, 1)


        self.verticalLayout_5.addLayout(self.extraTopLayout)


        self.extraColumLayout.addWidget(self.extraTopBg)

        self.extraContent = QFrame(self.extraLeftBox)
        self.extraContent.setObjectName(u"extraContent")
        self.extraContent.setFrameShape(QFrame.NoFrame)
        self.extraContent.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.extraContent)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.extraTopMenu = QFrame(self.extraContent)
        self.extraTopMenu.setObjectName(u"extraTopMenu")
        self.extraTopMenu.setFrameShape(QFrame.NoFrame)
        self.extraTopMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.extraTopMenu)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.btn_share = QPushButton(self.extraTopMenu)
        self.btn_share.setObjectName(u"btn_share")
        sizePolicy.setHeightForWidth(self.btn_share.sizePolicy().hasHeightForWidth())
        self.btn_share.setSizePolicy(sizePolicy)
        self.btn_share.setMinimumSize(QSize(0, 45))
        self.btn_share.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_share.setLayoutDirection(Qt.LeftToRight)
        self.btn_share.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-share-boxed.png);")

        self.verticalLayout_11.addWidget(self.btn_share)

        self.btn_adjustments = QPushButton(self.extraTopMenu)
        self.btn_adjustments.setObjectName(u"btn_adjustments")
        sizePolicy.setHeightForWidth(self.btn_adjustments.sizePolicy().hasHeightForWidth())
        self.btn_adjustments.setSizePolicy(sizePolicy)
        self.btn_adjustments.setMinimumSize(QSize(0, 45))
        self.btn_adjustments.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_adjustments.setLayoutDirection(Qt.LeftToRight)
        self.btn_adjustments.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-equalizer.png);")

        self.verticalLayout_11.addWidget(self.btn_adjustments)

        self.btn_more = QPushButton(self.extraTopMenu)
        self.btn_more.setObjectName(u"btn_more")
        sizePolicy.setHeightForWidth(self.btn_more.sizePolicy().hasHeightForWidth())
        self.btn_more.setSizePolicy(sizePolicy)
        self.btn_more.setMinimumSize(QSize(0, 45))
        self.btn_more.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_more.setLayoutDirection(Qt.LeftToRight)
        self.btn_more.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-layers.png);")

        self.verticalLayout_11.addWidget(self.btn_more)


        self.verticalLayout_12.addWidget(self.extraTopMenu, 0, Qt.AlignTop)

        self.extraCenter = QFrame(self.extraContent)
        self.extraCenter.setObjectName(u"extraCenter")
        self.extraCenter.setFrameShape(QFrame.NoFrame)
        self.extraCenter.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.extraCenter)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.textEdit = QTextEdit(self.extraCenter)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(222, 0))
        self.textEdit.setStyleSheet(u"background: transparent;")
        self.textEdit.setFrameShape(QFrame.NoFrame)
        self.textEdit.setReadOnly(True)

        self.verticalLayout_10.addWidget(self.textEdit)


        self.verticalLayout_12.addWidget(self.extraCenter)

        self.extraBottom = QFrame(self.extraContent)
        self.extraBottom.setObjectName(u"extraBottom")
        self.extraBottom.setFrameShape(QFrame.NoFrame)
        self.extraBottom.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.extraBottom)


        self.extraColumLayout.addWidget(self.extraContent)


        self.appLayout.addWidget(self.extraLeftBox)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.contentTopBg.setFrameShape(QFrame.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy1)
        self.leftBox.setFrameShape(QFrame.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy2)
        self.titleRightInfo.setMaximumSize(QSize(16777215, 45))
        font3 = QFont()
        font3.setFamilies([u"\u5b8b\u4f53"])
        font3.setPointSize(14)
        font3.setBold(False)
        font3.setItalic(False)
        self.titleRightInfo.setFont(font3)
        self.titleRightInfo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.titleRightInfo.setMargin(0)
        self.titleRightInfo.setIndent(2)

        self.horizontalLayout_3.addWidget(self.titleRightInfo)


        self.horizontalLayout.addWidget(self.leftBox)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.rightButtons.setFrameShape(QFrame.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.settingsTopBtn = QPushButton(self.rightButtons)
        self.settingsTopBtn.setObjectName(u"settingsTopBtn")
        self.settingsTopBtn.setMinimumSize(QSize(28, 28))
        self.settingsTopBtn.setMaximumSize(QSize(28, 28))
        self.settingsTopBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/icon_settings.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.settingsTopBtn.setIcon(icon)
        self.settingsTopBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.settingsTopBtn)

        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.minimizeAppBtn.setIcon(icon1)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.minimizeAppBtn)

        self.maximizeRestoreAppBtn = QPushButton(self.rightButtons)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.maximizeRestoreAppBtn.setMinimumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setMaximumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/icon_maximize.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.maximizeRestoreAppBtn.setIcon(icon2)
        self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.maximizeRestoreAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.closeAppBtn.setIcon(icon3)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.closeAppBtn)


        self.horizontalLayout.addWidget(self.rightButtons, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.contentTopBg)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setFrameShape(QFrame.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        font4 = QFont()
        font4.setFamilies([u"\u5b8b\u4f53"])
        font4.setPointSize(9)
        font4.setBold(False)
        font4.setItalic(False)
        self.pagesContainer.setFont(font4)
        self.pagesContainer.setStyleSheet(u"")
        self.pagesContainer.setFrameShape(QFrame.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.pagesContainer)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(10, 10, 10, 10)
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setLayoutDirection(Qt.LeftToRight)
        self.stackedWidget.setStyleSheet(u"")
        self.serial = QWidget()
        self.serial.setObjectName(u"serial")
        self.serial.setMinimumSize(QSize(110, 110))
        self.serial.setLayoutDirection(Qt.LeftToRight)
        self.serial.setStyleSheet(u"")
        self.horizontalLayout_6 = QHBoxLayout(self.serial)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.groupBox = QGroupBox(self.serial)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy3)
        self.formLayout = QFormLayout(self.groupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_2)

        self.CheckButton = QPushButton(self.groupBox)
        self.CheckButton.setObjectName(u"CheckButton")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.CheckButton)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_5)

        self.serialComboBox = QComboBox(self.groupBox)
        self.serialComboBox.setObjectName(u"serialComboBox")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.serialComboBox)

        self.statues = QLabel(self.groupBox)
        self.statues.setObjectName(u"statues")
        self.statues.setTextFormat(Qt.AutoText)

        self.formLayout.setWidget(2, QFormLayout.ItemRole.SpanningRole, self.statues)

        self.connectButton = QPushButton(self.groupBox)
        self.connectButton.setObjectName(u"connectButton")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.SpanningRole, self.connectButton)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.formLayout.setItem(3, QFormLayout.ItemRole.LabelRole, self.verticalSpacer)


        self.verticalLayout_21.addWidget(self.groupBox)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.sendEdit = QLineEdit(self.serial)
        self.sendEdit.setObjectName(u"sendEdit")

        self.horizontalLayout_7.addWidget(self.sendEdit)

        self.sendButton = QPushButton(self.serial)
        self.sendButton.setObjectName(u"sendButton")

        self.horizontalLayout_7.addWidget(self.sendButton)


        self.verticalLayout_21.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.saveButton = QPushButton(self.serial)
        self.saveButton.setObjectName(u"saveButton")

        self.horizontalLayout_8.addWidget(self.saveButton)

        self.clearButton = QPushButton(self.serial)
        self.clearButton.setObjectName(u"clearButton")

        self.horizontalLayout_8.addWidget(self.clearButton)


        self.verticalLayout_21.addLayout(self.horizontalLayout_8)

        self.verticalLayout_21.setStretch(0, 7)
        self.verticalLayout_21.setStretch(2, 1)

        self.horizontalLayout_6.addLayout(self.verticalLayout_21)

        self.tb = QTextBrowser(self.serial)
        self.tb.setObjectName(u"tb")

        self.horizontalLayout_6.addWidget(self.tb)

        self.horizontalLayout_6.setStretch(0, 1)
        self.horizontalLayout_6.setStretch(1, 2)
        self.stackedWidget.addWidget(self.serial)
        self.owner = QWidget()
        self.owner.setObjectName(u"owner")
        self.owner.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.owner)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.row_1 = QFrame(self.owner)
        self.row_1.setObjectName(u"row_1")
        self.row_1.setFrameShape(QFrame.StyledPanel)
        self.row_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.row_1)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_div_content_1 = QFrame(self.row_1)
        self.frame_div_content_1.setObjectName(u"frame_div_content_1")
        self.frame_div_content_1.setMinimumSize(QSize(0, 110))
        self.frame_div_content_1.setMaximumSize(QSize(16777215, 110))
        self.frame_div_content_1.setFrameShape(QFrame.NoFrame)
        self.frame_div_content_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_div_content_1)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_title_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_title_wid_1.setObjectName(u"frame_title_wid_1")
        self.frame_title_wid_1.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_1.setFrameShape(QFrame.StyledPanel)
        self.frame_title_wid_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_title_wid_1)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.labelBoxBlenderInstalation = QLabel(self.frame_title_wid_1)
        self.labelBoxBlenderInstalation.setObjectName(u"labelBoxBlenderInstalation")
        font5 = QFont()
        font5.setFamilies([u"Segoe UI"])
        font5.setPointSize(10)
        font5.setBold(False)
        font5.setItalic(False)
        self.labelBoxBlenderInstalation.setFont(font5)
        self.labelBoxBlenderInstalation.setStyleSheet(u"")

        self.verticalLayout_18.addWidget(self.labelBoxBlenderInstalation)


        self.verticalLayout_17.addWidget(self.frame_title_wid_1)

        self.frame_content_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_content_wid_1.setObjectName(u"frame_content_wid_1")
        self.frame_content_wid_1.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_content_wid_1)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, -1, -1, 0)
        self.labelVersion_3 = QLabel(self.frame_content_wid_1)
        self.labelVersion_3.setObjectName(u"labelVersion_3")
        self.labelVersion_3.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_3.setLineWidth(1)
        self.labelVersion_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.labelVersion_3, 1, 0, 1, 2)

        self.pushButton = QPushButton(self.frame_content_wid_1)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(150, 30))
        self.pushButton.setFont(font5)
        self.pushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton.setStyleSheet(u"")
        icon4 = QIcon()
        icon4.addFile(u":/icons/images/icons/cil-folder-open.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon4)

        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)

        self.lineEdit = QLineEdit(self.frame_content_wid_1)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 30))
        self.lineEdit.setStyleSheet(u"")

        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)


        self.horizontalLayout_9.addLayout(self.gridLayout)


        self.verticalLayout_17.addWidget(self.frame_content_wid_1)


        self.verticalLayout_16.addWidget(self.frame_div_content_1)


        self.verticalLayout.addWidget(self.row_1)

        self.row_2 = QFrame(self.owner)
        self.row_2.setObjectName(u"row_2")
        self.row_2.setMinimumSize(QSize(0, 150))
        self.row_2.setFrameShape(QFrame.StyledPanel)
        self.row_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.row_2)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.commandLinkButton = QCommandLinkButton(self.row_2)
        self.commandLinkButton.setObjectName(u"commandLinkButton")
        self.commandLinkButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.commandLinkButton.setStyleSheet(u"")
        icon5 = QIcon()
        icon5.addFile(u":/icons/images/icons/cil-link.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.commandLinkButton.setIcon(icon5)

        self.gridLayout_2.addWidget(self.commandLinkButton, 1, 6, 1, 1)

        self.radioButton = QRadioButton(self.row_2)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.radioButton, 0, 1, 1, 1)

        self.scrollArea = QScrollArea(self.row_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 218, 218))
        self.scrollAreaWidgetContents.setStyleSheet(u" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }")
        self.horizontalLayout_11 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.plainTextEdit = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setMinimumSize(QSize(200, 200))
        self.plainTextEdit.setStyleSheet(u"")

        self.horizontalLayout_11.addWidget(self.plainTextEdit)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_2.addWidget(self.scrollArea, 0, 5, 3, 1)

        self.checkBox = QCheckBox(self.row_2)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setAutoFillBackground(False)
        self.checkBox.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.checkBox, 0, 0, 1, 1)

        self.verticalScrollBar = QScrollBar(self.row_2)
        self.verticalScrollBar.setObjectName(u"verticalScrollBar")
        self.verticalScrollBar.setStyleSheet(u"")
        self.verticalScrollBar.setOrientation(Qt.Vertical)

        self.gridLayout_2.addWidget(self.verticalScrollBar, 0, 4, 3, 1)

        self.horizontalScrollBar = QScrollBar(self.row_2)
        self.horizontalScrollBar.setObjectName(u"horizontalScrollBar")
        sizePolicy.setHeightForWidth(self.horizontalScrollBar.sizePolicy().hasHeightForWidth())
        self.horizontalScrollBar.setSizePolicy(sizePolicy)
        self.horizontalScrollBar.setStyleSheet(u"")
        self.horizontalScrollBar.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.horizontalScrollBar, 1, 3, 1, 1)

        self.comboBox = QComboBox(self.row_2)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setFont(font5)
        self.comboBox.setAutoFillBackground(False)
        self.comboBox.setStyleSheet(u"")
        self.comboBox.setIconSize(QSize(16, 16))
        self.comboBox.setFrame(True)

        self.gridLayout_2.addWidget(self.comboBox, 1, 0, 1, 2)

        self.horizontalSlider = QSlider(self.row_2)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setStyleSheet(u"")
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.horizontalSlider, 2, 0, 1, 2)

        self.verticalSlider = QSlider(self.row_2)
        self.verticalSlider.setObjectName(u"verticalSlider")
        self.verticalSlider.setStyleSheet(u"")
        self.verticalSlider.setOrientation(Qt.Vertical)

        self.gridLayout_2.addWidget(self.verticalSlider, 0, 2, 3, 1)


        self.verticalLayout_19.addLayout(self.gridLayout_2)


        self.verticalLayout.addWidget(self.row_2)

        self.row_3 = QFrame(self.owner)
        self.row_3.setObjectName(u"row_3")
        self.row_3.setMinimumSize(QSize(0, 150))
        self.row_3.setFrameShape(QFrame.StyledPanel)
        self.row_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.row_3)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.tableWidget = QTableWidget(self.row_3)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.tableWidget.rowCount() < 16):
            self.tableWidget.setRowCount(16)
        font6 = QFont()
        font6.setFamilies([u"Segoe UI"])
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font6);
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(12, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(13, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(14, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(15, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget.setItem(0, 2, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget.setItem(0, 3, __qtablewidgetitem23)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy4)
        palette = QPalette()
        brush = QBrush(QColor(221, 221, 221, 255))
        brush.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 0))
        brush1.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush1)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ButtonText, brush)
        brush2 = QBrush(QColor(0, 0, 0, 255))
        brush2.setStyle(Qt.BrushStyle.NoBrush)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush2)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush)
#endif
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush1)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ButtonText, brush)
        brush3 = QBrush(QColor(0, 0, 0, 255))
        brush3.setStyle(Qt.BrushStyle.NoBrush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush3)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.PlaceholderText, brush)
#endif
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush1)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, brush)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, brush)
        brush4 = QBrush(QColor(0, 0, 0, 255))
        brush4.setStyle(Qt.BrushStyle.NoBrush)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush4)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush)
#endif
        self.tableWidget.setPalette(palette)
        self.tableWidget.setFrameShape(QFrame.NoFrame)
        self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(Qt.SolidLine)
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setHighlightSections(False)
        self.tableWidget.verticalHeader().setStretchLastSection(True)

        self.horizontalLayout_12.addWidget(self.tableWidget)


        self.verticalLayout.addWidget(self.row_3)

        self.stackedWidget.addWidget(self.owner)
        self.test = QWidget()
        self.test.setObjectName(u"test")
        self.horizontalLayout_30 = QHBoxLayout(self.test)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.groupBox_2 = QGroupBox(self.test)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setFlat(False)
        self.groupBox_2.setCheckable(False)
        self.verticalLayout_15 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(3, -1, 3, -1)
        self.groupBox_3 = QGroupBox(self.groupBox_2)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.horizontalLayout_13 = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.Folder_lineEdit = QLineEdit(self.groupBox_3)
        self.Folder_lineEdit.setObjectName(u"Folder_lineEdit")

        self.horizontalLayout_13.addWidget(self.Folder_lineEdit)

        self.Folder_Button = QToolButton(self.groupBox_3)
        self.Folder_Button.setObjectName(u"Folder_Button")

        self.horizontalLayout_13.addWidget(self.Folder_Button)


        self.verticalLayout_15.addWidget(self.groupBox_3)

        self.groupBox_4 = QGroupBox(self.groupBox_2)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout_22 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_3 = QLabel(self.groupBox_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_14.addWidget(self.label_3)

        self.Cleartime_spinBox = QSpinBox(self.groupBox_4)
        self.Cleartime_spinBox.setObjectName(u"Cleartime_spinBox")
        self.Cleartime_spinBox.setFocusPolicy(Qt.WheelFocus)
        self.Cleartime_spinBox.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.Cleartime_spinBox.setMinimum(10)
        self.Cleartime_spinBox.setMaximum(256)
        self.Cleartime_spinBox.setValue(10)

        self.horizontalLayout_14.addWidget(self.Cleartime_spinBox)

        self.label_34 = QLabel(self.groupBox_4)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_14.addWidget(self.label_34)

        self.label_4 = QLabel(self.groupBox_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_14.addWidget(self.label_4)

        self.Sample_spinBox = QSpinBox(self.groupBox_4)
        self.Sample_spinBox.setObjectName(u"Sample_spinBox")
        self.Sample_spinBox.setFocusPolicy(Qt.WheelFocus)
        self.Sample_spinBox.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.Sample_spinBox.setMinimum(0)
        self.Sample_spinBox.setMaximum(256)
        self.Sample_spinBox.setValue(10)

        self.horizontalLayout_14.addWidget(self.Sample_spinBox)

        self.label_35 = QLabel(self.groupBox_4)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_14.addWidget(self.label_35)

        self.horizontalLayout_14.setStretch(0, 3)
        self.horizontalLayout_14.setStretch(1, 2)
        self.horizontalLayout_14.setStretch(2, 1)
        self.horizontalLayout_14.setStretch(3, 3)
        self.horizontalLayout_14.setStretch(4, 2)
        self.horizontalLayout_14.setStretch(5, 1)

        self.verticalLayout_22.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_9 = QLabel(self.groupBox_4)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_15.addWidget(self.label_9)

        self.Basetime_spinBox = QSpinBox(self.groupBox_4)
        self.Basetime_spinBox.setObjectName(u"Basetime_spinBox")
        self.Basetime_spinBox.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.Basetime_spinBox.setMinimum(1)
        self.Basetime_spinBox.setMaximum(60)
        self.Basetime_spinBox.setValue(1)
        self.Basetime_spinBox.setDisplayIntegerBase(10)

        self.horizontalLayout_15.addWidget(self.Basetime_spinBox)

        self.label_36 = QLabel(self.groupBox_4)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_15.addWidget(self.label_36)

        self.label_14 = QLabel(self.groupBox_4)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_15.addWidget(self.label_14)

        self.Worktime_spinBox = QSpinBox(self.groupBox_4)
        self.Worktime_spinBox.setObjectName(u"Worktime_spinBox")
        self.Worktime_spinBox.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.Worktime_spinBox.setMinimum(1)
        self.Worktime_spinBox.setMaximum(65535)
        self.Worktime_spinBox.setValue(1)
        self.Worktime_spinBox.setDisplayIntegerBase(10)

        self.horizontalLayout_15.addWidget(self.Worktime_spinBox)

        self.horizontalLayout_15.setStretch(0, 3)
        self.horizontalLayout_15.setStretch(1, 2)
        self.horizontalLayout_15.setStretch(2, 1)
        self.horizontalLayout_15.setStretch(3, 3)
        self.horizontalLayout_15.setStretch(4, 3)

        self.verticalLayout_22.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.Auto_Button = QPushButton(self.groupBox_4)
        self.Auto_Button.setObjectName(u"Auto_Button")
        self.Auto_Button.setMaximumSize(QSize(200, 60))

        self.horizontalLayout_16.addWidget(self.Auto_Button)

        self.InitPos_Button = QPushButton(self.groupBox_4)
        self.InitPos_Button.setObjectName(u"InitPos_Button")
        self.InitPos_Button.setMaximumSize(QSize(200, 60))

        self.horizontalLayout_16.addWidget(self.InitPos_Button)


        self.verticalLayout_22.addLayout(self.horizontalLayout_16)


        self.verticalLayout_15.addWidget(self.groupBox_4)

        self.groupBox_5 = QGroupBox(self.groupBox_2)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.gridLayout_4 = QGridLayout(self.groupBox_5)
        self.gridLayout_4.setSpacing(1)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(9, 9, 9, 9)
        self.Senser_stableView = QTableView(self.groupBox_5)
        self.Senser_stableView.setObjectName(u"Senser_stableView")
        self.Senser_stableView.setMinimumSize(QSize(226, 0))
        self.Senser_stableView.setMaximumSize(QSize(1600, 16777215))
        self.Senser_stableView.horizontalHeader().setVisible(False)
        self.Senser_stableView.verticalHeader().setHighlightSections(True)

        self.gridLayout_4.addWidget(self.Senser_stableView, 0, 0, 1, 1)


        self.verticalLayout_15.addWidget(self.groupBox_5)

        self.verticalLayout_15.setStretch(2, 10)

        self.horizontalLayout_30.addWidget(self.groupBox_2)

        self.verticalLayout_31 = QVBoxLayout()
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_30 = QVBoxLayout()
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_40 = QLabel(self.test)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setLayoutDirection(Qt.LeftToRight)
        self.label_40.setTextFormat(Qt.AutoText)
        self.label_40.setScaledContents(False)

        self.horizontalLayout_19.addWidget(self.label_40)

        self.statues_label = QLabel(self.test)
        self.statues_label.setObjectName(u"statues_label")

        self.horizontalLayout_19.addWidget(self.statues_label)

        self.Clear_Button = QPushButton(self.test)
        self.Clear_Button.setObjectName(u"Clear_Button")
        self.Clear_Button.setMaximumSize(QSize(150, 60))

        self.horizontalLayout_19.addWidget(self.Clear_Button)

        self.Collectbegin_Button = QPushButton(self.test)
        self.Collectbegin_Button.setObjectName(u"Collectbegin_Button")
        self.Collectbegin_Button.setMaximumSize(QSize(150, 60))

        self.horizontalLayout_19.addWidget(self.Collectbegin_Button)

        self.Clearroom_Button = QPushButton(self.test)
        self.Clearroom_Button.setObjectName(u"Clearroom_Button")
        self.Clearroom_Button.setMaximumSize(QSize(150, 60))

        self.horizontalLayout_19.addWidget(self.Clearroom_Button)

        self.Stop_Button_3 = QPushButton(self.test)
        self.Stop_Button_3.setObjectName(u"Stop_Button_3")
        self.Stop_Button_3.setMaximumSize(QSize(150, 60))

        self.horizontalLayout_19.addWidget(self.Stop_Button_3)

        self.horizontalLayout_19.setStretch(0, 1)
        self.horizontalLayout_19.setStretch(1, 10)
        self.horizontalLayout_19.setStretch(2, 1)
        self.horizontalLayout_19.setStretch(3, 1)
        self.horizontalLayout_19.setStretch(4, 1)
        self.horizontalLayout_19.setStretch(5, 1)

        self.verticalLayout_30.addLayout(self.horizontalLayout_19)


        self.verticalLayout_31.addLayout(self.verticalLayout_30)

        self.tabWidget = QTabWidget(self.test)
        self.tabWidget.setObjectName(u"tabWidget")
        self.Line_Show = QWidget()
        self.Line_Show.setObjectName(u"Line_Show")
        self.gridLayout_3 = QGridLayout(self.Line_Show)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.Linegragh_Layout = QVBoxLayout()
        self.Linegragh_Layout.setObjectName(u"Linegragh_Layout")

        self.gridLayout_3.addLayout(self.Linegragh_Layout, 0, 0, 1, 1)

        self.tabWidget.addTab(self.Line_Show, "")

        self.verticalLayout_31.addWidget(self.tabWidget)


        self.horizontalLayout_30.addLayout(self.verticalLayout_31)

        self.horizontalLayout_30.setStretch(0, 1)
        self.horizontalLayout_30.setStretch(1, 3)
        self.stackedWidget.addWidget(self.test)
        self.alg = QWidget()
        self.alg.setObjectName(u"alg")
        self.horizontalLayout_38 = QHBoxLayout(self.alg)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.gridLayout_12 = QGridLayout()
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.widget_2 = QWidget(self.alg)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_36 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_36.setContentsMargins(-1, 0, -1, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_36.addItem(self.horizontalSpacer)

        self.Begin_Button = QPushButton(self.widget_2)
        self.Begin_Button.setObjectName(u"Begin_Button")
        self.Begin_Button.setMaximumSize(QSize(100, 32))

        self.horizontalLayout_36.addWidget(self.Begin_Button)


        self.gridLayout_12.addWidget(self.widget_2, 0, 1, 1, 1)

        self.tabWidget_4 = QTabWidget(self.alg)
        self.tabWidget_4.setObjectName(u"tabWidget_4")

        self.gridLayout_12.addWidget(self.tabWidget_4, 1, 1, 1, 1)

        self.groupBox_15 = QGroupBox(self.alg)
        self.groupBox_15.setObjectName(u"groupBox_15")
        font7 = QFont()
        font7.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font7.setPointSize(10)
        font7.setBold(False)
        font7.setItalic(False)
        self.groupBox_15.setFont(font7)
        self.groupBox_15.setFlat(False)
        self.groupBox_15.setCheckable(False)
        self.verticalLayout_34 = QVBoxLayout(self.groupBox_15)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.horizontalLayout_37 = QHBoxLayout()
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.label = QLabel(self.groupBox_15)
        self.label.setObjectName(u"label")

        self.horizontalLayout_37.addWidget(self.label)

        self.FilePath_lineEdit = QLineEdit(self.groupBox_15)
        self.FilePath_lineEdit.setObjectName(u"FilePath_lineEdit")

        self.horizontalLayout_37.addWidget(self.FilePath_lineEdit)

        self.toolButton = QToolButton(self.groupBox_15)
        self.toolButton.setObjectName(u"toolButton")

        self.horizontalLayout_37.addWidget(self.toolButton)


        self.verticalLayout_34.addLayout(self.horizontalLayout_37)

        self.groupBox_16 = QGroupBox(self.groupBox_15)
        self.groupBox_16.setObjectName(u"groupBox_16")
        self.gridLayout_13 = QGridLayout(self.groupBox_16)
        self.gridLayout_13.setSpacing(3)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setContentsMargins(-1, -1, -1, 3)
        self.Reg_ComboBox = QComboBox(self.groupBox_16)
        self.Reg_ComboBox.setObjectName(u"Reg_ComboBox")

        self.gridLayout_13.addWidget(self.Reg_ComboBox, 5, 1, 1, 1)

        self.label_18 = QLabel(self.groupBox_16)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout_13.addWidget(self.label_18, 1, 0, 1, 1)

        self.Classify_ComboBox = QComboBox(self.groupBox_16)
        self.Classify_ComboBox.setObjectName(u"Classify_ComboBox")

        self.gridLayout_13.addWidget(self.Classify_ComboBox, 7, 1, 1, 1)

        self.label_19 = QLabel(self.groupBox_16)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout_13.addWidget(self.label_19, 5, 0, 1, 1)

        self.label_20 = QLabel(self.groupBox_16)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout_13.addWidget(self.label_20, 3, 0, 1, 1)

        self.label_21 = QLabel(self.groupBox_16)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout_13.addWidget(self.label_21, 7, 0, 1, 1)

        self.Dimension_ComboBox = QComboBox(self.groupBox_16)
        self.Dimension_ComboBox.setObjectName(u"Dimension_ComboBox")

        self.gridLayout_13.addWidget(self.Dimension_ComboBox, 3, 1, 1, 1)

        self.Pre_Button = QPushButton(self.groupBox_16)
        self.Pre_Button.setObjectName(u"Pre_Button")

        self.gridLayout_13.addWidget(self.Pre_Button, 1, 1, 1, 1)

        self.gridLayout_13.setColumnStretch(0, 1)
        self.gridLayout_13.setColumnStretch(1, 2)

        self.verticalLayout_34.addWidget(self.groupBox_16)

        self.groupBox_17 = QGroupBox(self.groupBox_15)
        self.groupBox_17.setObjectName(u"groupBox_17")
        self.gridLayout_14 = QGridLayout(self.groupBox_17)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.textBrowser = QTextBrowser(self.groupBox_17)
        self.textBrowser.setObjectName(u"textBrowser")

        self.gridLayout_14.addWidget(self.textBrowser, 0, 0, 1, 1)


        self.verticalLayout_34.addWidget(self.groupBox_17)

        self.verticalLayout_34.setStretch(1, 1)
        self.verticalLayout_34.setStretch(2, 4)

        self.gridLayout_12.addWidget(self.groupBox_15, 0, 0, 2, 1)

        self.gridLayout_12.setColumnStretch(0, 1)
        self.gridLayout_12.setColumnStretch(1, 4)

        self.horizontalLayout_38.addLayout(self.gridLayout_12)

        self.stackedWidget.addWidget(self.alg)

        self.horizontalLayout_10.addWidget(self.stackedWidget)


        self.horizontalLayout_4.addWidget(self.pagesContainer)

        self.extraRightBox = QFrame(self.content)
        self.extraRightBox.setObjectName(u"extraRightBox")
        self.extraRightBox.setMinimumSize(QSize(0, 0))
        self.extraRightBox.setMaximumSize(QSize(0, 16777215))
        self.extraRightBox.setFrameShape(QFrame.NoFrame)
        self.extraRightBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.extraRightBox)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.themeSettingsTopDetail = QFrame(self.extraRightBox)
        self.themeSettingsTopDetail.setObjectName(u"themeSettingsTopDetail")
        self.themeSettingsTopDetail.setMaximumSize(QSize(16777215, 3))
        self.themeSettingsTopDetail.setFrameShape(QFrame.NoFrame)
        self.themeSettingsTopDetail.setFrameShadow(QFrame.Raised)

        self.verticalLayout_7.addWidget(self.themeSettingsTopDetail)

        self.contentSettings = QFrame(self.extraRightBox)
        self.contentSettings.setObjectName(u"contentSettings")
        self.contentSettings.setFrameShape(QFrame.NoFrame)
        self.contentSettings.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.contentSettings)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.topMenus = QFrame(self.contentSettings)
        self.topMenus.setObjectName(u"topMenus")
        self.topMenus.setFrameShape(QFrame.NoFrame)
        self.topMenus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.topMenus)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.btn_message = QPushButton(self.topMenus)
        self.btn_message.setObjectName(u"btn_message")
        sizePolicy.setHeightForWidth(self.btn_message.sizePolicy().hasHeightForWidth())
        self.btn_message.setSizePolicy(sizePolicy)
        self.btn_message.setMinimumSize(QSize(0, 45))
        self.btn_message.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_message.setLayoutDirection(Qt.LeftToRight)
        self.btn_message.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-envelope-open.png);")

        self.verticalLayout_14.addWidget(self.btn_message)

        self.btn_print = QPushButton(self.topMenus)
        self.btn_print.setObjectName(u"btn_print")
        sizePolicy.setHeightForWidth(self.btn_print.sizePolicy().hasHeightForWidth())
        self.btn_print.setSizePolicy(sizePolicy)
        self.btn_print.setMinimumSize(QSize(0, 45))
        self.btn_print.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_print.setLayoutDirection(Qt.LeftToRight)
        self.btn_print.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-print.png);")

        self.verticalLayout_14.addWidget(self.btn_print)

        self.btn_logout = QPushButton(self.topMenus)
        self.btn_logout.setObjectName(u"btn_logout")
        sizePolicy.setHeightForWidth(self.btn_logout.sizePolicy().hasHeightForWidth())
        self.btn_logout.setSizePolicy(sizePolicy)
        self.btn_logout.setMinimumSize(QSize(0, 45))
        self.btn_logout.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_logout.setLayoutDirection(Qt.LeftToRight)
        self.btn_logout.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-account-logout.png);")

        self.verticalLayout_14.addWidget(self.btn_logout)


        self.verticalLayout_13.addWidget(self.topMenus, 0, Qt.AlignTop)


        self.verticalLayout_7.addWidget(self.contentSettings)


        self.horizontalLayout_4.addWidget(self.extraRightBox)


        self.verticalLayout_6.addWidget(self.content)

        self.bottomBar = QFrame(self.contentBottom)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 22))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setFrameShape(QFrame.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.creditsLabel = QLabel(self.bottomBar)
        self.creditsLabel.setObjectName(u"creditsLabel")
        self.creditsLabel.setMaximumSize(QSize(16777215, 16))
        self.creditsLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.creditsLabel)

        self.version = QLabel(self.bottomBar)
        self.version.setObjectName(u"version")
        self.version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.version)

        self.frame_size_grip = QFrame(self.bottomBar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_size_grip)


        self.verticalLayout_6.addWidget(self.bottomBar)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.appLayout.addWidget(self.contentBox)


        self.appMargins.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_4.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titleLeftApp.setText(QCoreApplication.translate("MainWindow", u"\u5b9e\u9a8c\u5e73\u53f0", None))
        self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"\u9690\u85cf\u6807\u7b7e", None))
        self.btn_serial.setText(QCoreApplication.translate("MainWindow", u"\u4e32\u53e3\u8bbe\u7f6e", None))
        self.btn_test.setText(QCoreApplication.translate("MainWindow", u"\u6d4b\u8bd5\u9636\u6bb5", None))
        self.btn_alg.setText(QCoreApplication.translate("MainWindow", u"\u7b97\u6cd5\u9009\u62e9", None))
        self.btn_ai.setText(QCoreApplication.translate("MainWindow", u"\u5927\u6a21\u578b", None))
        self.extraLabel.setText(QCoreApplication.translate("MainWindow", u"Left Box", None))
        self.btn_share.setText(QCoreApplication.translate("MainWindow", u"Share", None))
        self.btn_adjustments.setText(QCoreApplication.translate("MainWindow", u"Adjustments", None))
        self.btn_more.setText(QCoreApplication.translate("MainWindow", u"More", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'SimSun'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:12pt; font-weight:600; color:#ff79c6;\">PyDracula</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:10pt; color:#ffffff;\">An interface created using Python and PySide (support for PyQt), and with colors based on the Dracula theme created by Zeno Rocha.</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0p"
                        "x; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:10pt; color:#ffffff;\">MIT License</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:10pt; color:#bd93f9;\">Created by: Wanderson M. Pimenta</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:12pt; font-weight:600; color:#ff79c6;\">Convert UI</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; color:#ffffff;\">pyside6-uic main.ui &gt; ui_main.py</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt"
                        "-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:12pt; font-weight:600; color:#ff79c6;\">Convert QRC</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; color:#ffffff;\">pyside6-rcc resources.qrc -o resources_rc.py</span></p></body></html>", None))
        self.titleRightInfo.setText(QCoreApplication.translate("MainWindow", u"\u667a\u80fd\u7535\u5b50\u9f3b\u5b9e\u9a8c\u53ca\u7b97\u6cd5\u5e73\u53f0", None))
#if QT_CONFIG(tooltip)
        self.settingsTopBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Settings", None))
#endif // QT_CONFIG(tooltip)
        self.settingsTopBtn.setText("")
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u4e32\u53e3\u8bbe\u7f6e", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u4e32\u53e3\u68c0\u6d4b", None))
        self.CheckButton.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u68c0\u6d4b", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">\u4fe1\u53f7\u4e32\u53e3</p></body></html>", None))
        self.statues.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#ff0000;\"><br/></span></p></body></html>", None))
        self.connectButton.setText(QCoreApplication.translate("MainWindow", u"\u8fde\u63a5", None))
        self.sendButton.setText(QCoreApplication.translate("MainWindow", u"\u53d1\u9001", None))
        self.saveButton.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u4e3a\u6587\u4ef6", None))
        self.clearButton.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u7a7a\u8f93\u51fa", None))
        self.labelBoxBlenderInstalation.setText(QCoreApplication.translate("MainWindow", u"FILE BOX", None))
        self.labelVersion_3.setText(QCoreApplication.translate("MainWindow", u"Label description", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here", None))
        self.commandLinkButton.setText(QCoreApplication.translate("MainWindow", u"Link Button", None))
        self.commandLinkButton.setDescription(QCoreApplication.translate("MainWindow", u"Link description", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Test 1", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Test 2", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Test 3", None))

        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem4 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem5 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem6 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem7 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem8 = self.tableWidget.verticalHeaderItem(4)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem9 = self.tableWidget.verticalHeaderItem(5)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem10 = self.tableWidget.verticalHeaderItem(6)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem11 = self.tableWidget.verticalHeaderItem(7)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem12 = self.tableWidget.verticalHeaderItem(8)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem13 = self.tableWidget.verticalHeaderItem(9)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem14 = self.tableWidget.verticalHeaderItem(10)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem15 = self.tableWidget.verticalHeaderItem(11)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem16 = self.tableWidget.verticalHeaderItem(12)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem17 = self.tableWidget.verticalHeaderItem(13)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem18 = self.tableWidget.verticalHeaderItem(14)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem19 = self.tableWidget.verticalHeaderItem(15)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"New Row", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem20 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Test", None));
        ___qtablewidgetitem21 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Text", None));
        ___qtablewidgetitem22 = self.tableWidget.item(0, 2)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Cell", None));
        ___qtablewidgetitem23 = self.tableWidget.item(0, 3)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Line", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u5b9e\u9a8c\u4fe1\u606f", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u8def\u5f84", None))
        self.Folder_Button.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"\u91c7\u6837\u8bbe\u7f6e", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u6d17\u6c14\u65f6\u957f", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"s", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u91c7\u6837\u65f6\u957f: ", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"s", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u57fa\u7ebf\u65f6\u957f", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"s", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\u5de5\u4f5c\u65f6\u95f4", None))
        self.Auto_Button.setText(QCoreApplication.translate("MainWindow", u"\u81ea\u52a8\u6a21\u5f0f", None))
        self.InitPos_Button.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb/\u521d\u59cb\u5316", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"\u4f20\u611f\u5668\u5217\u8868", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"\u5f53\u524d\u72b6\u6001:", None))
        self.statues_label.setText("")
        self.Clear_Button.setText(QCoreApplication.translate("MainWindow", u"\u57fa\u7ebf\u8c03\u6574", None))
        self.Collectbegin_Button.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u91c7\u96c6", None))
        self.Clearroom_Button.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u6d17\u6c14\u5ba4", None))
        self.Stop_Button_3.setText(QCoreApplication.translate("MainWindow", u"\u4e00\u952e\u6682\u505c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Line_Show), QCoreApplication.translate("MainWindow", u"\u66f2\u7ebf\u56fe", None))
        self.Begin_Button.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u5904\u7406", None))
        self.groupBox_15.setTitle(QCoreApplication.translate("MainWindow", u"\u5b9e\u9a8c\u4fe1\u606f", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u8def\u5f84", None))
        self.toolButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.groupBox_16.setTitle(QCoreApplication.translate("MainWindow", u"\u7b97\u6cd5\u9009\u62e9", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"\u9884\u5904\u7406", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"\u56de\u5f52\u9884\u6d4b", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"\u964d\u7ef4\u7b97\u6cd5", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"\u5206\u7c7b\u7b97\u6cd5", None))
        self.Pre_Button.setText(QCoreApplication.translate("MainWindow", u"\u7b97\u6cd5\u9009\u62e9", None))
        self.groupBox_17.setTitle(QCoreApplication.translate("MainWindow", u"\u6570\u636e\u9009\u62e9", None))
        self.btn_message.setText(QCoreApplication.translate("MainWindow", u"Message", None))
        self.btn_print.setText(QCoreApplication.translate("MainWindow", u"Print", None))
        self.btn_logout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.creditsLabel.setText("")
        self.version.setText(QCoreApplication.translate("MainWindow", u"v1.0.3", None))
    # retranslateUi

