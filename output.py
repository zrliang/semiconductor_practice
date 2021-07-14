## 7/9
import csv
import pandas as pd
import numpy as np  

## ini time
relative_time_1 = 120      # >10:30 改
relative_time_2 = 150      # >11:00

# read csv data
df1 = pd.read_csv("result(0707_2).csv")
df2 = pd.read_excel('機台區域作業產品.xls')[['Entity','Location']]  
result = pd.merge(df1, df2, left_on ='entity', right_on ='Entity', how='left')
original_group=result.groupby(['cust','pin_pkg','prod_id','bd_id','Location']) # Not use

# # 11. 7:30
def get_result_byFilter(result,relative_time):
    filter_strt = result["start_time"] <= relative_time #0, 150
    filter_end = result["end_time"] >= relative_time
    filter_result = result[filter_strt & filter_end]

    ## add 如果對照不到就回傳-1 , get ENT產生空白列 (改)
    return filter_result

# 
def getENTdf(temp_result,ent_colname):

    temp_group= temp_result.groupby(['cust','pin_pkg','prod_id','bd_id','Location','entity']) 
    df_grp_entity = pd.DataFrame(temp_group.groups.keys())
    grp_basis = df_grp_entity.groupby([0,1,2,3,4])  # cust > Location
    df_keys= pd.DataFrame(grp_basis.groups.keys())
    df_Ent_amount= pd.DataFrame(list(grp_basis.size()))
    ENTdf= pd.concat([df_keys, df_Ent_amount], axis=1)
    ENTdf.columns=['cust','pin_pkg','prod_id','bd_id','Location',ent_colname]

    return ENTdf

ENT_all = getENTdf(result,'Allocate ENT')
ENT_08 = getENTdf(get_result_byFilter(result,relative_time_1),'Original ENT(10:30)') # 改
ENT_11 = getENTdf(get_result_byFilter(result,relative_time_2),'Original ENT(11:00)')

# # ---caculate total qty -------
qty_list=[]
group_key_list= list(original_group.groups.keys())

# accumulation
for i in range(len(group_key_list)): 
    key= group_key_list[i]
    qty_sum=0
    for j in range(len(original_group.groups[key])):
        row_index=original_group.groups[key][j]
        qty_sum+=result.iloc[row_index].at['qty']

    qty_list.append(qty_sum)
df_qty = pd.DataFrame(qty_list,columns=['Output plan'])
# -------
# merge three df
result_all_8 = pd.merge(ENT_all, ENT_08, on =(['cust','pin_pkg','prod_id','bd_id','Location']), how ='left')
ENT_result = pd.merge(result_all_8, ENT_11, on =(['cust','pin_pkg','prod_id','bd_id','Location']), how ='left')
# concat all
temp_df= pd.concat([ENT_result, df_qty], axis=1)

## change column sequence
final_df = temp_df[['cust','pin_pkg','prod_id','bd_id','Location','Original ENT(10:30)','Original ENT(11:00)','Allocate ENT','Output plan']]

# # write to csv
final_df.to_csv("midterm.csv", index=False ,na_rep=0) #ignore index & replace NA to 0