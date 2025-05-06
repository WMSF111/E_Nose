# import numpy as np
# import pandas as pd
# import os
# import seaborn as sns
# from sklearn.preprocessing import scale
# from factor_analyzer.factor_analyzer import calculate_bartlett_sphericity
# import matplotlib.pyplot as plt
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LogisticRegression
# from sklearn.datasets import load_wine
# from sklearn.metrics import confusion_matrix,accuracy_score,classification_report


# class pca(): 
#     def __init__(self):
#         self.df = []
#         self.df=pd.read_csv(os.path.join(os.path.dirname(__file__)) + '\\datafile.csv') #读取文件
#         data=pd.DataFrame(self.df.iloc[:, 1:]) 
#         self.process(data)
        
#     def process(self, data):
#         # data=pd.DataFrame(data) 
#         chi_value, p_value = calculate_bartlett_sphericity(data)  # 检验各个变量是否独立
#         data.info()
#         print(chi_value, p_value)
#         data_scale = scale(data) #数据标准化
#         CovX = np.around(np.corrcoef(data.T), decimals=3) # 相关系数矩阵
#         n,p = data.shape 
#         # print(data.shape)
#         # R=data.corr() #计算数据框中各变量之间的相关系数，得到相关矩阵R
#         featValue, featVec = np.linalg.eig(CovX.T) #求特征值featValue与特征向量featVec，特征值默认从大到小排序
#         featValue = sorted(featValue, reverse = True) #对特征值进行排序输出
#         name = [] #主成分名称
#         s=0
#         num=0
#         cr=[] #累计贡献率
#         pc=[] #主成分
#         for i in range(len(featValue)):
#             pc.append(i)
#             num+=1
#             contri=featValue[i]/np.sum(featValue) #第i主成分贡献率(度)
#             cr.append(contri)
#             name.append(data.columns[i])
#             s += contri #累计贡献率
#             if s >= 0.8: #累计贡献率达80%即停止
#                 break
#         for i in range(num): 
#             selectVec = np.matrix(featVec.T[pc]).T
#             selectVec = selectVec*(-1)
#             finalData = np.dot(data_scale, selectVec)
#         print('主成分名称：',name)
#         print('主成分个数：',num)
#         # print('主成分得分：',finalData)
#         print('贡献率：',cr)
#         print('累计贡献率：',s)
#         self.train_data(finalData)
#         # self.draw_line(self, data, featValue, selectVec)

#     def train_data(self, finalData):
#         X = finalData
#         y = self.df['target'].tolist()
#         x_train,x_test,y_train,y_test = train_test_split(X, y, test_size=0.2, random_state=0)

#         #逻辑回归模型
#         lg = LogisticRegression()
#         x_train = np.asarray(x_train)
#         y_train = np.asarray(y_train)
#         x_test = np.asarray(x_test)
#         lg.fit(x_train, y_train)
#         y_pred = lg.predict(x_test)

#         print("模型准确率",accuracy_score(y_test,y_pred))
#         print("混淆矩阵",confusion_matrix(y_test,y_pred))
#         print("分类报告",classification_report(y_test,y_pred))

#     def draw_line(self, data, featValue, selectVec):
#         plt.scatter(range(1,data.shape[1] + 1), featValue)
#         plt.plot(range(1,data.shape[1] + 1), featValue)
#         plt.hlines(y=1,xmin=0,xmax=13)
#         plt.grid()
#         plt.show()
#         plt.figure(figsize = (7,7))
#         ax = sns.heatmap(selectVec, annot = True, cmap ="BuPu")
#         ax.yaxis.set_tick_params(labelsize = 15)
#         plt.show()

# pca()