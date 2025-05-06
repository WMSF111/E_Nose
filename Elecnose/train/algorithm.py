import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.preprocessing import scale
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.decomposition import PCA
from factor_analyzer.factor_analyzer import calculate_bartlett_sphericity
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_wine
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
import statsmodels.api as sm
import global_vars
import Picture.Show_pic as Show_pic


class alg():
    def __init__(self, df):
        self.df = df  # 读取文件
        # 初始化一个三维图像
        self.fig = plt.figure()
        self.finalData = 0
        self.name = []
        self.num = 3
        self.target = self.df['target'].values  # numpy.ndarray
        self.data = pd.DataFrame(self.df.iloc[:, 1:])
        self.confusion_matrix = self.accuracy_score = self.classification_report = ' '
        # self.choose_al(self.data)
        # Show_pic.draw_line(self.name, self.num)
        # if self.num != 0:
        #     self.train_data()

    def choose_al(self, al, num):
        self.num = num
        if (al == "LDA"):
            self.lda(self.data, self.num)
        # self.finalData = LinearDiscriminantAnalysis(n_components = self.num).fit_transform(data, self.target)
        if (al == "my_LDA"):
            self.my_lda(self.data, self.num)
        if (al == "PCA"):
            self.pca(self.data, self.num)
        if (al == "my_PCA"):
            self.my_pca(self.data, self.num)
        if (al == "OLS"):
            self.OLS(self.df)

    def OLS(self, data):
        cols = global_vars.headers[1:]
        print(cols)
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

    def train_data(self):
        x_train, x_test, y_train, y_test = train_test_split(self.finalData, self.target, test_size=0.2, random_state=0)
        # 逻辑回归模型
        lg = LogisticRegression()
        x_train = np.asarray(x_train)
        y_train = np.asarray(y_train)
        x_test = np.asarray(x_test)
        lg.fit(x_train, y_train)
        y_pred = lg.predict(x_test)

        self.accuracy_score = accuracy_score(y_test, y_pred)
        self.confusion_matrix = confusion_matrix(y_test, y_pred)
        self.classification_report = classification_report(y_test, y_pred)

        # print("模型准确率",accuracy_score(y_test,y_pred))
        # print("混淆矩阵",confusion_matrix(y_test,y_pred))
        # print("分类报告",classification_report(y_test,y_pred))

    def pca(self, data, num):
        pca_f = PCA(n_components=num, svd_solver="full")
        pca_f = pca_f.fit(data)
        self.finalData = pca_f.transform(data)
        variance_ratios = pca_f.explained_variance_ratio_
        print(pca_f.explained_variance_ratio_)
        # 计算累积贡献率
        cumulative_variance_ratios = np.cumsum(variance_ratios)
        print('主成分个数', len(variance_ratios))
        print('贡献率：', variance_ratios)
        print('累计贡献率：', cumulative_variance_ratios)

    def my_pca(self, data, num):
        chi_value, p_value = calculate_bartlett_sphericity(data)  # 检验各个变量是否独立
        data.info()
        print(chi_value, p_value)
        data_scale = scale(data)  # 数据标准化
        CovX = np.around(np.corrcoef(data.T), decimals=3)  # 相关系数矩阵
        featValue, featVec = np.linalg.eig(CovX.T)  # 求特征值featValue与特征向量featVec，特征值默认从大到小排序
        featValue = sorted(featValue, reverse=True)  # 对特征值进行排序输出
        s = 0
        sum = 0
        cr = []  # 累计贡献率
        pc = []  # 主成分
        for i in range(len(featValue)):
            pc.append(i)
            sum += 1
            contri = featValue[i] / np.sum(featValue)  # 第i主成分贡献率(度)
            cr.append(contri)
            self.name.append(data.columns[i])
            s += contri  # 累计贡献率
            if sum == num:
                break
            # if s >= 0.8: #累计贡献率达80%即停止
            #     break
        for i in range(sum):
            selectVec = np.asarray(featVec.T[pc]).T
            selectVec = selectVec * (-1)
            self.finalData = np.dot(data_scale, selectVec)
        print('主成分名称：', self.name)
        print('主成分个数：', sum)
        print('贡献率：', cr)
        print('累计贡献率：', s)

    def lda(self, data, num):
        lda_model = LinearDiscriminantAnalysis(n_components=num)
        self.finalData = lda_model.fit_transform(data, self.target)
        # 获取解释方差比
        explained_variance_ratio = lda_model.explained_variance_ratio_
        print("解释方差比: ", explained_variance_ratio)
        print("解释方差比之和: ", np.cumsum(explained_variance_ratio))

        # 将数据转换到投影空间
        transformed_data = lda_model.transform(data)
        # 计算类内散布矩阵
        Sw = np.cov(transformed_data.T)
        #    计算类间散布矩阵
        means_diff = (lda_model.means_[1] - lda_model.means_[0]).reshape(-1, 1)
        SB = np.outer(means_diff, means_diff)

        # 计算类间散布与类内散布之比
        inter_intra_ratio = np.trace(SB) / np.trace(Sw)
        print("类间散布与类内散布之比: ", inter_intra_ratio)

    def my_lda(self, data, num):
        clusters = np.unique(self.target)
        name = []  # 主成分名称
        if num > len(clusters) - 1:
            print("K is too much")
            print("please input again")
            exit(0)

        Sw = np.zeros((data.shape[1], data.shape[1]))
        for i in clusters:
            datai = data[self.target == i]
            datai = datai - datai.mean(0)
            Swi = np.mat(datai).T * np.mat(datai)
            Sw += Swi

        # between_class scatter matrix
        SB = np.zeros((data.shape[1], data.shape[1]))
        u = data.mean(0)  # 所有样本的平均值
        for i in clusters:
            Ni = data[self.target == i].shape[0]
            ui = data[self.target == i].mean(0)  # 某个类别的平均值
            SBi = Ni * np.mat(ui - u).T * np.mat(ui - u)
            SB += SBi
        S = np.linalg.inv(Sw) * SB
        eigVals, eigVects = np.linalg.eig(S)  # 求特征值，特征向量
        eigValInd = np.argsort(eigVals)
        eigValInd = eigValInd[:(-num - 1):-1]
        w = eigVects[:, eigValInd]
        self.finalData = np.dot(data, w)
        total_variance = np.sum(eigVals)
        explained_variance = eigVals / total_variance
        print("解释方差比: ", explained_variance)
        print("解释方差比之和: ", np.cumsum(explained_variance)[0:num])
        inter_intra_ratio = np.trace(SB) / np.trace(Sw)
        print("类间散布与类内散布之比: ", inter_intra_ratio)
        # self.draw_line(name, num)

        return self.finalData


