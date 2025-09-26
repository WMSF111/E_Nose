headers_list = [] # 列头列表
textEdit_DataFrame = ' ' # 编辑框的文字
textEdit_nolc_DataFrame = ' ' # 编辑框内无列头行头数据
folders = ' '
trainfile_txt_path = ' ' # 训练集路径
header_trainfile_txt_path = ' ' # 训练集路径
folder_path = ' '
# 算法
filter_preprocess = ' '

thepos = [[0,0,0],
    [944, 3184, 15480]]
posxyz = [
    [0,0,0],
    [944, 3184, 1548],
    [1536, 3184, 1548],
    [960, 18943, 1548],
    [1728, 19455, 1548],
]

# posxyz = [
#     [0,0,0],
#     [944, 1433, 5000],
#     [1536, 1433, 5000],
#     [944, 18943, 5000],
#     [1536, 18943, 5000],
#     [944, 38911, 5000],
#     [1536, 38911, 5000],
#     [944, 55295, 5000],
#     [1536, 55295, 5000],
#     [2377, 55295, 5000],
#     [3328, 55295, 5000],
#     [2377, 38911, 5000],
#     [3328, 38911, 5000],
#     [2377, 18943, 5000],
#     [3328, 18943, 5000],
#     [2377, 1433, 5000],
#     [3328, 1433, 5000]
# ]



Com_select = " "
Port_select = ""
Bund_select = 115200
now_temp = 1.0
target_temp = 0
target_temp_time = 0
room_temp = 1
channal = [0, 4,3,2,1,5,6,7,8]
now_chan = 1
now_Sam = 0
target_Sam = 1

Port_select2 = ""
Bund_select2 = 9600
Save_flag = 0


sensors = [
    "sensor1", "sensor2", "sensor3", "sensor4", "sensor5",
    "sensor6", "sensor7", "sensor8", "sensor9", "sensor10",
    "sensor11", "sensor12", "sensor13", "sensor14", "sensor15",
    "sensor16"
]