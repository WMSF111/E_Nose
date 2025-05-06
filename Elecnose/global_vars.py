import pandas as pd
from functools import reduce

file_csv = []
file_text_DataFrame = []
file_text = []
noheader_file = []
headers_str = ""
headers_list = []
file_text_nolc_DataFrame = []

folders = []

file_csv_path = 0
file_txt_path = 0

df_dataframe = 0
result_df = 0
headers_flag = 0

color = ["light","dark","white","chalk","essos","infographic","macarons","purple-passion","roma","romantic","shine","vintage","walden","westeros","wonderland","halloween"]


selected_value1, selected_index1 = 0,0
selected_value2, selected_index2 = 0,0
selected_value3, selected_index3 = 0,0
selected_value4, selected_index4 = 0,0
selected_value5, selected_index5 = 0,0
color_flag_1 = 0
color1 = 0

selected_value1_2, selected_index1_2 = 0,0
selected_value2_2, selected_index2_2 = 0,0
selected_value3_2, selected_index3_2 = 0,0
selected_value4_2, selected_index4_2 = 0,0
selected_value5_2, selected_index5_2 = 0,0
color_flag_2 = 0
color2 = 0

selected_value1_3, selected_index1_3 = 0,0
selected_value2_3, selected_index2_3 = 0,0
selected_value3_3, selected_index3_3 = 0,0
selected_value4_3, selected_index4_3 = 0,0
selected_value5_3, selected_index5_3 = 0,0
color_flag_3 = 0
color3 = 0

selected_value1_4, selected_index1_4 = 0,0
selected_value2_4, selected_index2_4 = 0,0
selected_value3_4, selected_index3_4 = 0,0
selected_value4_4, selected_index4_4 = 0,0
selected_value5_4, selected_index5_4 = 0,0
color_flag_4 = 0
color4 = 0



def merge_and_keep_common_rows(df, *dataframes):
    
    # 合并所有传入的 DataFrame
    dfs = [df] + list(dataframes)
    print(type(dfs))
    merged_df = reduce(lambda left, right: pd.merge(left, right, on=list(left.columns), how='inner'), dfs)
    
    # # 删除合并后数据框的第一行
    # result_df = merged_df.drop(0)
    
    return merged_df

# result_df = merge_and_keep_common_rows(df, df_1, df_2, df_3, df_4, df_5, df_6)

