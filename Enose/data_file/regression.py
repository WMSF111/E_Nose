import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report

class TRAIN():
    # 输入： finalData=数据级 target =数据标签 test_size = 训练集数量（0.1-0.9）
    def __init__(self, ui, DataFrame):
        self.ui = ui
        target = DataFrame.iloc[1:, 0]
        # 将剩余的列作为数据 (features)
        data = DataFrame.iloc[1:, 1:]
        self.finalData = data  # 读取数据
        self.target = target  # 读取标签名

    def LG(self, test_size):
        x_train, x_test, y_train, y_test = (  # 划分训练集与测试集
            train_test_split(self.finalData, self.target, test_size = test_size, random_state=0))

        # 搭建逻辑回归模型
        lg = LogisticRegression()
        x_train = np.asarray(x_train)
        y_train = np.asarray(y_train)
        x_test = np.asarray(x_test)
        lg.fit(x_train, y_train)

        # 预测数据结果及准确率
        y_pred = lg.predict(x_test)
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
                # print(f"类别 {label} 没有被预测到，精度为 0")
        return accuracy, confusion, classification, err_str
        # print("模型准确率", accuracy_score(y_test, y_pred))
        # print("混淆矩阵", confusion_matrix(y_test, y_pred))
        # print("分类报告", classification_report(y_test, y_pred))