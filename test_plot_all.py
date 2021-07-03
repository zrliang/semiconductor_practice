import plotly.express as px
import pandas as pd
import datetime
import time # 引入time


result = pd.read_csv("result.csv",names=["Lot_id","HB","Wire","Entity","Start_t","End_t"])
entities= result.groupby("Entity") # group by entity
# entities.groups #show dict, value is row index
entity_key_list= list(entities.groups.keys()) # key list

# 2021/4/17 (改 變數)
ini_time_stamp = 1618615800 

df=[]
count=0
for i in range(len(entity_key_list)): 
    key= entity_key_list[i]
    count+=1
    for j in range(len(entities.groups[key])):
        row_index=entities.groups[key][j]
        Lot_id =result.iloc[row_index].at['Lot_id'].strip()
        Entity =result.iloc[row_index].at['Entity'].strip()
        start_ts =  time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(ini_time_stamp+result.iloc[row_index].at['Start_t']*60)) 
        end_ts =  time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(ini_time_stamp+result.iloc[row_index].at['End_t']*60)) 

        df.append(dict(Lot_ID= Lot_id, Start=start_ts,Finish=end_ts,Entity=Entity))
    if(count==20) or i==len(entity_key_list)-1: #變數
       #呈現圖表
        fig = px.timeline(df, x_start="Start", x_end="Finish", y="Entity", color="Lot_ID",text="Lot_ID")
        fig.update_yaxes(categoryorder="category descending") # 
        fig.write_html("C:/Users/LiangCJ/Desktop/plot_result/"+df[0]['Entity']+"_" +df[-1]['Entity']+".html")
        df=[]
        count=0

    


# #呈現圖表
# fig1 = px.timeline(df, x_start="Start", x_end="Finish", y="Entity", color="Lot_ID",text="Lot_ID")
# fig1.update_yaxes(categoryorder="category descending") # 
# fig1.show()
# fig1.show()
