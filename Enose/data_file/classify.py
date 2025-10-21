import numpy as np
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
from sklearn.neighbors import KNeighborsClassifier
import random


class TRAIN():
    # 输入： finalData=数据级 target =数据标签 test_size = 训练集数量（0.1-0.9）
    def __init__(self, ui, DataFrame):
        self.ui = ui
        self.target_map, self.target, self.data = read(DataFrame)  # 训练数据级、预测数据级
        self.num_target = transfer(self.target_map, self.target)  # 转化为数字target

    def svm(self, test_size, kernel_str, C):
        '''SVM 线性与非线性分类'''
        x_train, x_test, y_train, y_test = (  # 划分训练集与测试集
            train_test_split(self.data, self.target, test_size=test_size, random_state=1, stratify=self.target))
        x_train, x_test = standart(x_train, x_test)
        X_combine = np.vstack((x_train, x_test))  # 竖直堆叠数组
        y_combine = np.hstack((y_train, y_test))  # 水平拼接数组
        # ? 训练线性支持向量机
        svm = SVC(kernel=kernel_str, C=C, random_state=1)  # 定义线性支持向量分类器 (linear为线性核函数)
        svm.fit(x_train, y_train)  # 根据给定的训练数据拟合训练SVM模型
        y_pred = svm.predict(x_test)# 用训练好的分类器svm预测数据X_test_std的标签
        accuracy, confusion, classification, err_str = check_accuray(y_test,y_pred)
        return X_combine, y_combine, y_test, y_pred, svm, range(105, 150)

    # KNN预测函数
    def knn(self, test_size, alg, n_neighbors_num):
        num_target = transfer(self.target_map, self.target)  # 转化为数字target
        # 测试精度参数为n_neighbors
        x_train, x_test, y_train, y_test = (  # 划分训练集与测试集
            train_test_split(self.data, num_target, test_size=test_size, random_state=1, stratify=num_target))
        neigh = KNeighborsClassifier(n_neighbors=n_neighbors_num, algorithm = alg)
        neigh.fit(x_train, y_train)
        y_pred = neigh.predict(x_test)
        return y_pred, y_test

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


# 读取文件函数，数据预处理，70%做训练集，30%做预测集
def read(data):
    target = data.iloc[:, 0]  # 第一列类别
    # 将剩余的列作为数据 (features)
    data = data.iloc[:, 1:]  # 所有数据
    # 打乱顺序
    data = data.sample(frac=1).reset_index(drop=True)
    # 创建一个字典，将 target 中的每个元素映射到一个数字
    target_map = make_map(target)
    return target_map, target, data

def make_map(target):
    # 获取类别的排序列表，按照字母或其他顺序排序
    sorted_target = sorted(set(target))  # 获取唯一类别并排序

    # 创建一个字典，将 sorted_target 中的每个元素映射到一个数字，数字从0开始
    target_map = {sorted_target[i]: i for i in range(len(sorted_target))}
    return  target_map


# 将字符类型数据转化为数字类型
def transfer(target_map, array):
    # 使用映射字典转换 array 中的种类标签为数字
    num = [target_map[i] for i in array]
    return num

# 反转映射字典
def reverse_transfer(target_map, array):
    # 创建反向映射字典
    reverse_map = {v: k for k, v in target_map.items()}
    # 使用反向映射字典转换 array 中的数字标签为字符
    char = [reverse_map[i] for i in array]
    return char

def standart(x_train, x_test,):
    # ? 标准化训练集和测试集
    sc = StandardScaler()  # 定义一个标准缩放器
    sc.fit(x_train)  # 计算均值、标准差
    x_train = sc.transform(x_train)  # 使用计算出的均值和标准差进行标准化
    x_test = sc.transform(x_test)  # 使用计算出的均值和标准差进行标准化

    return x_train, x_test

def check_accuray(y_test, y_pred):
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
    return accuracy, confusion, classification, err_str