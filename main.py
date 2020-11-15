import pandas as pd
import json
from Job import * 
from Machine import * 
from Chromosome import * 
import matplotlib.pyplot as plt

import plotly.express as px
import datetime

# Read data
wip = pd.read_excel("./semiconductor_data.xlsx", sheet_name=2, dtype=str)
eqp = pd.read_excel("./semiconductor_data.xlsx", sheet_name=0, dtype=str)
tool = pd.read_excel("./semiconductor_data.xlsx", sheet_name=1, dtype=str)
setup_time = pd.read_excel("./semiconductor_data.xlsx", sheet_name=3, index_col=0)

# ---------------Frame----------------
# create jobs
jobs = []
for i in range(len(wip.values)): #job len (100)
    jobs.append(Job(wip.iloc[i], eqp))

# create chromosomes
chromosomes = []
for i in range(10):
    chromosomes.append(Chromosome(len(jobs))) #input ()

# create machine
machines=[]
for i in range(len(tool.values)):
    machines.append(Machine(tool.iloc[i]))

# ------------------------------------

# 一條

#for k in range(len(chromosomes)):

# set_machine_id
for j in range(len(jobs)):
    jobs[j].set_machine_id(chromosomes[0].get_probability(j)) 

# add jobs to machine(object) 可改在裡面
for i in range(len(machines)):
    for j in range(len(jobs)): 
        if machines[i].configure["EQP_ID"]==jobs[j].machineID:
            machines[i].jobs.append(jobs[j])
    machines[i].sort_job(setup_time)


# for j in range(len(machines[0].sorted_jobs)):
#     print(machines[0].jobs[j].LOT_ID)
# print("----------")
# for j in range(len(machines[0].sorted_jobs)):   
#     print(machines[0].sorted_jobs[j].LOT_ID)
for i in range(len(machines[0].sorted_jobs)):
    print(machines[0].sorted_jobs[i].LOT_ID)
    print(machines[0].sorted_jobs[i].startTime)
    print(machines[0].sorted_jobs[i].endTime)
    
# for i in range(len(jobs)):
#     print(jobs[i].endTime)

# add machine to chromosome(object)
# for j in range(len(machines)):
#     chromosomes[0].machines.append(machines[j])

# chromosomes[k].getMakespan()

    # # clear job
    # for i in range(len(machines)):
    #     machines[i].clear_job()


#Mating

#Mutation

#Selection

#甘特圖
#時間限制(超過24hr:1440 分)
df=[]
for i in range(len(machines)):
    for j in range(len(machines[i].sorted_jobs)):    
        df.append(dict(Task=str(machines[i].sorted_jobs[j].LOT_ID), 
        Start='2020-11-07 %s'%datetime.timedelta(seconds=float(machines[i].sorted_jobs[j].startTime)),
        Finish='2020-11-07 %s'%datetime.timedelta(seconds=float(machines[i].sorted_jobs[j].endTime)),
        Machine=str(machines[i].EQP_ID),
        Recipe=machines[i].sorted_jobs[j].RECIPE))


#呈現圖表
fig = px.timeline(df, x_start="Start", x_end="Finish", y="Machine", color="Recipe",text="Task")
fig.show()



    