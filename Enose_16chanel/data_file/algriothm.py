import numpy as np
import pandas as pd
import data_file.filter as filter
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
import statsmodels.api as sm
import global_var as global_var

class choose_alg():
    def __init__(self, ui, textEdit_DataFrame):
        self.ui = ui
        self.df = textEdit_DataFrame  # 读取文件
        self.data = pd.DataFrame(self.df.iloc[:, 1:])

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

class Pre_Alg():
    def __init__(self, ui, textEdit_DataFrame, select):
        self.ui = ui
        self.select = select
        self.type = float
        self.data = textEdit_DataFrame.iloc[:, 1:].copy()  # 去除列头行头
        self.result = textEdit_DataFrame.copy()

    def Filter_Choose(self):
        for column in self.data.columns:
            column_data = self.data[column].to_numpy() # 转化为数组
            if self.select == "算术平均滤波法":
                # window_size: 窗口大小，用于计算中位值，输入整数，越小越接近原数据
                result = filter.ArithmeticAverage(column_data.copy(), 2)
                # window_size: 窗口大小，用于计算中位值，输入整数，越小越接近原数据
            elif self.select == "递推平均滤波法":
                result = filter.SlidingAverage(column_data.copy(), 2)
            elif self.select == "中位值平均滤波法":
                result = filter.MedianAverage(column_data.copy(), 2)
            elif self.select == "一阶滞后滤波法":
                # 滞后程度决定因子，0~1（越大越接近原数据）
                result = filter.FirstOrderLag(column_data.copy(), 0.9)
            elif self.select == "加权递推平均滤波法":
                # 平滑系数，范围在0到1之间（越大越接近原数据）
                result = filter.WeightBackstepAverage(column_data.copy(), 0.9)
            elif self.select == "消抖滤波法":
                # N:消抖上限,范围在2以上。
                result = filter.ShakeOff(column_data.copy(), 4)
            elif self.select == "限幅消抖滤波法":
                # Amplitude:限制最大振幅,范围在0 ~ ∞ 建议设大一点
                # N:消抖上限,范围在0 ~ ∞
                result = filter.AmplitudeLimitingShakeOff(column_data.copy(), 200, 3)
            # 将 result 列表中的元素显式转换为目标列的数据类型
            result = [self.result[column].dtype.type(value) for value in result]
            # 将处理后的数据直接更新回原始的 DataFrame
            self.result.iloc[:, self.result.columns.get_loc(column)] = result
        return self.result

    def Val_Choose(self): # 返回Dataframe
        self.result.set_index('target', inplace=True)
        self.result = self.result.apply(pd.to_numeric, errors='coerce') # 全部转化为数字
        if(self.select == "平均值"):
            df_new = self.result.groupby(self.result.index).median() # 按平均值新建dataframe
        elif(self.select == "中位数"):
            df_new = self.result.groupby(self.result.index).mean()
        elif(self.select == "众数"):
            # mode()，它会返回一个 DataFrame 或者 Series，包含每个组的众数（如果有多个众数，它会列出所有的众数）
            # iloc[0] 用来选取第一个众数（如果有多个众数）
            df_new = (self.result.groupby(self.result.index).
                      agg(lambda x: x.mode().iloc[0]))
        # self.result.iloc[:, 0].dtype：获取第一列数据类型
        df_new = df_new.astype(self.result.iloc[:, 0].dtype)
        # 取消索引，将 'target' 列恢复为普通列
        df_new.reset_index(inplace=True)
        return df_new


