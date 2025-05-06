import os
import pandas as pd
from PySide2.QtCore import QObject, Signal
import putdownchoose
import global_vars
import putdownchoose


class InputWaiter(QObject):
    textEntered = Signal(str)

    def __init__(self, ui, logger):
        super().__init__()
        self.ui = ui
        self.logger = logger
        #当点击按钮后执行onTextChanged文件
        self.ui.tab1.Button.clicked.connect(lambda: self.onTextChanged(ui))


    def onTextChanged(self, ui):
        # 一个列头及其索引的的字典和一个列头列表
        header_dict, global_vars.headers_list = self.read_df_return_header(global_vars.file_text_DataFrame) # 获取内容（字典）及列头（列表）
        #转化为.csv文件
        global_vars.file_text_DataFrame.to_csv(os.path.join(str(global_vars.folders[0]), 'train', 'trainfile.csv'), index = False)
        # 将csv文件读取到df中,是dataframe数据
        global_vars.df_dataframe = pd.read_csv(os.path.join(str(global_vars.folders[0]), 'train', 'trainfile.csv')) #读取文件,得到dataframe数据
        # df1 = pd.read_csv(os.path.join(str(global_vars.folders[0]), 'train', 'datafile.csv')) #读取文件,得到dataframe数据
        # 将df传入到算法类中
        #当第一列改变后，新建对象
        putdownchoose.MainApplication( 
            ui.tab2, ui.tab2.LH_ComboBox_1Y_2, ui.tab2.LH_ComboBox_1X_2, 
            ui.tab2.LH_ComboBox_1L_2, ui.tab2.LH_ComboBox_2, ui.tab2.comboBox_C1_2, 
            ui.tab2.LH_Button_2, self.logger)
        
    def read_df_return_header(self, df):
        header = df.columns.tolist() # 获取数据框的列名，并转换为列表
        header_dict = {col_name: index for index, col_name in enumerate(header)}  # 创建一个字典，将列名作为键，列索引作为值
        return header_dict, header # 返回结果，一个字典和一个列表

            
            
