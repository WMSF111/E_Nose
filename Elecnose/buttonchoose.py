import pandas as pd
from PySide2.QtCore import Qt
from PySide2.QtWidgets import  QWidget, QPushButton, QVBoxLayout
import global_vars
import The_test

filtered_df = []


class CSVHeaderButtons(QWidget):
    def __init__(self, ui, target_widget, index, df_num, logger):
        super().__init__()
        self.logger = logger
        self.logger.info("CSVHeaderButtons 右侧框画多选按钮开始初始化")
        self.buttons = []
        self.df = global_vars.df
        self.column_index = index
        self.selected_columns = []
        self.selected_column_values = []
        # 在对应画布上列出按钮供用户选择
        self.initUI(ui, target_widget, index, global_vars.headers, df_num)
        # print('selected_column_values: ',self.selected_column_values)
    
    def select_value(self, ui):
        if global_vars.selected_value4_1 != 0:
            The_test.MainApplication(global_vars.result_df, ui, ui.LH_Button, ui.scrollArea_L1, self.logger)
            print(global_vars.selected_value4_1)
        if global_vars.selected_value4_2 != 0:
            The_test.MainApplication(global_vars.result_df, ui, ui.LH_Button_2, ui.scrollArea_L2, self.logger)
            print(global_vars.selected_value4_2)
        if global_vars.selected_value4_3 != 0:
            The_test.MainApplication(global_vars.result_df, ui, ui.LH_Button_3,  ui.scrollArea_L3, self.logger)
            print(global_vars.selected_value4_3)
        if global_vars.selected_value4_4 != 0:
            The_test.MainApplication(global_vars.result_df, ui, ui.LH_Button_4, ui.scrollArea_L4, self.logger)
            print(global_vars.selected_value4_4)
        

    def initUI(self, ui, target_widget, index, headers, df_num):
        self.ui = ui
        self.layout = QVBoxLayout()
        if index != -1:
            #根据列作按钮
            self.read_data_from_csv(ui, index, headers, df_num)
        
        target_widget.setWidgetResizable(True)
        target_widget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        target_widget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        
        widget = QWidget()
        widget.setLayout(self.layout)
        
        target_widget.setWidget(widget)
        target_widget.setLayout(QVBoxLayout())
        target_widget.layout().addWidget(target_widget)
    
    #读取选择的按钮，并将按钮列到画布中
    def read_data_from_csv(self, ui, index, headers, df_num):
        unique_values = global_vars.df.iloc[:, index].unique()
        for idx, value in enumerate(unique_values):
            btn = QPushButton(str(value))
            btn.clicked.connect(lambda checked=False, idx=id: self.toggle_column_selection(global_vars.df, ui, idx, headers, index, df_num))
            self.buttons.append(btn)
            self.layout.addWidget(btn) # 画按钮
        self.select_all_columns(ui)
        self.toggle_column_selection(global_vars.df, ui, -1, headers, index, df_num)


    def toggle_column_selection(self, df, ui, column_index, headers ,index, df_num):
        if column_index in self.selected_columns:
            self.selected_columns.remove(column_index)
        else:
            self.selected_columns.append(column_index)
        
        self.selected_columns = self.selected_columns
        self.selected_column_values = self.get_selected_column_values()
        # 根据如今选择的是哪个框，在对应df存储选择的数据
        if df_num == 1:
            global_vars.df_1 = self.Get_file(df, headers[index], self.selected_column_values)
        elif df_num == 2:
            global_vars.df_2 = self.Get_file(df, headers[index], self.selected_column_values)
        elif df_num == 3:
            global_vars.df_3 = self.Get_file(df, headers[index], self.selected_column_values)
        elif df_num == 4:
            global_vars.df_4 = self.Get_file(df, headers[index], self.selected_column_values)
        elif df_num == 5:
            global_vars.df_5 = self.Get_file(df, headers[index], self.selected_column_values)
        elif df_num == 6:
            global_vars.df_6 = self.Get_file(df, headers[index], self.selected_column_values)
        print(global_vars.df_1)
        global_vars.result_df = global_vars.merge_and_keep_common_rows(df, global_vars.df_1, global_vars.df_2, global_vars.df_3, global_vars.df_4, global_vars.df_5, global_vars.df_6)
        print(global_vars.result_df)
        self.select_value(ui)
        self.update_button_styles()

    def select_all_columns(self, ui):
        self.selected_columns = list(range(len(self.buttons)))
        #根据选择的数据刷新画布
        self.select_value(ui)
        self.update_button_styles()
        

    def update_button_styles(self):
        for idx, btn in enumerate(self.buttons):
            if idx in self.selected_columns:
                btn.setStyleSheet("background-color: rgba(173, 216, 230, 0.5)")
            else:
                btn.setStyleSheet("")

    def get_selected_columns(self):
        selected_indices = []
        for idx, btn in enumerate(self.buttons):
            if idx in self.selected_columns:
                selected_indices.append(idx)
        return selected_indices

    def get_selected_column_values(self):
        selected_values = []
        for idx in self.get_selected_columns():
            unique_values = self.df.iloc[:, self.column_index].unique()
            selected_values.append(unique_values[idx])
        return selected_values
    
    def Get_file(self, df, column_header, target_strings):   
         # 检查列头是否存在
        if column_header not in df.columns:
            return pd.DataFrame()  # 如果列头不存在，返回一个空 DataFrame
    
        # 使用向量化操作，筛选出包含目标字符串的行
        mask = df[column_header].isin(target_strings)
        #df[column_header].astype(str) 的作用是将 DataFrame 中特定列的数据类型转换为字符串类型。
        filtered_df = df[mask]
    
        return filtered_df

