import plotly.express as px
import pandas as pd
import datetime
import time # 引入time

# fixme
result = pd.read_csv("result(0707).csv",names=["wlot_lot_number","bd_id","HB","Wire","Entity","Start_t","End_t"])
#df2 = pd.read_csv('WipOutPlanTime_.csv')
#result = pd.merge(df1, df2, on ='wlot_lot_number', how ='left')
entities= result.groupby("Entity") # group by entity
# entities.groups #show dict, value is row index
entity_key_list= list(entities.groups.keys()) # key list

# 2021/4/17 08:30 (改 變數)
ini_time_stamp = 1618619400 

df=[]
count=0
for i in range(len(entity_key_list)): 
    key= entity_key_list[i]
    count+=1
    for j in range(len(entities.groups[key])):
        row_index=entities.groups[key][j]

        Lot_id =result.iloc[row_index].at['wlot_lot_number'].strip()
        Entity =result.iloc[row_index].at['Entity'].strip()
        start_ts =  time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(ini_time_stamp+result.iloc[row_index].at['Start_t']*60)) 
        end_ts =  time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(ini_time_stamp+result.iloc[row_index].at['End_t']*60)) 
        Sets = result.iloc[row_index].at['HB'].strip()+ "/"+ result.iloc[row_index].at['Wire'].strip()
        Bd_id= result.iloc[row_index].at['bd_id'].strip()
    

        df.append(dict(Lot_ID= Lot_id, Start=start_ts,Finish=end_ts,Entity=Entity,Sets=Sets,Bd_Id=Bd_id))
    if(count==25) or i==len(entity_key_list)-1: #變數
       #呈現圖表
        fig = px.timeline(df, x_start="Start", x_end="Finish", y="Entity", color="Bd_Id",text="Lot_ID",hover_name="Sets")   # hover_name
        fig.update_yaxes(categoryorder="category descending") # 
        fig.update_traces(textposition='inside',marker_line_color='rgb(8,48,107)')
        fig.write_html("C:/Users/LiangCJ/Desktop/plot_result/"+df[0]['Entity']+"_" +df[-1]['Entity']+".html")
        df=[]
        count=0
 




# #呈現圖表
# fig1 = px.timeline(df, x_start="Start", x_end="Finish", y="Entity", color="Lot_ID",text="Lot_ID")
# fig1.update_yaxes(categoryorder="category descending") # 
# fig1.show()
# fig1.show()
