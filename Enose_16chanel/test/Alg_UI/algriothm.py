import numpy as np
import pandas as pd
from sklearn.preprocessing import scale
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.decomposition import PCA
from factor_analyzer.factor_analyzer import calculate_bartlett_sphericity
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.utils.multiclass import unique_labels
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
import statsmodels.api as sm
import global_var as global_var

class choose_alg():
    def __init__(self, ui, textEdit_DataFrame):
        self.ui = ui
        self.df = textEdit_DataFrame  # 读取文件
        # 初始化一个三维图像
        self.fig = plt.figure()
        # self.finalData = 0
        # self.name = []
        # self.num = 3
        # self.target = self.df['target'].values  # numpy.ndarray
        self.data = pd.DataFrame(self.df.iloc[:, 1:])
        # self.confusion_matrix = self.accuracy_score = self.classification_report = ' '
        # self.choose_al(self.data, 3)
        # if self.num != 0:
        #     self.train_data()



    def choose_al(self, al, num):
        print(al)
        if (al == "LDA"):
            self.lda(num)
        if (al == "PCA"):
            self.pca(num)
        if (al == "OLS"):
            self.OLS(self.df)

    def OLS(self, data):
        cols = global_var.headers[1:]
        # print(cols)
        for i in range(0, len(cols)):
            data1 = data[cols]
            x = sm.add_constant(data1)  # 生成自变量
            y = data['target']  # 生成因变量
            model = sm.OLS(y, x)  # 生成模型
            result = model.fit()  # 模型拟合
            print(result.summary())  # 模型描述
            pvalues = result.pvalues  # 得到结果中所有P值
            pvalues.drop('const', inplace=True)  # 把const取得
            pmax = max(pvalues)  # 选出最大的P值
            if pmax > 0.05:
                ind = pvalues.idxmax()  # 找出最大P值的index
                cols.remove(ind)  # 把这个index从cols中删除
            else:
                self.finalData = result
                break
    def pca(self, num,  target_variance=80):
        target_variance = target_variance / 100
        # 标准化数据
        scaler = StandardScaler()

        data_scaled = scaler.fit_transform(self.data)

        # 应用 PCA
        pca_f = PCA(n_components=num, svd_solver="full")
        pca_f = pca_f.fit(data_scaled)
        self.finalData = pca_f.transform(data_scaled)
        df = pd.DataFrame(self.finalData) # 转化成DataFrame
        df.insert(0, 'target', self.df['target'].values)# 将 new_column 添加到 DataFrame 的第一列
        self.finalData = df.to_numpy()# 如果需要，你可以将 df 转回 NumPy 数组


        variance_ratios = pca_f.explained_variance_ratio_  # 贡献率

        cumulative_variance_ratios = np.cumsum(variance_ratios) # 计算累积贡献率
        # 将累积贡献率转换为字符串并追加到 QTextBrowser
        cumulative_variance_ratios_str = ', '.join(map(str, cumulative_variance_ratios))

        self.ui.textBrowser.clear()
        # 将主成分个数转换为字符串并追加到 QTextBrowser
        self.ui.textBrowser.append('主成分个数: ' + str(len(variance_ratios)))
        self.ui.textBrowser.append('累计贡献率：' + cumulative_variance_ratios_str)
        print(cumulative_variance_ratios[-1])
        if cumulative_variance_ratios[-1] > target_variance:
            # 找到累积贡献率达到目标值的最小主成分数
            num_components = np.argmax(cumulative_variance_ratios >= target_variance) + 1
            # 追加需要的主成分数和累积贡献率
            self.ui.textBrowser.append(
                f"\n需要 {num_components} 个主成分才能达到累积贡献率 {target_variance * 100:.2f}% 以上。")
        else:
            self.ui.textBrowser.append(
                f"\n {num} 个主成分无法达到累积贡献率 {target_variance * 100:.2f}% 以上，请增加维度尝试，或者切换算法。")
        return self.finalData, variance_ratios


    def lda(self, num, target_variance):
        lda_model = LinearDiscriminantAnalysis(n_components=num)
        self.finalData = lda_model.fit_transform(self.data, self.df['target'].values)
        df = pd.DataFrame(self.finalData)  # 转化成DataFrame
        df.insert(0, 'target', self.df['target'].values)  # 将 new_column 添加到 DataFrame 的第一列
        self.finalData = df.to_numpy()  # 如果需要，你可以将 df 转回 NumPy 数组

        # 获取解释方差比
        explained_variance_ratio = lda_model.explained_variance_ratio_
        sum_explained_variance_ratio = np.cumsum(explained_variance_ratio)
        # 将数据转换到投影空间
        transformed_data = lda_model.transform(self.data)
        # 计算类内散布矩阵
        Sw = np.cov(transformed_data.T)
        #    计算类间散布矩阵
        means_diff = (lda_model.means_[1] - lda_model.means_[0]).reshape(-1, 1)
        SB = np.outer(means_diff, means_diff)
        # 计算类间散布与类内散布之比
        inter_intra_ratio = np.trace(SB) / np.trace(Sw)

        self.ui.textBrowser.clear()
        # 将主成分个数转换为字符串并追加到 QTextBrowser
        self.ui.textBrowser.append('解释方差比: ' + str(explained_variance_ratio))
        self.ui.textBrowser.append("解释方差比之和: " + str(sum_explained_variance_ratio))
        self.ui.textBrowser.append("类间散布与类内散布之比: " + str(inter_intra_ratio))
        print(sum_explained_variance_ratio[-1])
        if sum_explained_variance_ratio[-1] * 100 > target_variance :
            # 找到累积贡献率达到目标值的最小主成分数
            num_components = np.argmax(sum_explained_variance_ratio >= target_variance) + 1
            # 追加需要的主成分数和累积贡献率
            self.ui.textBrowser.append(
                f"\n需要 {num_components} 个主成分才能达到累积贡献率 {target_variance:.2f}% 以上。")
        else:
            self.ui.textBrowser.append(
                f"\n {num} 个主成分无法达到累积贡献率 {target_variance:.2f}% 以上，请增加维度尝试，或者切换算法。")

        return self.finalData, explained_variance_ratio

class TRAIN():
    # 输入： finalData=数据级 target =数据标签 test_size = 训练集数量（0.1-0.9）
    def __init__(self, ui, target, data):
        self.ui = ui
        self.finalData = data  # 读取数据
        self.target = target  # 读取标签

    def LG_train(self, test_size):
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

