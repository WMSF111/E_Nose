import os, glob, global_var,  logging, ast
import data_file.filter as filter
import pandas as pd
import numpy as np
import matplotlib.pyplot as pl
logging.getLogger('matplotlib.font_manager').setLevel(logging.WARNING)



class DATAFRAME_TO():
    def __init__(self, df):
        self.df = df
    def listheader(self): # 获取列头作为列表
        header = self.df.columns.tolist()  # 获取Dataframe的列名，并转换为列表
        return header  # 返回结果，一个字典和一个列表

    def csv(self, folders):
        if global_var.folders != ' ':
            self.df.to_csv(folders,index=False) # 不保存dataframe索引



class UI_TXT_TO():
    # 遍历有resource文件夹的文件夹中的.txt合并成带文件名的trainfile.txt存在train文件夹中
    def unit_traintxt(script_dir):
        print("running write_traintxt")
        # 查找指定目录下所有扩展名为 .txt 的文件，并将这些文件的路径存储到 self.train_files 列表中。
        path_folder = glob.glob(os.path.join(script_dir + '\\resource\\*.txt'))
        global_var.trainfile_txt_path = os.path.join(script_dir + "\\train\\trainfile.txt")  # 中间存储的.txt路径
        if os.path.exists(global_var.trainfile_txt_path): # 如果存在该路径,进行去除
            os.remove(global_var.trainfile_txt_path)
            print("remove")
        # 读取文件夹，将.txt合并成一个,第一列是文件名
        with open(global_var.trainfile_txt_path, "a") as outfile:
            # 第一行是列名
            with open(path_folder[0], 'r') as infile: # 写入列名
                trainfile_txt_text = infile.read()
                rows = trainfile_txt_text.split('\n')  # 每行代表表格中的一行数据
                table_data1 = [row.split(' ') for row in rows]  # 假设每列用空格分隔
                data = []
                if(len(global_var.headers_list) == 0): # 当不存在列名
                    global_var.headers_list.append("target")
                    for i in range(0, len(table_data1[0])):
                        global_var.headers_list.append(global_var.sensors[i])
            headers_str = " ".join(map(str, global_var.headers_list))
            outfile.write(headers_str + '\n')
            #遍历所有文件
            for file_path in path_folder:
                file_name = os.path.basename(file_path).replace(".txt", "")
                with open(file_path, 'r') as infile:
                    lines = infile.readlines()  # 读取每个文件的所有行
                    for line in lines:
                        stripped = line.rstrip()  # 去掉行尾空白和换行
                        if not stripped:  # 空行直接跳过
                            print(f"{file_name} 有空行")
                            continue
                        # 确保每一行最后都有且只有一个 \n
                        outfile.write(f"{file_name} {stripped}\n")

    def txt_to_dataframe(the_path):
        # 读取trainfile.txt并显示到数据源看板，将.txt存储为dataFrame
        with open(the_path, 'r') as file: # 显示列名
            trainfile_txt_text = file.read()
        text = trainfile_txt_text
        if len(text) >= 4:  # 显示所有数据
            rows = text.split('\n')  # 每行代表表格中的一行数据
            # table_data = [row.split(' ') for row in rows]  # split() 自动处理多个空格,转化为列表
            table_data = [row.split() for row in rows]  # 默认按空白字符分割，去除多余空格
            data = []
            for row in table_data[1:]:  # 从第二行开始（去掉标题行）
                # 检查是否是空行，如果是空行则跳过
                if not any(row):  # 如果整行没有任何有效数据
                    continue
                data_row = []
                for value in row:
                    try:
                        # 尝试转换为整数，如果失败则转换为浮动数
                        data_row.append(int(value))
                    except ValueError:
                        try:
                            data_row.append(float(value))  # 如果整数转换失败，尝试浮动数
                        except ValueError:
                            data_row.append(value)  # 如果两者都无法转换，保留原始字符串
                data.append(data_row)

            print("Columns:", table_data[0])
            return pd.DataFrame(data, columns=table_data[0])

    def txt_to_Array(the_path):
        # 读取txt文件中的数据，返回第一列标签，和后面的数据
        with open(the_path, 'r') as file:
            lines = file.readlines()

        # 初始化存储第一列和从第二列开始的列的空数组
        first_column = []
        remaining_columns = []
        print("lines:", lines)

        # 假设 lines 是每行数据的列表
        for line in lines[1:]: # 从第二行开始
            line = line.strip()  # 清除行末的换行符
            row_data = line.split()  # 将每行按空格分割

            # 第一列是字符串
            first_column.append(row_data[0])  # row_data[0] 是第一列的字符串数据

            # 将从第二列开始的数据转换为浮动数，并存入 remaining_columns
            remaining_columns.append([float(x) for x in row_data[1:]])  # 转换为浮动数
        return first_column, remaining_columns


    def Choose_Filter_Alg(self, filter_preprocess):
        # data = global_var.textEdit_DataFrame.iloc[1:, 1:].copy()  # 获取数据部分（去除列头和行头）
        data = global_var.textEdit_DataFrame
        for column in data.columns: # 按列处理, column 是当前列的列名
            column_data = data[column].astype(int).tolist()
            if filter_preprocess == "算术平均滤波法":
                # window_size: 窗口大小，用于计算中位值，输入整数，越小越接近原数据
                result = filter.ArithmeticAverage(column_data.copy(), 2)
            elif filter_preprocess == "递推平均滤波法":
                result = filter.SlidingAverage(column_data.copy(), 2)
            elif filter_preprocess == "中位值平均滤波法":
                result = filter.MedianAverage(column_data.copy(), 2)
            elif filter_preprocess == "一阶滞后滤波法":
                # 滞后程度决定因子，0~1（越大越接近原数据）
                result = filter.FirstOrderLag(column_data.copy(), 0.9)
            elif filter_preprocess == "加权递推平均滤波法":
                # 平滑系数，范围在0到1之间（越大越接近原数据）
                result = filter.WeightBackstepAverage(column_data.copy(), 0.9)
            elif filter_preprocess == "消抖滤波法":
                # N:消抖上限,范围在2以上。
                result = filter.ShakeOff(column_data.copy(), 4)
            elif filter_preprocess == "限幅消抖滤波法":
                # Amplitude:限制最大振幅,范围在0 ~ ∞ 建议设大一点
                # N:消抖上限,范围在0 ~ ∞
                result = filter.AmplitudeLimitingShakeOff(column_data.copy(), 200, 3)
            # data.iloc[1:, data.columns.get_loc(column)] = result
            data[column] = result #将滤波后的数据替换原数据

        # 将处理结果放回到原数据中
        global_var.textEdit_DataFrame.iloc[1:, 1:] = data
        global_var.textEdit_nolc_DataFrame = global_var.textEdit_DataFrame.iloc[1:, 1:]
        # # 删除第一行(获取无列头数据):无header数据
        # global_var.file_text_nolc_DataFrame = global_var.textEdit_DataFrame.drop(0)  # 0 是第一行的索引
        # # 删除第一列
        # global_var.file_text_nolc_DataFrame = global_var.textEdit_DataFrame.drop(
        #     global_var.file_text_nolc_DataFrame.columns[0], axis=1)  # df.columns[0] 是第一列的名称
        self.ui.tab1.textEdit.clear()
        self.ui.tab1.textEdit.append(global_var.textEdit_DataFrame.to_string(index=False))
        self.text = self.ui.tab1.textEdit.toPlainText()
        pl.title(global_var.filter_preprocess)
        pl.subplot(2, 1, 1)
        pl.plot(column_data)
        pl.subplot(2, 1, 2)
        pl.plot(result)
        pl.show()
