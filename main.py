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

#
jobs = []
for i in range(len(wip.values)): #job len
    jobs.append(Job(wip.iloc[i], eqp))

#
chromosomes = []
for i in range(10):
    chromosomes.append(Chromosome(len(jobs)))

#
machines=[]
for i in range(len(tool.values)):
    machines.append(Machine(tool.iloc[i]))

## one chromosome
#for i in range(len(chromosomes)):

#
for j in range(len(jobs)):
    jobs[j].set_machine_id(chromosomes[0].get_probability(j)) #[0] first chromosome

# for i in range(len(machines)): #10
#     for j in range(len(jobs)): #100
#         machines[i].add_job(jobs[j].LOT_ID,jobs[j].machineID,jobs[j].probability[1])
#         pass
#     machines[i].sort_job()

#     print(f"Machine{i+1}:" ,len(machines[i].jobs))
# print("Machine 1 's jobs:",machines[0].jobs)
# print("Machine 1 's jobs:",machines[0].job_sort_prob)
# print("Machine 1 's jobs:",machines[0].sorted_jobs)

# add jobs to machine(object)
for i in range(len(machines)):
    for j in range(len(jobs)): 
        if machines[i].configure["EQP_ID"]==jobs[j].machineID:
            machines[i].jobs.append(jobs[j])
    machines[i].convert_to_dicts()
    machines[i].sort_job()

#print(machines[0].jobs2)

for i in range(len(machines[0].jobs)):
    print(machines[0].jobs[i].LOT_ID)
    print(machines[0].jobs[i].startTime)
    print(machines[0].jobs[i].endTime)
print("------")



#甘特圖
df=[]
for i in range(len(machines)):
    for j in range(len(machines[i].jobs)):    
        df.append(dict(Task=machines[i].jobs[j].LOT_ID, Start='2020-11-07 %s'%datetime.timedelta(minutes=machines[i].jobs[j].startTime),
        Finish='2020-11-07 %s'%datetime.timedelta(minutes=machines[i].jobs[j].endTime),Resource=machines[i].EQP_ID))

#呈現圖表
fig = px.timeline(df, x_start="Start", x_end="Finish", y="Resource", color="Task",text="Task")
fig.show()




    