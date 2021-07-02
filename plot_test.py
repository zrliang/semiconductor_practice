import plotly.express as px
import pandas as pd
import datetime
import time # 引入time

df1 = pd.read_csv("result.csv",names=["wlot_lot_number","HB","Wire","Entity","Start_t","End_t"])
df2 = pd.read_csv('WipOutPlanTime_.csv')
result = pd.merge(df1, df2, on ='wlot_lot_number', how ='left')
entities= result.groupby("Entity") # group by entity
# entities.groups #show dict, value is row index
entity_key_list= list(entities.groups.keys()) # key list

# 2021/4/17 (改 變數)
ini_time_stamp = 1618615800 

df=[]
count=0
for i in range(10): 
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

        df.append(dict(Lot_ID= Lot_id, Start=start_ts,Finish=end_ts,Entity=Entity,Sets=Sets,Bd_id=Bd_id))
    if(count==20) or i==9: #變數
       #呈現圖表
        fig = px.timeline(df, x_start="Start", x_end="Finish", y="Entity", color="Bd_id",text="Lot_ID",hover_name="Sets")
        fig.update_yaxes(categoryorder="category descending") # 
        fig.write_html("C:/Users/LiangCJ/Desktop/plot_result/"+df[0]['Entity']+"_" +df[-1]['Entity']+".html")
        df=[]
        count=0

    


# #呈現圖表
# fig1 = px.timeline(df, x_start="Start", x_end="Finish", y="Entity", color="Lot_ID",text="Lot_ID")
# fig1.update_yaxes(categoryorder="category descending") # 
# fig1.show()
# fig1.show()
