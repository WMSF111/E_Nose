import scipy.signal as signal
import numpy as np
import pylab as pl
import matplotlib.pyplot as plt
import os
import pandas as pd

script_dir = os.path.dirname(__file__)

def file_get():
    try:
        with open(script_dir + "./0507.txt", 'r') as file:
            text = file.read()

        if len(text) >= 4:
            rows = text.split('\n')  # 每行代表表格中的一行数据
            table_data = [row.split(' ') for row in rows]  # 假设每列用逗号分隔

            num_cols = len(table_data[0])
            data = []
            for i in range(0, len(table_data)):
                if len(table_data[i]) == num_cols:
                    data.append(table_data[i])

            file = pd.DataFrame(data, columns=table_data[0])  # 保存创建的 DataFrame
            return file
        else:
            print("文件内容太短，无法创建 DataFrame。")
            return None
    except FileNotFoundError:
        print("文件未找到。")
        return None
    except Exception as e:
        print("发生错误:", e)
        return None
    
 
'''
算术平均滤波法
参数：
    inputs: 输入信号的列表
    window_size: 窗口大小，用于计算中位值，输入整数，越小越接近原数据
返回：
    filtered_output: 滤波后的输出信号列表
'''
def ArithmeticAverage(inputs,window_size):
    filtered_output = []
	 # 对于每个窗口，计算窗口内数据的平均值并添加到输出列表中
    for i in range(len(inputs) - window_size + 1):
        window = inputs[i:i + window_size]
        window_average = sum(window) / window_size
        filtered_output.append(window_average)

    return filtered_output
 
'''
递推平均滤波法
参数：
    inputs: 输入信号的列表
    window_size: 窗口大小，用于计算中位值，输入整数，越小越接近原数据
返回：
    filtered_output: 滤波后的输出信号列表
'''
def SlidingAverage(inputs,window_size):
    filtered_output = []
    window_sum = sum(inputs[:window_size])  # 初始窗口内数据的总和

    # 初始窗口的平均值作为第一个输出
    filtered_output.append(window_sum / window_size)

    # 对于每个后续的数据点，利用递推公式更新窗口内数据的总和，并计算平均值
    for i in range(window_size, len(inputs)):
        window_sum = window_sum - inputs[i - window_size] + inputs[i]  # 更新窗口内数据的总和
        filtered_output.append(window_sum / window_size)  # 计算平均值并添加到输出列表中

    return filtered_output
 
'''
中位值平均滤波法
参数：
    inputs: 输入信号的列表
    window_size: 窗口大小，用于计算中位值，输入整数，越小越接近原数据
返回：
    filtered_output: 滤波后的输出信号列表
'''
def MedianAverage(inputs, window_size):

    filtered_output = []

    # 边缘情况处理：将前 window_size//2 个值复制到结果列表中
    for i in range(window_size // 2):
        filtered_output.append(inputs[i])

    # 对于每个窗口，计算中位值并将其添加到结果列表中
    for i in range(len(inputs) - window_size + 1):
        window = inputs[i:i + window_size]
        median_value = np.median(window)
        filtered_output.append(median_value)

    # 边缘情况处理：将后 window_size//2 个值复制到结果列表中
    for i in range(len(inputs) - window_size + 1, len(inputs)):
        filtered_output.append(inputs[i])

    return filtered_output

 
'''
一阶滞后滤波法
    方法：本次滤波结果=（1-a）*本次采样值+a*上次滤波结果。 
a:滞后程度决定因子，0~1（越大越接近原数据）
'''
def FirstOrderLag(inputs,a):
      
	filtered_output = inputs
	  
	tmpnum = inputs[0]							#上一次滤波结果
	for index,tmp in enumerate(inputs):
		filtered_output[index] = (1-a)*tmp + a*tmpnum
		tmpnum = tmp
	return filtered_output
 
'''
    加权递推平均滤波法
    参数：
    inputs: 输入信号的列表
    alpha: 平滑系数，范围在0到1之间（越大越接近原数据）
    返回：
    filtered_output: 滤波后的输出信号列表
'''
def WeightBackstepAverage(inputs, alpha):

    filtered_output = []
    filtered_output.append(inputs[0])  # 初始时，输出等于第一个输入值

    for i in range(1, len(inputs)):
        # 递推式：滤波后的当前值等于上一个滤波后的值乘以(1-alpha)，再加上当前输入值乘以alpha
        filtered_value = (1 - alpha) * filtered_output[-1] + alpha * inputs[i]
        filtered_output.append(filtered_value)

    return filtered_output
 
'''
消抖滤波法
    检查是否有连续N个不相同的元素，如果有，则将后续的元素设置为与这N个元素的第一个值。
N:消抖上限,范围在2以上。
'''
def ShakeOff(inputs,N):
    
	filtered_output = inputs

	usenum = filtered_output[0]								#有效值
	i = 0 											#标记计数器
	for index,tmp in enumerate(filtered_output):
		if tmp != usenum:	
			usenum = filtered_output[index - 1]				
			i = i + 1
			if i >= N:
				i = 0
				filtered_output[index] = usenum
		else:
			i = 0
	return filtered_output
 
'''
限幅消抖滤波法
    首先，它检查相邻元素之间的差值是否超过了给定的振幅（Amplitude），
	如果超过，则将该元素的值设为前一个元素的值。
	然后，它检查是否有连续N个相同的元素，如果有，则将后续的元素设置为与这N个元素相同的值。
Amplitude:限制最大振幅,范围在0 ~ ∞ 建议设大一点
N:消抖上限,范围在0 ~ ∞
'''
def AmplitudeLimitingShakeOff(inputs,Amplitude,N):
	filtered_output = inputs
	tmpnum = inputs[0]
	for index,newtmp in enumerate(filtered_output):
		if np.abs(tmpnum-newtmp) > Amplitude:
			print(np.abs(tmpnum-newtmp))
			filtered_output[index] = tmpnum
		tmpnum = filtered_output[index]
	usenum = filtered_output[0]
	i = 0
	for index2,tmp2 in enumerate(filtered_output):
		if tmp2 != usenum:
			usenum = filtered_output[index2]
			i = i + 1
			if i >= N:
				i = 0
				filtered_output[index2] = usenum
		else:
			i = 0
	return filtered_output

File = file_get()
train_data = np.array(File) #先将数据框转换为数组
train_data_list = train_data.tolist()  #其次转换为列表
T = np.arange(0, 0.5, 1/4410.0)
num = signal.chirp(T, f0=10, t1 = 0.5, f1=1000.0)
print(num)
File2 = file_get()
for column in File:
      column_data = File[column].astype(int)
      column_data = column_data.tolist()
      pl.subplot(2,1,1)
      pl.plot(column_data)
      result = AmplitudeLimitingShakeOff(column_data.copy(), 20, 5)
      print(len(result))
      #print(num - result
      pl.subplot(2,1,2)
      pl.plot(result)
      pl.show()
      File2[column] = column_data
print(File2)

