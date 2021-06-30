
import plotly.express as px
import pandas as pd
import datetime
import time # 引入time

import csv

file = 'result.csv'
with open(file) as csvFile:
    csvReader = csv.reader(csvFile)
    datas = list(csvReader)
#print(datas)

for data in datas[:1]:
    print(float(data[4])*60)   
# time_stamp = 1624923000 # 設定timeStamp
# struct_time = time.localtime(time_stamp) # 轉成時間元組
# print(struct_time)
# timeString = time.strftime("%Y-%m-%d %H:%M:%S", struct_time) # 轉成字串
# print(timeString)

# #時間限制(超過24hr:1440 分)
# # df=[]
# # for i in range(len(machines)):
# #     for j in range(len(machines[i].sorted_jobs)): 

#         df.append(
#         dict(Task=str(machines[i].sorted_jobs[j].LOT_ID), 
#         Start='2020-11-07 %s'%datetime.timedelta(seconds=float(machines[i].sorted_jobs[j].startTime)),
#         Finish='2020-11-07 %s'%datetime.timedelta(seconds=float(machines[i].sorted_jobs[j].endTime)),
#         Recipe=machines[i].sorted_jobs[j].RECIPE,
#         Machine=machines[i].EQP_ID))

# df = pd.DataFrame([
#     dict(Task="Job A", Start='2009-01-01', Finish='2009-02-28', Resource="Alex"),
#     dict(Task="Job B", Start='2009-03-05', Finish='2009-04-15', Resource="Alex"),
#     dict(Task="Job C", Start='2009-02-20', Finish='2009-05-30', Resource="Max")
# ])

# df = pd.DataFrame([
#     dict(Task="Job A", Start=timeString, Finish=timeString, Resource="Alex")])


# #呈現圖表
# fig1 = px.timeline(df, x_start="Start", x_end="Finish", y="Resource", color="Task",text="Task")
# fig1.show()
