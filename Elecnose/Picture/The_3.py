import matplotlib.pyplot as plt
from PySide2.QtWebEngineWidgets import QWebEngineView
from pyecharts.charts import Radar,Bar
from pyecharts import options as opts

plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Microsoft Yahei']

class ContractAmountPlotter:
    def __init__(self, df):
        self.df = df
        self.data_dict = {}
        # 生成绘图series
        self.data_radar = []
        # 各特征维度取值范围
        self.scope = []
        #设置浏览器网页为pyecharts图
        self.bro = QWebEngineView()

    def read_data(self, df, the1, the2, the3):
        for index, row in df.iterrows():
                product = row.iloc[the2] 
                year = row.iloc[the3]  # 提取年份

                if product not in self.data_dict:
                    self.data_dict[product] = {}
                if year not in self.data_dict[product]:
                    self.data_dict[product][year] = 0
                self.data_dict[product][year] += int(row.iloc[the1])

        # 获取所有产品类型和年份
        The_labels = list(self.data_dict.keys())
        The_lengends = sorted(set(The_lengend for The_label in self.data_dict.values() for The_lengend in The_label.keys())) #取所有产品的年份并进行排序去重

        return The_labels,The_lengends
    
    def draw_radar(self,max_contract_amount, The_legends, color, width, height, title):
        radar = Radar(init_opts = opts.InitOpts(
                width = str(width) + "px",
                height = str(height) + "px",
                theme = color,
                ))
        radar.add_schema(
            schema=self.scope,
            shape="polygon",
            center=["50%", "50%"],#宽高：900px*500px
            radius="70%",
            angleaxis_opts=opts.AngleAxisOpts(
                axistick_opts=opts.AxisTickOpts(is_show=True),
                axislabel_opts=opts.LabelOpts(is_show=False,
                ),
                axisline_opts=opts.AxisLineOpts(is_show=True),
                splitline_opts=opts.SplitLineOpts(is_show=True)
            ),
            radiusaxis_opts=opts.RadiusAxisOpts(
                min_=0,
                max_= max_contract_amount,
                interval= max_contract_amount/5,
                splitarea_opts=opts.SplitAreaOpts(
                    is_show=True, areastyle_opts=opts.AreaStyleOpts(opacity=1)
                ),
                axislabel_opts=opts.LabelOpts(formatter="{{value}} {}".format(title))
            ),
            polar_opts=opts.PolarOpts(),
            splitline_opt=opts.SplitLineOpts(is_show=False)
            )
    
        for i,The_legend in enumerate(The_legends):
            radar.add(
                series_name=The_legend,
                areastyle_opts=opts.AreaStyleOpts(opacity=0.2),
                linestyle_opts=opts.LineStyleOpts(width=2),
                data=self.data_radar[i],
            )
        radar.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        radar.set_global_opts(
            title_opts=opts.TitleOpts(title = '雷达图',pos_left='left'),
            )    
        self.bro.setHtml(radar.render_embed())

    def draw_bar(self,max_contract_amount, The_labels, The_legends, color, width, height, title):
        bar = Bar(init_opts = opts.InitOpts(
                theme = color,
                width = str(width) + "px",
                height = str(height) + "px",
                ))
        bar.add_xaxis(The_labels)
        for i, The_legend in enumerate(The_legends):
            # 使用 tolist() 方法将 NumPy 数组转换为 Python 列表
            bar.add_yaxis(The_legend, self.data_radar[i][0]['value'])
            bar.set_global_opts(title_opts=opts.TitleOpts(title="柱状图"),
                yaxis_opts = opts.AxisOpts(
                # 刻度值
                axislabel_opts=opts.LabelOpts(
                    font_size = 11,
                    position='top',
                    formatter = "{{value}} {}".format(title)
                ),))
        print("len(The_labels) :",len(The_labels),"len(The_legends) :",len(The_legends))
        if len(The_labels) >= 8 or len(The_legends) >= 8:
            print("不显示")
            bar.set_series_opts(label_opts=opts.LabelOpts(is_show = False, position="top"))
        else:
            print("显示")
            bar.set_series_opts(label_opts=opts.LabelOpts(is_show=True, position="top"))
            
        self.bro.setHtml(bar.render_embed())

    def plot_contract_amounts(self, the1, the2, the3, df, color, width, height, The_value):
        The_labels, The_legends = self.read_data(df, the1, the2, the3)        
        max_contract_amount = 0
        for i,The_legend in enumerate(The_legends):
            for j,The_label in enumerate(The_labels):
                value = self.data_dict[The_label].get(The_legend, 0)
                if value > max_contract_amount:
                    max_contract_amount = value

        for i,The_legend in enumerate(The_legends):
            dic = {}
            value = []
            for j,The_label in enumerate(The_labels):
                value.append(self.data_dict[The_label].get(The_legend, 0))
            if max_contract_amount > 10000 and max_contract_amount < 100000:
                value = [round(amount / 10000,2) for amount in value]
                title = "万"
                max_contract_amount1 = max_contract_amount/10000
            elif max_contract_amount > 100000 and max_contract_amount < 1000000:
                value = [round(amount / 100000,2) for amount in value]
                title = "十万"
                max_contract_amount1 = max_contract_amount/100000
            elif max_contract_amount > 1000000 and max_contract_amount < 10000000:
                value = [round(amount / 1000000,2) for amount in value]
                title = "百万"
                max_contract_amount1 = max_contract_amount/1000000
            elif max_contract_amount > 10000000 and max_contract_amount < 100000000:
                value = [round(amount / 10000000,2) for amount in value]
                title = "千万"
                max_contract_amount1 = max_contract_amount/10000000
            else:
                title = ""
            dic['name'],dic['value'] = The_legend,value
            self.data_radar.append([dic])

        for The_label in The_labels:
            dic2 = {}
            dic2['name'] = The_label
            # 如果键存在于字典中，则返回对应的值；如果键不存在，则返回指定的默认值（这里是0）。
            for The_legend in The_legends:
                dic2['max'], dic2['min'] = int(max_contract_amount1+1), 0
            # print(dic2)
            self.scope.append(dic2)

        if The_value == "radar":
            self.draw_radar(int(max_contract_amount1+1), The_legends, color, width, height, title)
        elif The_value == "bar":
            self.draw_bar(int(max_contract_amount1+1), The_labels, The_legends, color, width, height, title)
        
        

