import pandas as pd
import os, glob
import train.algorithm as algorithm
import global_vars

class txt_to_csv(): #遍历文件夹的.txt合并成带文件名的.txt
    def __init__(self, script_dir):
        # 使用 glob 模块获取文件夹中所有 .txt 文件的路径列表
        self.csv = []
        # script_dir = os.path.dirname(__file__)
        self.train_files = glob.glob(os.path.join(script_dir + "\\resource_ui", '*.txt'))
        global_vars.trainfile_txt_path = os.path.join(script_dir + "\\train\\trainfile.txt") #中间存储的.txt
        # self.write_traintxt()
        # self.turn_to_csv()
        
    def write_traintxt(self):   
        if os.path.exists(global_vars.trainfile_txt_path):
            os.remove(global_vars.trainfile_txt_path)
            print("remove")
        #读取文件夹，将.txt合并成一个  
        with open(global_vars.trainfile_txt_path, "a") as outfile:
            # outfile.write("target ")
            for file_path in self.train_files:
                file_name = os.path.basename(file_path).replace(".txt", "")
                with open(file_path, 'r') as infile:
                    lines = infile.readlines()  # 读取每个文件的所有行
                    for line in lines:
                        line_with_file_name = f"{file_name} {line}"  # 在每行开头添加文件名
                        outfile.write(line_with_file_name)
        
class turn_to_csv():
    def __init__(self, text):
        # with open(self.The_path, 'r') as file:
        #     text = file.read()
        rows = text.split('\n')  # 每行代表表格中的一行数据
        table_data = [row.split(' ') for row in rows]  # 假设每列用逗号分隔
        num_cols = len(table_data[0])
        line1 = []
        line1.append("target")
        for i in range(1, num_cols):
            line1.append(str(i))
        data = []
        for i in range(1, len(table_data)):
            if len(table_data[i]) == num_cols:
                data.append(table_data[i])
        self.csv = pd.DataFrame(data)  # 保存创建的 DataFrame
        print(self.csv)
        # self.csv = pd.DataFrame(data, columns=None)  # 保存创建的 DataFrame,列头为line1
        self.csv.to_csv(os.path.join(os.path.dirname(__file__) + '\\train\\trainfile.csv'), index=False, columns=None)

# txt_to_csv(os.path.dirname(__file__))
# df = pd.read_csv(os.path.join(os.path.dirname(__file__)) + '\\train\\trainfile.csv') #读取文件
# algorithm.pca(df)