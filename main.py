import pandas as pd
import json
from Job import * 
from Machine import * 
from Chromosome import * 
import matplotlib.pyplot as plt

import random
import plotly.express as px
import datetime
from copy import deepcopy

# Read data
wip = pd.read_excel("./semiconductor_data.xlsx", sheet_name=2, dtype=str)
eqp = pd.read_excel("./semiconductor_data.xlsx", sheet_name=0, dtype=str)
tool = pd.read_excel("./semiconductor_data.xlsx", sheet_name=1, dtype=str)
setup_time = pd.read_excel("./semiconductor_data.xlsx", sheet_name=3, index_col=0)

population_size= 4  #6666666666666666666666
crossover_rate=1    #6666666666666666666666
mutation_rate=1     #6666666666666666666666

# ---------------Frame----------------
# create jobs
jobs = []
for i in range(len(wip.values)): #job len (100)
    jobs.append(Job(wip.iloc[i], eqp))

# # create chromosomes
# chromosomes = []
# for i in range(population_size):
#     chromosomes.append(Chromosome(len(jobs))) #input ()

# test  #6666666666666666666666
chromosomes = []
for i in range(population_size):
    chromosomes.append(Chromosome(6)) #input ()

# create machine
machines=[]
for i in range(len(tool.values)):
    machines.append(Machine(tool.iloc[i]))

# ------------------------------------

# # Papulations

# for k in range(len(chromosomes)):

#     # job set_probability
#     for j in range(len(jobs)):
#         jobs[j].set_probability(chromosomes[k].get_probability(j)) 

#     # add jobs to machine(object) 可改在裡面
#     for i in range(len(machines)):
#         for j in range(len(jobs)): 
#             if machines[i].configure["EQP_ID"]==jobs[j].machineID:
#                 machines[i].jobs.append(jobs[j])
#         machines[i].sort_job(setup_time)

#     # record makespan & clear job
#     for i in range(len(machines)):
#         if machines[i].endTime > chromosomes[k].makespan :
#             chromosomes[k].makespan=machines[i].endTime

#         machines[i].clear_job()
    
#     #print(chromosomes[k].makespan)

#print("---------")

#Crossover
##
parent_list= deepcopy(chromosomes[:])
offspring_list= deepcopy(chromosomes[:])
s=list(np.random.permutation(population_size)) #[0,2,3,1]
s=[0,1,2,3]
print(s)
for m in range(int(population_size/2)): #2
    crossover_prob=np.random.rand()
    if crossover_rate>=crossover_prob: 

        parent1= deepcopy(parent_list[s[2*m]].probability)
        parent2= deepcopy(parent_list[s[2*m+1]].probability)

        #size=range(1,len(jobs)+1)  #染色體大小 #10+10(range(1,21))  #只有前半 #1~100 #666
        # test
        size=range(1,7)  #6666666666666666666666

        CutPoint=random.sample(size, 2) 
        CutPoint.sort()
        print(CutPoint)
        strpoint=CutPoint[0]
        endpoint=CutPoint[1]

        child1= deepcopy(parent1)
        child2= deepcopy(parent2)

        child1[strpoint-1:endpoint]=parent2[strpoint-1:endpoint]
        child2[strpoint-1:endpoint]=parent1[strpoint-1:endpoint]

        offspring_list[s[2*m]].probability = deepcopy(child1)
        offspring_list[s[2*m+1]].probability = deepcopy(child2)

       
for i in range(4):
    print(parent_list[i].probability)
print("----")
for i in range(4):  
    print(offspring_list[i].probability)

#print(len(chromosomes[0].probability))

# for i in range(population_size):
#     print(chromosomes[i].makespan)

# print("s",s)

#Mutation
s=list(np.random.permutation(population_size)) #[0,2,3,1]
for m in range(len(offspring_list)):
        mutation_prob=np.random.rand()
        if mutation_rate >= mutation_prob:

            #size=range(1,len(jobs)+1)  #染色體大小 #10+10(range(1,21))  #只有前半 #1~100 #666
            # test
            size=range(0,6)  #0-5  #6666666666666666666666
            one_gene=random.sample(size, 1) 
            print("第",m+1,"次",one_gene[0])
            offspring_list[s[m]].probability[one_gene[0]] = random.random()

            pass

for i in range(4):  
    print(offspring_list[i].probability)

#算makespan

#Selection


# for j in range(len(machines[0].sorted_jobs)):
#     print(machines[0].jobs[j].LOT_ID, machines[0].jobs[j].R_QT)

# print("----------")

# for i in range(len(machines[0].sorted_jobs)):
#     print(machines[0].sorted_jobs[i].LOT_ID,machines[0].sorted_jobs[i].R_QT)
 
    
# for i in range(len(jobs)):
#     print(jobs[i].endTime)

# add machine to chromosome(object)
# for j in range(len(machines)):
#     chromosomes[0].machines.append(machines[j])

# chromosomes[k].getMakespan()

    # # clear job
    # for i in range(len(machines)):
    #     machines[i].clear_job()



# #甘特圖
# #時間限制(超過24hr:1440 分)
# df=[]
# for i in range(len(machines)):
#     for j in range(len(machines[i].sorted_jobs)): 

#         if  machines[i].sorted_jobs[j].startTime > float(machines[i].sorted_jobs[j].R_QT)*60:
#             df.append(
#             dict(Task=str(machines[i].sorted_jobs[j].LOT_ID), 
#             Start='2020-11-07 %s'%datetime.timedelta(seconds=float(machines[i].sorted_jobs[j].startTime)),
#             Finish='2020-11-07 %s'%datetime.timedelta(seconds=float(machines[i].sorted_jobs[j].endTime)),
#             Recipe='broken',
#             Machine=machines[i].EQP_ID))
        
#         else:
#             df.append(
#             dict(Task=str(machines[i].sorted_jobs[j].LOT_ID), 
#             Start='2020-11-07 %s'%datetime.timedelta(seconds=float(machines[i].sorted_jobs[j].startTime)),
#             Finish='2020-11-07 %s'%datetime.timedelta(seconds=float(machines[i].sorted_jobs[j].endTime)),
#             Recipe=machines[i].sorted_jobs[j].RECIPE,
#             Machine=machines[i].EQP_ID))



# #呈現圖表
# fig1 = px.timeline(df, x_start="Start", x_end="Finish", y="Machine", color="Recipe",text="Task")
# #fig2 = px.timeline(df, x_start="Start", x_end="Finish", y="Machine", color="Task",text="Task")
# #sfig.update_yaxes(autorange="reversed")

# fig1.show()
# #fig2.show()


    