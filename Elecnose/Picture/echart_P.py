import global_vars
import Picture.The_2 as The_2
import Picture.The_3 as The_3
from PySide2.QtWebEngineWidgets import QWebEngineView

#根据传入的图表列的索引及选择的列的名称进行绘图
class Plotter:
    def __init__(self, df, logger):
        self.df = df
        self.logger = logger
        self.logger.info("Plotter 开始初始化")
        self.bro = QWebEngineView()

    def plot_chart(self, selected_index1, selected_index2, selected_index3, selected_index5, selected_value1, selected_value2, selected_value3, selected_value4, width, height):
        # print("selected_index3 :",selected_index3,"selected_value3 :",selected_value3) 
        self.logger.info("plot_chart 开始绘图")
        if (selected_index3 != -1 and selected_value3 != "不选") and (selected_value4 == "radar" or  selected_value4 == "bar"):
            if selected_index5 is -1:
                colors = global_vars.color[0]
            else:
                colors = global_vars.color[selected_index5]
            global_vars.color1 = colors
            #画单独的柱状图
            plotter = The_3.ContractAmountPlotter(global_vars.result_df)
            plotter.plot_contract_amounts(selected_index1, selected_index2,selected_index3, global_vars.result_df, global_vars.color1, width, height,selected_value4)
            self.bro = plotter.bro
        else:
            if selected_index5 is -1:
                colors = global_vars.color[0]
            else:
                colors = global_vars.color[selected_index5]
            global_vars.color1 = colors
            #画单独的柱状图
            plotter = The_2.ContractAmountPlotter(global_vars.result_df, f'不同{selected_value2}对应的{selected_value1}', f'{selected_value1}')
            plotter.plot_contract_amounts(selected_index1, selected_index2, global_vars.result_df, global_vars.color1, width, height,selected_value4)
            self.bro = plotter.bro
        self.logger.info("plot_chart 绘图结束")
            