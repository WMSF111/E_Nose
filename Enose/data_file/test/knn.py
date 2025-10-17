# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier


# 读取文件函数，数据预处理，70%做训练集，30%做预测集
def read(datafile):
    data = pd.read_csv(datafile)
    # data = pd.read_excel(datafile)
    # 去掉第一列
    data = data.iloc[:, 1:]
    target = data['Species'].unique()
    # 创建一个字典，将 target 中的每个元素映射到一个数字
    target_map = {target[i]: i for i in range(len(target))}
    # 打乱顺序
    data = data.sample(frac=1).reset_index(drop=True)
    length = len(data)
    # 70%做训练集，剩下的为预测集
    data_practice = data[0:int(length * 0.7)]
    data_predict = data[int(length * 0.7):]
    return target_map, data_practice, data_predict


# KNN预测函数
def knn(practice_x, practice_y, predict_x):
    # 测试精度参数为n_neighbors
    neigh = KNeighborsClassifier(n_neighbors=1)
    neigh.fit(practice_x, practice_y)
    predict_y = neigh.predict(predict_x)
    return predict_y


# 将字符类型数据转化为数字类型
def transfer(target_map, array):
    # 使用映射字典转换 array 中的种类标签为数字
    num = [target_map[i] for i in array]
    return num


# 混淆矩阵画图
def cm_plot(t1, output):
    from sklearn.metrics import confusion_matrix
    cm = confusion_matrix(t1, output)
    #    print(cm)
    #    print(len(cm))
    import matplotlib.pyplot as plt
    plt.matshow(cm, cmap=plt.cm.Greens)
    plt.colorbar()
    for x in range(len(cm)):
        for y in range(len(cm)):
            plt.annotate(cm[x, y], xy=(x, y), horizontalalignment='center', verticalalignment='center')
    plt.ylabel('True label')
    plt.xlabel('Predict label')
    return plt


# 读取文件
datafile = './iris.csv'
target_map, data_practice, data_predict = read(datafile) # 训练数据级、预测数据级
# 训练数据的数据和标签，practice_X为数据，practice_y为标签
practice_x = np.array(data_practice.iloc[0:, 0:4]) # 训练数据级
practice_y = list(data_practice['Species'])# 训练标签集
# 预测数据的结果和标签，predict_x为数据，predict_y为标签
predict_x = np.array(data_predict.iloc[0:, 0:4])# 预测数据级
predict_y = knn(practice_x, practice_y, predict_x)# 预测标签集
# 将预测的标签和数据真正的标签转化成数字类型，并画出混淆矩阵
true_y = transfer(target_map, list(data_predict['Species'])) # 数据级的类别（正确标签）
test_y = transfer(target_map, predict_y) # 错误标签转化成数字
print(true_y,test_y)
cm_plot(true_y, test_y).show()
