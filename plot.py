
import plotly.express as px
import pandas as pd
import datetime
import time # 引入time
import csv

# read csv
file = 'result.csv'
with open(file) as csvFile:
    csvReader = csv.reader(csvFile)
    datas = list(csvReader)
#print(datas)

# 2021/4/17 (改變數)
ini_time_stamp = 1618615800 

# for data in datas[:1]:
#     print(float(data[4])*60)   
# time_stamp = 1624923000 # 設定timeStamp


# struct_time = time.localtime(time_stamp) # 轉成時間元組
# print(struct_time)
# timeString = time.strftime("%Y-%m-%d %H:%M:%S", struct_time) # 轉成字串
# print(timeString)

# #convert stamp to date
# start_ts =  time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(ini_time_stamp)) 
# end_ts =  time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(ini_time_stamp)) 
# print(start_ts)
count= 0
for i in range(len(datas[:3])):

    if(datas[i][3]!=datas[i+1][3]):
        count+=1
        list1=[]
        list1.append(i)

        if count ==3:
            print("畫")
            print(list1)
            count=0
            list1=[]




    print(datas[i][0])

# #時間限制(超過24hr:1440 分)
# df=[]
# for data in datas[:50]:
    
#     #convert stamp to date
#     start_ts =  time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(ini_time_stamp+float(data[4])*60)) 
#     end_ts =  time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(ini_time_stamp+float(data[5])*60)) 
#     # print(start_ts)
#     # print(end_ts)
#     df.append(dict(Lot_ID= data[0], Start=start_ts,Finish=end_ts,Entity=data[3], Wire=data[2],Heatblock=data[1]))


# #呈現圖表
# fig1 = px.timeline(df, x_start="Start", x_end="Finish", y="Entity", color="Wire",text="Lot_ID")
# fig1.update_yaxes(categoryorder="category descending") # 
# fig1.show()
