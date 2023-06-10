#0.输入氧化铜或氧化铅生成字符串
# 1.利用split分割得到数组
# 2.转为np数组
# 3.转为dtype = float
# 4.利用array的15%为标准差，生成均值为0正态分布的数组
# 5.将原数组与新数组相加得到扰动数据
#6.写入txt
import numpy as np
import easygui
import random
box_string = easygui.enterbox('')#0.输入氧化铜或氧化铅生成字符串
# 1.利用split分割得到数组
array_box = box_string.split('\n')
# 2.转为np数组
array_box = np.array(array_box)
# 3.转为dtype = float
array_box = np.float32(array_box)
# 4.利用array的15%为标准差，生成均值为0正态分布的数组
error_box = array_box * 0.15
noise_box = error_box * np.random.normal(size=1)
# 5.将原数组与新数组相加得到扰动数据e
noise_num = noise_box + array_box
#6.写入txt
with open('扰动数据.txt',mode="w") as f:
    for i in noise_num:
        temp_string = str(i)
        f.write(temp_string+'\n')