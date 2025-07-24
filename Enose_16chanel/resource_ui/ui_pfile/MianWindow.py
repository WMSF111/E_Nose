# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MianWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QHeaderView,
    QMainWindow, QMenu, QMenuBar, QSizePolicy,
    QStatusBar, QToolBar, QTreeWidget, QTreeWidgetItem,
    QWidget)
# import icon_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1077, 706)
        self.Open_action = QAction(MainWindow)
        self.Open_action.setObjectName(u"Open_action")
        icon = QIcon()
        icon.addFile(u":/\u6587\u4ef6/\u6253\u5f00.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Open_action.setIcon(icon)
        self.Newfile_action = QAction(MainWindow)
        self.Newfile_action.setObjectName(u"Newfile_action")
        icon1 = QIcon()
        icon1.addFile(u":/\u6587\u4ef6/\u65b0\u5efa.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Newfile_action.setIcon(icon1)
        self.action = QAction(MainWindow)
        self.action.setObjectName(u"action")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(1077, 630))
        self.centralwidget.setLayoutDirection(Qt.LeftToRight)
        self.horizontalLayout_3 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.treeWidget = QTreeWidget(self.centralwidget)
        __qtreewidgetitem = QTreeWidgetItem(self.treeWidget)
        QTreeWidgetItem(__qtreewidgetitem)
        QTreeWidgetItem(__qtreewidgetitem)
        __qtreewidgetitem1 = QTreeWidgetItem(self.treeWidget)
        QTreeWidgetItem(__qtreewidgetitem1)
        QTreeWidgetItem(__qtreewidgetitem1)
        QTreeWidgetItem(__qtreewidgetitem1)
        QTreeWidgetItem(__qtreewidgetitem1)
        __qtreewidgetitem2 = QTreeWidgetItem(self.treeWidget)
        QTreeWidgetItem(__qtreewidgetitem2)
        QTreeWidgetItem(__qtreewidgetitem2)
        QTreeWidgetItem(__qtreewidgetitem2)
        self.treeWidget.setObjectName(u"treeWidget")

        self.horizontalLayout_3.addWidget(self.treeWidget)

        self.show_widget = QWidget(self.centralwidget)
        self.show_widget.setObjectName(u"show_widget")
        self.gridLayout_2 = QGridLayout(self.show_widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.show_Layout = QGridLayout()
        self.show_Layout.setObjectName(u"show_Layout")

        self.gridLayout_2.addLayout(self.show_Layout, 0, 0, 1, 1)


        self.horizontalLayout_3.addWidget(self.show_widget)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1077, 22))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        self.menu_3 = QMenu(self.menubar)
        self.menu_3.setObjectName(u"menu_3")
        self.menu_4 = QMenu(self.menubar)
        self.menu_4.setObjectName(u"menu_4")
        self.menu_5 = QMenu(self.menubar)
        self.menu_5.setObjectName(u"menu_5")
        self.menu_6 = QMenu(self.menubar)
        self.menu_6.setObjectName(u"menu_6")
        self.menu_7 = QMenu(self.menubar)
        self.menu_7.setObjectName(u"menu_7")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menu_4.menuAction())
        self.menubar.addAction(self.menu_5.menuAction())
        self.menubar.addAction(self.menu_6.menuAction())
        self.menubar.addAction(self.menu_7.menuAction())
        self.menu.addAction(self.Open_action)
        self.menu.addAction(self.Newfile_action)
        self.menu_2.addAction(self.action)
        self.toolBar.addAction(self.Open_action)
        self.toolBar.addAction(self.Newfile_action)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Open_action.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00", None))
        self.Newfile_action.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa", None))
        self.action.setText(QCoreApplication.translate("MainWindow", u"\u4f20\u611f\u5668\u8bbe\u7f6e", None))
        ___qtreewidgetitem = self.treeWidget.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"\u5b9e\u9a8c", None));

        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        ___qtreewidgetitem1 = self.treeWidget.topLevelItem(0)
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("MainWindow", u"\u51c6\u5907\u9636\u6bb5", None));
        ___qtreewidgetitem2 = ___qtreewidgetitem1.child(0)
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("MainWindow", u"\u4f20\u611f\u5668\u8bbe\u7f6e", None));
        ___qtreewidgetitem3 = ___qtreewidgetitem1.child(1)
        ___qtreewidgetitem3.setText(0, QCoreApplication.translate("MainWindow", u"\u4e32\u53e3\u8bbe\u7f6e", None));
        ___qtreewidgetitem4 = self.treeWidget.topLevelItem(1)
        ___qtreewidgetitem4.setText(0, QCoreApplication.translate("MainWindow", u"\u6d4b\u8bd5\u9636\u6bb5", None));
        ___qtreewidgetitem5 = ___qtreewidgetitem4.child(0)
        ___qtreewidgetitem5.setText(0, QCoreApplication.translate("MainWindow", u"\u4f20\u611f\u5668\u9009\u62e9", None));
        ___qtreewidgetitem6 = ___qtreewidgetitem4.child(1)
        ___qtreewidgetitem6.setText(0, QCoreApplication.translate("MainWindow", u"\u91c7\u6837\u8bbe\u7f6e", None));
        ___qtreewidgetitem7 = ___qtreewidgetitem4.child(2)
        ___qtreewidgetitem7.setText(0, QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u5b9e\u9a8c", None));
        ___qtreewidgetitem8 = ___qtreewidgetitem4.child(3)
        ___qtreewidgetitem8.setText(0, QCoreApplication.translate("MainWindow", u"\u52a0\u8f7d\u5b9e\u9a8c", None));
        ___qtreewidgetitem9 = self.treeWidget.topLevelItem(2)
        ___qtreewidgetitem9.setText(0, QCoreApplication.translate("MainWindow", u"\u6570\u636e\u5206\u6790", None));
        ___qtreewidgetitem10 = ___qtreewidgetitem9.child(0)
        ___qtreewidgetitem10.setText(0, QCoreApplication.translate("MainWindow", u"\u7b97\u6cd5\u9009\u62e9", None));
        ___qtreewidgetitem11 = ___qtreewidgetitem9.child(1)
        ___qtreewidgetitem11.setText(0, QCoreApplication.translate("MainWindow", u"\u754c\u9762\u7f8e\u5316", None));
        ___qtreewidgetitem12 = ___qtreewidgetitem9.child(2)
        ___qtreewidgetitem12.setText(0, QCoreApplication.translate("MainWindow", u"\u5927\u6a21\u578b\u5206\u6790", None));
        self.treeWidget.setSortingEnabled(__sortingEnabled)

        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6{F)", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u5b9e\u9a8c(E)", None))
        self.menu_3.setTitle(QCoreApplication.translate("MainWindow", u"\u6570\u636e(D)", None))
        self.menu_4.setTitle(QCoreApplication.translate("MainWindow", u"\u8bbe\u5907(W)", None))
        self.menu_5.setTitle(QCoreApplication.translate("MainWindow", u"\u53c2\u8003(R)", None))
        self.menu_6.setTitle(QCoreApplication.translate("MainWindow", u"\u7cfb\u7edf\u7ba1\u7406(S)", None))
        self.menu_7.setTitle(QCoreApplication.translate("MainWindow", u"\u5e2e\u52a9(H)", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

