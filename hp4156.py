import numpy as np
import pandas as pd
from pandas import DataFrame,Series
import os

filepath = r'E:\黄泰燚\2018.12.03所有数据\三极管50芯数据\7Pulse-2009-03-19 13.45.12\第1次'
os.chdir(filepath)#设置工作路径
filelist = os.listdir(filepath)

'''删除Index'''
for i in range(len(filelist)):
    oldfile = pd.read_table(filelist[i])
    del oldfile['Index']
    oldfile.to_csv(filelist[i],index = False)

all_status = []
for k in range(15):
    if k%3  == 0 :
        status = '饱和'
    elif k%3 == 1:
        status = '截止'
    elif k%3 == 2:
        status = '放大'
    else:
        break
    all_status.append(status)


for j in range(15):
    if j < 3:
        transistor = '2N41124'
    elif j >= 3 and j < 6:
        transistor = 'BCW72'
    elif j >= 6 and j < 9:
        transistor = 'SGA8343Z'
    elif j >= 9 and j < 12:
        transistor = 'BFU730F'
    elif j >= 12 and j < 15:
        transistor = 'NE85633'
    else:
        break

    os.rename(filelist[j],'Q' + str(j//3 + 1) + str(j%3 + 1) + ' - Gummel曲线 - ' + transistor + ' - ' + all_status[j] + '.CSV')
    os.rename(filelist[j + 15], 'Q' + str(j//3 + 1) + str(j%3 + 1) + ' - 输出特性曲线 - ' + transistor + ' - ' + all_status[j] + '.CSV')
    #os.rename(filelist[j + 30], 'Q' + str(j//3 + 1) + str(j%3 + 1) + ' - 反向Gummel曲线 - ' + transistor + ' - ' + all_status[j] + '.CSV')


#filelist = os.listdir(filepath)
#print(filelist)

