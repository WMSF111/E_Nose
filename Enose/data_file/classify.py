import numpy as np
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
import operator
import random


class TRAIN():
    # 输入： finalData=数据级 target =数据标签 test_size = 训练集数量（0.1-0.9）
    def __init__(self, ui, DataFrame):
        self.ui = ui
        target = DataFrame.iloc[1:, 0]
        # 将剩余的列作为数据 (features)
        data = DataFrame.iloc[1:, 1:]
        self.finalData = data  # 读取数据
        self.target = target  # 读取标签

    def svm(self, test_size):
        '''SVM 线性与非线性分类'''
        x_train, x_test, y_train, y_test = (  # 划分训练集与测试集
            train_test_split(self.finalData, self.target, test_size=test_size, random_state=1, stratify=self.target))
        """
        train_test_split()函数: 用于将数据集划分为训练集train和测试集test
        test_size: 0~1表示测试集样本占比、整数表示测试集样本数量
        random_state: 随机数种子。在需要重复实验的时候保证得到一组一样的随机数据。每次填1(其他参数一样)，每次得到的随机数组一样；每次填0/不填，每次都不一样
        stratify=y: 划分数据集时保证每个类别在训练集和测试集中的比例与原数据集中的比例相同
        """
        # ? 标准化训练集和测试集
        sc = StandardScaler()  # 定义一个标准缩放器
        sc.fit(x_train)  # 计算均值、标准差
        X_train_std = sc.transform(x_train)  # 使用计算出的均值和标准差进行标准化
        X_test_std = sc.transform(x_test)  # 使用计算出的均值和标准差进行标准化

        X_combined_std = np.vstack((X_train_std, X_test_std))  # 竖直堆叠
        y_combined = np.hstack((y_train, y_test))  # 水平拼接
        """
        np.vstack(tup): tup为一个元组，返回一个竖直堆叠后的数组
        np.hstack(tup): tup为一个元组，返回一个水平拼接后的数组
        """

        # ? 训练线性支持向量机
        svm = SVC(kernel='linear', C=1.0, random_state=1)  # 定义线性支持向量分类器 (linear为线性核函数)
        svm.fit(X_train_std, y_train)  # 根据给定的训练数据拟合训练SVM模型


        y_pred = svm.predict(X_test_std)# 用训练好的分类器svm预测数据X_test_std的标签
        y_pred[:20]
        accuracy = accuracy_score(y_test, y_pred)  # 查看模型准确度
        confusion = confusion_matrix(y_test, y_pred)  # 混淆概率矩阵
        classification = classification_report(y_test, y_pred, zero_division=0)  # 提供分类报告，避免出现零分母警告

        labels = sorted(set(y_test) | set(y_pred))  # 获取所有出现的类别
        err_str = ""
        for label in labels:
            y_true_label = [1 if y == label else 0 for y in y_test]
            y_pred_label = [1 if y == label else 0 for y in y_pred]
            if sum(y_pred_label) == 0:
                err_str += f"类别 {label} 没有被预测到，精度为 0\n"
        return X_combined_std, y_combined, svm, range(105, 150)

    def knn(self, test_size):
        """
        :param x_test: 测试集数据
        :param x_train: 训练集数据
        :param y_train: 测试集标签
        :param k: 邻居数
        :return: 返回一个列表包含预测结果
        """
        x_train, x_test, y_train, y_test = (  # 划分训练集与测试集
            train_test_split(self.finalData, self.target, test_size=test_size, random_state=1, stratify=self.target))

        # 预测结果列表，用于存储测试集预测出来的结果
        predict_result_set = []

        # 训练集的长度
        train_set_size = len(x_train)

        # 创建一个全零的矩阵，长度为训练集的长度
        distances = np.array(np.zeros(train_set_size))

        # 计算每一个测试集与每一个训练集的距离
        for i in x_test:
            for indx in range(train_set_size):
                # 计算数据之间的距离
                distances[indx] = data_diatance(i, x_train[indx])

            # 排序后的距离的下标
            sorted_dist = np.argsort(distances)

            class_count = {}

            # 取出k个最短距离
            for i in range(test_size):
                # 获得下标所对应的标签值
                sort_label = y_train[sorted_dist[i]]

                # 将标签存入字典之中并存入个数
                class_count[sort_label] = class_count.get(sort_label, 0) + 1

            # 对标签进行排序
            sorted_class_count = sorted(class_count.items(), key=operator.itemgetter(1), reverse=True)

            # 将出现频次最高的放入预测结果列表
            predict_result_set.append(sorted_class_count[0][0])

        # 返回预测结果列表
        return predict_result_set

def data_diatance(x_test, x_train):
    """
    :param x_test: 测试集
    :param x_train: 训练集
    :return: 返回计算的距离
    """

    # sqrt_x = np.linalg.norm(test-train)  # 使用norm求二范数（距离）
    distances = np.sqrt(sum((x_test - x_train) ** 2))
    return distances

def random_number(data_size):
    """
    该函数使用shuffle()打乱一个包含从0到数据集大小的整数列表。因此每次运行程序划分不同，导致结果不同

    改进：
    可使用random设置随机种子，随机一个包含从0到数据集大小的整数列表，保证每次的划分结果相同。

    :param data_size: 数据集大小
    :return: 返回一个列表
    """

    number_set = []
    for i in range(data_size):
        number_set.append(i)

    random.shuffle(number_set)

    return number_set
