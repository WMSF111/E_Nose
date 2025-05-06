import matplotlib.pyplot as plt
from pyecharts.charts import Bar,Pie,Funnel,Scatter,Line
from PySide2.QtWebEngineWidgets import QWebEngineView
from pyecharts import options as opts

plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Microsoft Yahei']

class ContractAmountPlotter:
    def __init__(self, file_path, title, ylabel):
        self.file_path = file_path
        self.title = title
        self.ylabel = ylabel
        self.amount = 0
        #设置浏览器网页为pyecharts图
        self.bro = QWebEngineView()

    def read_data_from_csv(self, the2, the1, df):
        data_dict = {}
        for index, row in df.iterrows():
            year = row.iloc[the1]  # 提取横轴内容
            contract_amount = int(row.iloc[the2])  # 提取纵轴内容

            # 如果之前横轴标签没有保存到字典中，为该标签创建一个空列表作为值。
            if year not in data_dict:
                data_dict[year] = [] 
            data_dict[year].append(contract_amount)  # 添加合同额数据
        
        # 获取所有X标签，并将获取的x轴标签按顺序排序
        The_x = sorted(data_dict.keys()) 
        # 遍历 The_x 中的每个年份，对于每个年份都执行 sum(data_dict[year]) 的操作，并将结果组成一个新的列表。
        contract_amounts = [sum(data_dict[year]) for year in The_x]

        return The_x, contract_amounts

    def plot_contract_amounts(self, the1, the2, df, color, width, height, value):
        #返回对应的X轴标签和对应标签累加的数值
        The_Labels, contract_amounts = self.read_data_from_csv(the1, the2 ,df)
        if max(contract_amounts) > 10000 and max(contract_amounts) < 100000:
            # 将 contract_amounts 数组中的每个数字都除以 10000
            contract_amounts = [round(amount / 10000,2) for amount in contract_amounts]
            title = "万"
        elif max(contract_amounts) > 100000 and max(contract_amounts) < 1000000:
            # 将 contract_amounts 数组中的每个数字都除以 10000
            contract_amounts = [round(amount / 100000,2) for amount in contract_amounts]
            title = "十万"
        elif max(contract_amounts) > 1000000 and max(contract_amounts) < 10000000:
            # 将 contract_amounts 数组中的每个数字都除以 10000
            contract_amounts = [round(amount / 1000000,2) for amount in contract_amounts]
            title = "百万"
        elif max(contract_amounts) > 10000000 and max(contract_amounts) < 100000000:
            # 将 contract_amounts 数组中的每个数字都除以 10000
            contract_amounts = [round(amount / 10000000,2) for amount in contract_amounts]
            title = "千万"
        else:
            title = ""

        if(value == "bar"):
            # 设置刻度值的自定义格式化函数
            bar = (
                Bar(init_opts=opts.InitOpts(
                    width=str(width) + "px",
                    height=str(height) + "px",
                    theme=color, 
                ))
                .add_xaxis(The_Labels)
                .add_yaxis(self.title, contract_amounts)
                .set_series_opts(label_opts=opts.LabelOpts(is_show=True, position="top"))
                .set_global_opts(
                    title_opts=opts.TitleOpts(title="柱状图"),
                    yaxis_opts = opts.AxisOpts(
                        # 刻度值
                        axislabel_opts=opts.LabelOpts(
                            font_size = 11,
                            formatter = "{{value}} {}".format(title)
                        ),),
                    xaxis_opts = opts.AxisOpts(
                        # 刻度值
                        axislabel_opts=opts.LabelOpts(
                            interval=0
                        ),)))
            self.bro.setHtml(bar.render_embed())

        elif(value == "pie"):
            data_pairs = [(label,amount) for label, amount in zip(The_Labels, contract_amounts)]
            pie = (
            Pie(init_opts = opts.InitOpts(
                width = str(width) + "px",
                height = str(height) + "px",
                theme = color,
                ))
            .add("", data_pairs, radius = ["40%", "75%"])
            # .set_colors(color)
            .set_global_opts(title_opts=opts.TitleOpts(title="饼状图"),
                             legend_opts=opts.LegendOpts( orient="vertical", pos_top="5%", pos_right="2%", item_width = 15,item_height=10 ),
                             tooltip_opts = opts.TooltipOpts(formatter = "{{b}} <br/>{{c}}{}".format(title)))
            )
            self.bro.setHtml(pie.render_embed())
        elif(value == "funnel"):
            data_pairs = [(label,amount) for label, amount in zip(The_Labels, contract_amounts)]
            funnel = (
            Funnel(init_opts = opts.InitOpts(
                width = str(width) + "px",
                height = str(height) + "px",
                theme = color,
                ))
            .add("", data_pairs)
            .set_global_opts(title_opts=opts.TitleOpts(title="漏斗图"),
                             tooltip_opts = opts.TooltipOpts(formatter = "{{b}} <br/>{{c}}{}".format(title)))
            )
            self.bro.setHtml(funnel.render_embed())
        elif(value == "scatter"):
            scatter = (
                Scatter(init_opts = opts.InitOpts(
                width = str(width) + "px",
                height = str(height) + "px",
                theme = color,
                ))
                .add_xaxis(The_Labels)
                .add_yaxis(self.title,contract_amounts)
                .set_global_opts(title_opts=opts.TitleOpts(title="散点图"),
                                 yaxis_opts = opts.AxisOpts(
                                # 刻度值
                                axislabel_opts=opts.LabelOpts(
                                    font_size = 11,
                                    formatter = "{{value}} {}".format(title)
                                ),))
            )
            self.bro.setHtml(scatter.render_embed())
        elif (value == "line"):
            line = (
                Line(init_opts = opts.InitOpts(
                width = str(width) + "px",
                height = str(height) + "px",
                theme = color,
                ))
                .add_xaxis(The_Labels)
                .add_yaxis(self.title,contract_amounts)
                .set_global_opts(title_opts=opts.TitleOpts(title="折线图"),
                                 yaxis_opts = opts.AxisOpts(
                                # 刻度值
                                axislabel_opts=opts.LabelOpts(
                                    font_size = 11,
                                    formatter = "{{value}} {}".format(title)
                                ),))
            )
            self.bro.setHtml(line.render_embed())
        
             
        print(self.title,contract_amounts,type(contract_amounts))
        






