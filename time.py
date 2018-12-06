import os
import time
import datetime
import pandas as pd 
from pandas import Series,DataFrame

fp = r'D:\Downloads\WeChat Files\hty821364719\Files\2018.11.28西核所脉冲中子实验\2018.11.29退火数据\三极管辐照板50芯1#退火数据\data\2009-03-20 03.31.57-三极管辐照板50芯1#退火数据\第1次'
os.chdir(fp)
filelist = os.listdir(fp)

times = []
for file in filelist:
    build_time = time.ctime(os.path.getmtime(file))
    times.append(build_time)
print(times)

lfp = r'C:\Users\Shiki\Desktop\2018.12.03所有数据\三极管50芯数据\前天退火测量2009-03-19 00.07.53\第1次'
os.chdir(lfp)
lfilelist = os.listdir(lfp)

after_times =[]
for file in lfilelist:
    after_time = time.ctime(os.path.getmtime(file))
    after_times.append(after_time)
print(after_times)

'''anneal_times = []
for i in range(44):
    time1 = (times[i]
    time2 = float(after_times[i])
    anneal = time.ctime((time2 - time1))
    anneal_times.append(anneal + '\t')
print(anneal_times)'''

Anneal_time = pd.DataFrame()
Anneal_time['ceishi'] = after_times
#Anneal_time['tuihuo'] = times
Anneal_time.to_csv('2.csv')