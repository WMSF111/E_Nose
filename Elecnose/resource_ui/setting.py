# coding:utf-8
from qfluentwidgets import (SettingCardGroup, FolderListSettingCard, ScrollArea,
                            ExpandLayout, ConfigItem, ComboBoxSettingCard, QConfig, 
                            OptionsConfigItem, OptionsValidator, PrimaryPushSettingCard,
                              qconfig, FluentIcon, FolderListValidator)
from PySide2.QtCore import Signal, QStandardPaths, QUrl
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QWidget
from PySide2.QtGui import QDesktopServices
import train.get_txt as get_txt
import os, global_vars

FEEDBACK_URL = "https://github.com/zhiyiYo/PyQt-Fluent-Widgets/issues"

class Config(QConfig):

    musicFolders = ConfigItem(
        "Folders", "LocalMusic", [], FolderListValidator())
    dpiScale = OptionsConfigItem(
        "MainWindow", "DpiScale", "不选", 
        OptionsValidator(["不选", "算术平均滤波法", "递推平均滤波法", "中位值平均滤波法",
                           "一阶滞后滤波法", "加权递推平均滤波法", "消抖滤波法", "限幅消抖滤波法"]), restart=True)

class SettingInterface1(ScrollArea):

    musicFoldersChanged = Signal(list)

    def __init__(self, ui, parent=None):
        super().__init__(parent=parent)
        self.ui = ui
        self.cfg = Config()
        self.scrollWidget = QWidget()
        self.expandLayout = ExpandLayout(self.scrollWidget)
        self.Get_txt = 0


        # music folders
        self.musicInThisPCGroup = SettingCardGroup(
            self.tr("初始设置"), self.scrollWidget)
        self.musicFolderCard = FolderListSettingCard(
            self.cfg.musicFolders,
            self.tr("文件路径"),
            directory = QStandardPaths.writableLocation(QStandardPaths.DesktopLocation),
            parent=self.musicInThisPCGroup
        )
        
        self.languageCard = ComboBoxSettingCard(
            configItem = self.cfg.dpiScale,
            icon=FluentIcon.ZOOM,
            title="预处理",
            content="对文件夹内的txt进行数据的预处理，生成有行列的数据列表",
            texts=["不选", "算术平均滤波法", "递推平均滤波法", "中位值平均滤波法",
                           "一阶滞后滤波法", "加权递推平均滤波法", "消抖滤波法", "限幅消抖滤波法"]
        )
        self.buttoncard = PrimaryPushSettingCard(
            self.tr('进入网页'),
            "Feedback",
            self.tr('大数据模型网页'),
            self.tr('进入该网页可以参考网上的大数据模型进行数据处理'),
            self.musicInThisPCGroup
        )

        self.__initWidget()

    def __initWidget(self):
        self.resize(1000, 800)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setViewportMargins(0, 0, 0, 0)
        self.setWidget(self.scrollWidget)
        self.setWidgetResizable(True)

        # initialize layout
        self.__initLayout()

    def __initLayout(self):
        # add cards to group
        self.musicFolderCard.folderChanged.connect(
            self.musicFolderCard_handleFolderChange)
        self.cfg.dpiScale.valueChanged.connect(
            self.languageCard_handleFolderChange)
        self.buttoncard.clicked.connect(
            lambda: QDesktopServices.openUrl(QUrl(FEEDBACK_URL)))

        self.musicInThisPCGroup.addSettingCard(self.musicFolderCard)
        self.musicInThisPCGroup.addSettingCard(self.languageCard)
        self.musicInThisPCGroup.addSettingCard(self.buttoncard)
        self.expandLayout.setSpacing(28)
        self.expandLayout.addWidget(self.musicInThisPCGroup)

    def musicFolderCard_handleFolderChange(self, folders):
        global_vars.folders = folders
        print("folders=", folders)
        # 检查 "preprocess.txt" 文件是否存在，如果存在则删除
        if os.path.exists("preprocess.txt"):
            os.remove("preprocess.txt")
        if len(self.ui.tab1.textEdit.toPlainText()) != 0:
            self.ui.tab1.textEdit.clear()
            print("clear text")
        for folder_path in folders:
            self.Get_txt = get_txt.Get_txt(folder_path, self.ui)

    def languageCard_handleFolderChange(self, options):
        print("options", options)
        global_vars.preprocess = options
        self.musicFolderCard_handleFolderChange(global_vars.folders)
        if(options != "不选"):
            for folder_path in global_vars.folders:
                self.Get_txt.choose_1()
        

class SettingInterface():
    def __init__(self, tab):
        musicFoldersChanged = Signal(list)
        cfg = Config()
        qconfig.load("config.json", cfg)
        tab.scrollArea.Card = FolderListSettingCard(
            cfg.musicFolders,
            tab.scrollArea.tr("Local music library"),
            directory=QStandardPaths.writableLocation(QStandardPaths.MusicLocation),
            parent=tab.scrollArea
        )
        tab.scrollArea.Card.resize(1000, 300)
        tab.scrollArea.setViewportMargins(0, 0, 0, 0)
        tab.scrollArea.Card.folderChanged.connect(
            musicFoldersChanged)

