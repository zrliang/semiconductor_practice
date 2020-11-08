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
    machines[i].sort_job()


for j in range(len(machines[0].sorted_jobs)):
    print(machines[0].jobs[j].LOT_ID)
print("----------")
for j in range(len(machines[0].sorted_jobs)):   
    print(machines[0].sorted_jobs[j].LOT_ID)


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
df=[]
for i in range(len(machines)):
    for j in range(len(machines[i].jobs)):    
        df.append(dict(Task=str(machines[i].sorted_jobs[j].LOT_ID), Start='2020-11-07 %s'%datetime.timedelta(minutes=int(machines[i].sorted_jobs[j].startTime)),
        Finish='2020-11-07 %s'%datetime.timedelta(minutes=int(machines[i].sorted_jobs[j].endTime)),Resource=str(machines[i].EQP_ID)))


#呈現圖表
fig = px.timeline(df, x_start="Start", x_end="Finish", y="Resource", color="Task",text="Task")
fig.show()




    