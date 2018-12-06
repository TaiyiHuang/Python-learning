import os
import pandas as pd
from pandas import DataFrame,Series

fp = r'E:\黄泰燚\2018.12.03所有数据\三极管采集卡数据\4\before'
os.chdir(fp)#设置工作路径
filelist = os.listdir(fp)
print(filelist)

def current(x):
    return (abs(x/200))

#修改文件行索引
for i in range(len(filelist)):
    oldfile = pd.read_table(filelist[i])
    newfile = oldfile.rename(columns = {'Voltage - Dev1_ai0':'VB-#1-BCW72','Voltage - Dev1_ai1':'VC-#1-BCW72',\
                                        'Voltage - Dev1_ai2':'VB-#2-BFU730F','Voltage - Dev1_ai3':'VC-#2-BFU730F', \
                                        'Voltage - Dev1_ai4': 'VB-#3-BFU730F', 'Voltage - Dev1_ai5': 'VC-#3-BFU730F', \
                                        'Voltage - Dev1_ai6': 'VB-#4-NE85633', 'Voltage - Dev1_ai7': 'VC-#4-NE85633'})
    
    #newfile.reindex(columns = ['Time','VB-#1-BCW72','VC-#1-BCW72','VB-#2-BFU730F','VC-#2-BFU730F','VB-#3-BFU730F','VC-#3-BFU730F','VB-#4-NE85633','VC-#4-NE85633'])
    col_name = newfile.columns.tolist()
    current_name = ['IB-#1-BCW72','IC-#1-BCW72','IB-#2-BFU730F','IC-#2-BFU730F','IB-#3-BFU730F','IC-#3-BFU730F','IB-#4-NE85633','IC-#4-NE85633']
    newfile['Time'] = newfile['Time'].map(lambda x:x*1000000)
    #添加电流列
    for j in range(1,9):
        newfile[current_name[j-1]] = newfile[col_name[j]].map(current)
    
    newfile.to_csv(filelist[i],index = False)

#修改文件后缀
for filename in filelist:
    portion = os.path.splitext(filename)
    # 如果后缀是.dat
    if portion[1] == ".txt":
        # 重新组合文件名和后缀名
        newname = portion[0] + ".csv"
        os.rename(filename,newname)
