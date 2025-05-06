import buttonchoose
from PySide2.QtWidgets import  QWidget
import putdownchoose

#构建选择了的选项，对数据源进行筛选，并绘图 
class MainApplication():

    def __init__( self, ui, comboBox, pushButton,scrollArea, logger):
        self.ui = ui
        if scrollArea == ui.scrollArea:
            df_num = 1
        if scrollArea == ui.scrollArea_2:
            df_num = 2
        if scrollArea == ui.scrollArea_3:
            df_num = 3
        if scrollArea == ui.scrollArea_4:
            df_num = 4
        if scrollArea == ui.scrollArea_5:
            df_num = 5
        if scrollArea == ui.scrollArea_6:
            df_num = 6
        self.logger = logger
        self.logger.info("右侧框开始初始化")
        #列写下拉选项
        self.stats1 = putdownchoose.ComboCheckbox(0,comboBox, self.ui, df_num, logger)
        self.setup_ui()
        self.selected_columns = []
        self.selected_column_values = []
        new_widget = QWidget()
        scrollArea.setWidget(new_widget)
        buttonchoose.CSVHeaderButtons(ui, scrollArea, self.stats1.index, df_num, logger)
        self.connect_signals( ui, pushButton, scrollArea, df_num)

    def setup_ui(self):
        self.stats1.ui.show()
    
    def clear_previous_plot(self, scrollArea):
        # 删除之前的绘图
        layout = scrollArea.layout()
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                scrollArea_to_remove = item.widget()
                if scrollArea_to_remove is not None:
                    scrollArea_to_remove.setParent(None)
                    scrollArea_to_remove.deleteLater()

    def connect_signals(self, ui, pushButton, scrollArea, df_num):
        pushButton.clicked.connect(lambda: self.on_button_click(ui, scrollArea, df_num))

    def on_button_click(self, ui, scrollArea, df_num):
        
        #获取选择了的选项
        selected_value1, selected_index1 = self.stats1.value,self.stats1.index
        print(selected_value1, selected_index1)
        # 检查选择了几几个按钮
        if (selected_value1 != "不选") or (selected_index1 != -1):
            #根据选择的列名，列出该列所有类型
            main_app = buttonchoose.CSVHeaderButtons( ui, scrollArea, selected_index1, df_num, self.logger)   
            self.selected_columns = main_app.get_selected_columns()
            self.selected_column_values = main_app.get_selected_column_values()
        else:
            new_widget = QWidget()
            scrollArea.setWidget(new_widget)
            print("缺少参数")


