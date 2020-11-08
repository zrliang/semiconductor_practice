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

for k in range(len(chromosomes)):

    # set_machine_id
    for j in range(len(jobs)):
        jobs[j].set_machine_id(chromosomes[k].get_probability(j)) 

    # add jobs to machine(object) 可改在裡面
    for i in range(len(machines)):
        for j in range(len(jobs)): 
            if machines[i].configure["EQP_ID"]==jobs[j].machineID:
                machines[i].jobs.append(jobs[j])
        machines[i].convert_to_dicts()
        machines[i].sort_job()

    # add machine to chromosome(object)
    for j in range(len(machines)):
        chromosomes[k].machines.append(machines[j])
    chromosomes[k].getMakespan()

    # clear job
    for i in range(len(machines)):
        machines[i].clear_job()





#print(machines[0].jobs2)

# for i in range(len(machines[0].jobs)):
#     print(machines[0].jobs[i].LOT_ID)
#     print(machines[0].jobs[i].startTime)
#     print(machines[0].jobs[i].endTime)
# print(machines[0].startTime)
# print(machines[0].endTime)
# print("------")

#get Makespan
# 寫在裡面
# for i in range(len(machines)):
#     print(machines[i].endTime)
#     if machines[i].endTime > chromosomes[0].makespan:
#         chromosomes[0].makespan= machines[i].endTime
# print(chromosomes[0].makespan)

#Mating

#Mutation

#Selection

# #甘特圖
# df=[]
# for i in range(len(machines)):
#     for j in range(len(machines[i].jobs)):    
#         df.append(dict(Task=str(machines[i].jobs[j].LOT_ID), Start='2020-11-07 %s'%datetime.timedelta(minutes=int(machines[i].jobs[j].startTime)),
#         Finish='2020-11-07 %s'%datetime.timedelta(minutes=int(machines[i].jobs[j].endTime)),Resource=str(machines[i].EQP_ID)))

# #呈現圖表
# fig = px.timeline(df, x_start="Start", x_end="Finish", y="Resource", color="Task",text="Task")
# fig.show()




    