import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.preprocessing import scale
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.decomposition import PCA
from factor_analyzer.factor_analyzer import calculate_bartlett_sphericity
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_wine
from sklearn.metrics import confusion_matrix,accuracy_score,classification_report
import statsmodels.api as sm
import global_vars
import matplotlib.cm as cm
import mplcursors
import Picture.figureCanvas as fc

def draw_line( ui, name, num, fig, target, finalData, data):
        # y = self.df['target'].tolist() #list
        # print(self.df['target'].tolist())
        if num == 3:
            # 创建一个颜色映射对象
            cmap = cm.get_cmap('tab10')

            # 创建子图
            ax = fig.add_subplot(111, projection='3d')

            # 获取类别值的唯一值和对应的索引
            unique_categories, category_indices = np.unique(target, return_index=True)
            # 绘制所有数据点，并为每个类别使用不同的颜色
            for i, category in enumerate(unique_categories):
                category_data = finalData[target == category] #提取出 finalData 中对应当前类别的数据行。
                color = cmap(i)
                scatter = ax.scatter(category_data[:, 0], category_data[:, 1], category_data[:, 2], c=color, label=f"Category {category}")
            
            # # # 使用mplcursors库显示标注
            # cursor = mplcursors.cursor(scatter, hover=True)
            # cursor.connect("add", lambda sel: sel.annotation.set_text(f"{sel.artist.get_label()}"))
            # cursor.connect("remove", lambda sel: sel.annotation.set_text(""))  # 设置标注文本为空字符串
            
            # 添加图例，只显示每种颜色的标签
            handles, labels = ax.get_legend_handles_labels()
            unique_handles = list(set(handles))
            unique_labels = [label for handle, label in zip(handles, labels) if handle in unique_handles]
            ax.legend(unique_handles, unique_labels, title="Category", loc='upper right',bbox_to_anchor=(1.4, 1))
            
        
            # 设置坐标轴标签
            if len(name) != 0:
                ax.set_xlabel("PC"+name[0])
                ax.set_ylabel("PC"+name[1])
                ax.set_zlabel("PC"+name[2])
            else:
                ax.set_xlabel("PC1")
                ax.set_ylabel("PC2")
                ax.set_zlabel("PC3")
        elif num == 2:
            # 创建一个颜色映射对象
            cmap = cm.get_cmap('tab10')

            # 创建子图
            ax = fig.add_subplot(111)

            # 获取类别值的唯一值和对应的索引
            unique_categories, category_indices = np.unique(target, return_index=True)

            # 绘制所有数据点，并为每个类别使用不同的颜色
            for i, category in enumerate(unique_categories):
                category_data = finalData[target == category]
                color = cmap(i/len(unique_categories))
                scatter = ax.scatter(category_data[:, 0], category_data[:, 1], color=color, label=f'{category}')
                # # 使用mplcursors库显示标注
                cursor = mplcursors.cursor(scatter, hover=True)
                cursor.connect("add", lambda sel: sel.annotation.set_text(f"{sel.artist.get_label()}"))
                cursor.connect("remove", lambda sel: sel.annotation.set_text(""))  # 设置标注文本为空字符串
            
            # 添加图例，只显示每种颜色的标签
            handles, labels = ax.get_legend_handles_labels()
            unique_handles = list(set(handles))
            unique_labels = [label for handle, label in zip(handles, labels) if handle in unique_handles]
            ax.legend(unique_handles, unique_labels, title="Category",loc='upper right')
             # 使用mplcursors库显示图例
            # mplcursors.cursor(scatter, hover=True).connect("add", lambda sel: sel.annotation.set_text(f"Category: {sel.artist.get_label()}"))
            # 设置坐标轴标签
            if len(name) != 0:
                ax.set_xlabel("PC"+name[0])
                ax.set_ylabel("PC"+name[1])
            else:
                ax.set_xlabel("PC1")
                ax.set_ylabel("PC2")
        elif num == 0:
            cols = global_vars.headers[1:]
            ax = fig.add_subplot(111)
            for column in cols:
                ax.scatter(data[column], target, label=column)
                
    
            # 添加标题和标签
            ax.set_title('Scatter Plot of Specific Columns with Target Variable')
            ax.set_xlabel('Independent Variables')
            ax.set_ylabel('Dependent Variable')
    
            # 添加图例
            ax.legend()

            print(finalData.summary())
            print(cols)
            # 重新绘制画布
            fc.canvas.draw()


def clear_previous_plot(layout, widget):
        # 删除之前的绘图
        layout = widget.layout()
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget_to_remove = item.widget()
                if widget_to_remove is not None:
                    widget_to_remove.setParent(None)
                    widget_to_remove.deleteLater()