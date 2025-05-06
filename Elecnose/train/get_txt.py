import pandas as pd
from scipy import stats
import os, global_vars, glob
import numpy as np
import scipy.signal as signal
import train.filter as filter
import matplotlib.pyplot as pl


class Get_txt():
    def __init__(self, folder_path, ui):
        self.df = []
        self.ui = ui
        # 使用 glob 模块获取文件夹中所有 .txt 文件的路径列表
        # txt_files = glob.glob(os.path.join(folder_path, '*.txt'))
        self.write_traintxt(folder_path)
        self.the_main()

    def write_traintxt(self, script_dir):  # 遍历文件夹的.txt合并成带文件名的.txt
        self.train_files = glob.glob(os.path.join(script_dir + "\\resource", '*.txt'))
        global_vars.trainfile_txt_path = os.path.join(script_dir + "\\train\\trainfile.txt")  # 中间存储的.txt
        if os.path.exists(global_vars.trainfile_txt_path):
            os.remove(global_vars.trainfile_txt_path)
            print("remove")
        # 读取文件夹，将.txt合并成一个
        with open(global_vars.trainfile_txt_path, "a") as outfile:
            # outfile.write("target ")
            for file_path in self.train_files:
                file_name = os.path.basename(file_path).replace(".txt", "")
                with open(file_path, 'r') as infile:
                    lines = infile.readlines()  # 读取每个文件的所有行
                    for line in lines:
                        line_with_file_name = f"{file_name} {line}"  # 在每行开头添加文件名
                        outfile.write(line_with_file_name)

    def the_main(self):
        # 读取trainfile.txt并显示到数据源看板，将.txt存储为dataFrame
        with open(global_vars.trainfile_txt_path, 'r') as file:
            global_vars.file_text = file.read()
            rows = global_vars.file_text.split('\n')  # 每行代表表格中的一行数据
            table_data1 = [row.split(' ') for row in rows]  # 假设每列用逗号分隔
            data = []
            global_vars.headers_str = "target"
            for i in range(1, len(table_data1[0])):
                global_vars.headers_str = global_vars.headers_str + " " + str(i)
        self.ui.tab1.textEdit.append(global_vars.headers_str)
        self.ui.tab1.textEdit.append(global_vars.file_text)
        text = self.ui.tab1.textEdit.toPlainText()
        # train.turn_to_csv(text)
        if len(text) >= 4:
            rows = text.split('\n')  # 每行代表表格中的一行数据
            table_data = [row.split(' ') for row in rows]  # 假设每列用逗号分隔
            num_cols = len(table_data[0])
            data = []
            for i in range(1, len(rows) - 1):
                # if len(table_data[i]) == num_cols:
                data.append(table_data[i])
        global_vars.file_text_DataFrame = pd.DataFrame(data, columns=table_data[0])  # 保存创建的 DataFrame

    def choose_1(self):
        File = global_vars.file_text_DataFrame
        print(File)
        train_data = np.array(File)  # 先将数据框转换为数组
        train_data_list = train_data.tolist()  # 其次转换为列表
        T = np.arange(0, 0.5, 1 / 4410.0)
        num = signal.chirp(T, f0=10, t1=0.5, f1=1000.0)
        File2 = File
        # 获取数据部分（去除列头和行头）
        data = File.iloc[1:, 1:].copy()  # 假设第0行和第0列是头部信息

        for column in data.columns:
            column_data = data[column].astype(int).tolist()
            if global_vars.preprocess == "算术平均滤波法":
                # window_size: 窗口大小，用于计算中位值，输入整数，越小越接近原数据
                result = filter.ArithmeticAverage(column_data.copy(), 2)
                # window_size: 窗口大小，用于计算中位值，输入整数，越小越接近原数据
            elif global_vars.preprocess == "递推平均滤波法":
                result = filter.SlidingAverage(column_data.copy(), 2)
            elif global_vars.preprocess == "中位值平均滤波法":
                result = filter.MedianAverage(column_data.copy(), 2)
            elif global_vars.preprocess == "一阶滞后滤波法":
                # 滞后程度决定因子，0~1（越大越接近原数据）
                result = filter.FirstOrderLag(column_data.copy(), 0.9)
            elif global_vars.preprocess == "加权递推平均滤波法":
                # 平滑系数，范围在0到1之间（越大越接近原数据）
                result = filter.WeightBackstepAverage(column_data.copy(), 0.9)
            elif global_vars.preprocess == "消抖滤波法":
                # N:消抖上限,范围在2以上。
                result = filter.ShakeOff(column_data.copy(), 4)
            elif global_vars.preprocess == "限幅消抖滤波法":
                # Amplitude:限制最大振幅,范围在0 ~ ∞ 建议设大一点
                # N:消抖上限,范围在0 ~ ∞
                result = filter.AmplitudeLimitingShakeOff(column_data.copy(), 200, 3)
            # data.iloc[1:, data.columns.get_loc(column)] = result
            data[column] = result

        # 将处理结果放回到原数据中
        File.iloc[1:, 1:] = data
        global_vars.file_text_DataFrame = File
        # File2[column] = column_data
        # 删除第一行
        global_vars.file_text_nolc_DataFrame = global_vars.file_text_DataFrame.drop(0)  # 0 是第一行的索引
        # 删除第一列
        global_vars.file_text_nolc_DataFrame = global_vars.file_text_DataFrame.drop(
            global_vars.file_text_nolc_DataFrame.columns[0], axis=1)  # df.columns[0] 是第一列的名称
        self.ui.tab1.textEdit.clear()
        self.ui.tab1.textEdit.append(global_vars.file_text_DataFrame.to_string(index=False))
        self.text = self.ui.tab1.textEdit.toPlainText()
        pl.subplot(2, 1, 1)
        pl.plot(column_data)
        pl.subplot(2, 1, 2)
        pl.plot(result)
        pl.show()


class standard():
    def __init__(self, data):
        self.data = data
        self.row_data = []
        for column in self.data:
            column_data = self.data[column].astype(int)
            # column_data = self.data[column].values.astype(int).tolist()
            self.row_data.append(self.choose_1(column_data))

    def choose_1(self, column_data):
        file_path = os.path.join(str(global_vars.folders[0]), 'train', 'trainfile.csv')
        File = pd.read_csv(file_path, skiprows=1, usecols=range(1, pd.read_csv(file_path, nrows=1).shape[1]))
        # 重新设置 DataFrame 的索引
        File.reset_index(drop=True, inplace=True)
        train_data = np.array(File)  # 先将数据框转换为数组
        train_data_list = train_data.tolist()  # 其次转换为列表
        T = np.arange(0, 0.5, 1 / 4410.0)
        num = signal.chirp(T, f0=10, t1=0.5, f1=1000.0)
        File2 = File
        for column in File:
            column_data = File[column].astype(int)
            column_data = column_data.tolist()
            if global_vars.preprocess == "算术平均滤波法":
                # window_size: 窗口大小，用于计算中位值，输入整数，越小越接近原数据
                result = filter.ArithmeticAverage(column_data.copy(), 2)
                # window_size: 窗口大小，用于计算中位值，输入整数，越小越接近原数据
            elif global_vars.preprocess == "递推平均滤波法":
                result = filter.SlidingAverage(column_data)
            elif global_vars.preprocess == "中位值平均滤波法":
                result = filter.MedianAverage(column_data.copy(), 2)
            elif global_vars.preprocess == "一阶滞后滤波法":
                # 滞后程度决定因子，0~1（越大越接近原数据）
                result = filter.FirstOrderLag(column_data.copy(), 0.9)
            elif global_vars.preprocess == "加权递推平均滤波法":
                # 平滑系数，范围在0到1之间（越大越接近原数据）
                result = filter.WeightBackstepAverage(column_data.copy(), 0.9)
            elif global_vars.preprocess == "消抖滤波法":
                # N:消抖上限,范围在2以上。
                result = filter.ShakeOff(column_data.copy(), 3)
            elif global_vars.preprocess == "限幅消抖滤波法":
                # Amplitude:限制最大振幅,范围在0 ~ ∞ 建议设大一点
                # N:消抖上限,范围在0 ~ ∞
                result = filter.ShakeOff(column_data.copy(), 2000, 50)
            print(len(result))
            File2[column] = column_data


