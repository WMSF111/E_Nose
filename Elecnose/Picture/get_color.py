from haishoku.haishoku import Haishoku
import tkinter as tk
from tkinter import filedialog
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as mcolors

def open_image():
    global hex_colors
    # 创建 Tkinter 应用程序窗口
    root = tk.Tk()
    root.withdraw()  # 隐藏窗口

    # 初始化 image 变量
    image = None

    # 打开文件对话框，让用户选择图片文件
    file_path = filedialog.askopenfilename()
    
    # 如果用户选择了文件，则将文件路径赋值给 image 变量
    if file_path:
        image = file_path

    haishoku = Haishoku.loadHaishoku(image)
    color_dict = haishoku.palette
    rgb_values = [(color[1][0], color[1][1], color[1][2]) for color in color_dict]

    # 转换 RGB 值为十六进制颜色代码
    hex_colors = ['#' + ''.join('{:02x}'.format(c) for c in rgb) for rgb in rgb_values]
    return hex_colors

def get_the_color(the_color, products):
    type_color = type(the_color)
    if type_color == str:
        the_color = plt.get_cmap(the_color)(np.linspace(0.2, 1, len(products)))
    elif len(the_color) < len(products):
        #函数返回一个颜色映射对象，它代表了从一组数值到颜色的映射关系。
        additional_colors = plt.get_cmap("Blues")(np.linspace(0.2, 1, len(products)-len(the_color)+1))
        # 将颜色数组转换为十六进制格式的字符串,接受一个 RGB 或 RGBA 颜色数组，并返回对应的十六进制字符串。
        hex_colors = [mcolors.rgb2hex(color) for color in additional_colors]
        the_color.extend(hex_colors)
    else:
        the_color
    return the_color

color_sing_tab = ["tab:blue","tab:orange","tab:green","tab:red"]
color_sing = ["blue",'orange',"green","red"]
color_Big = ["Blues","Oranges","Greens","Reds"]
