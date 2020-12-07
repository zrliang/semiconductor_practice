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
import time

start = time.process_time()

# import data
wip = pd.read_excel("./semiconductor_data(30lot).xlsx", sheet_name=2, dtype=str)
eqp = pd.read_excel("./semiconductor_data(30lot).xlsx", sheet_name=0, dtype=str)
tool = pd.read_excel("./semiconductor_data(30lot).xlsx", sheet_name=1, dtype=str)
setup_time = pd.read_excel("./semiconductor_data(30lot).xlsx", sheet_name=3, index_col=0)

population_size=10  #66666
num_iteration =1
crossover_rate=1    #66666
mutation_rate=1     #66666

# ---------------Frame----------------
# create jobs
jobs = []
for i in range(len(wip.values)): #job len (100)
    jobs.append(Job(wip.iloc[i], eqp))

# create chromosomes
chromosomes = []
for i in range(population_size):
    chromosomes.append(Chromosome(len(jobs))) #input ()

# create machines
machines=[]
for i in range(len(tool.values)):
    machines.append(Machine(tool.iloc[i]))

# ------------------------------------
MakespanRecord=[]

# 迭代
for x in range(num_iteration):
    #------------------------Crossover------------------------------------
    ##
    parent_list = deepcopy(chromosomes)
    offspring_list= deepcopy(chromosomes)

    Crossover(parent_list,offspring_list,population_size,len(jobs),crossover_rate)

    #------------------------Mutation------------------------------------
    mutation(population_size,offspring_list,mutation_rate,len(jobs))

    #-------------------- fitness value -------------------------------------
    total_chromosomes=deepcopy(parent_list)+deepcopy(offspring_list)
    # print("--total_chromosomes--")   
    # for i in range(8):
    #     print(total_chromosomes[i].probability)


    for k in range(len(total_chromosomes)):
        total_chromosomes[k].clear_values()
        # job set_probability
        for j in range(len(jobs)):
            jobs[j].set_probability(total_chromosomes[k].get_probability(j)) 

        # add jobs to machine(object) 可改在裡面
        for i in range(len(machines)):
            for j in range(len(jobs)): 
                if machines[i].configure["EQP_ID"]==jobs[j].machineID:
                    machines[i].jobs.append(jobs[j])
            machines[i].sort_job(setup_time)

        # record makespan & tardiness_num
        for i in range(len(machines)):
            # record makespan
            if machines[i].endTime > total_chromosomes[k].makespan :
                total_chromosomes[k].makespan=machines[i].endTime
            # record tardiness_num
            for j in range(len(machines[i].sorted_jobs)): 
                if  machines[i].sorted_jobs[j].startTime > float(machines[i].sorted_jobs[j].R_QT)*60:
                    total_chromosomes[k].tardiness_num+=1

            machines[i].clear_job()            

        #print(total_chromosomes[k].tardiness_num)
        # record tardiness

        # for i in range(len(machines)):
        #     for j in range(len(machines[i].sorted_jobs)): 
        #         if  machines[i].sorted_jobs[j].startTime > float(machines[i].sorted_jobs[j].R_QT)*60:
        #             total_chromosomes[k].tardiness_num+=1

        #     machines[i].clear_job()
        
        # print(total_chromosomes[k].makespan)

    #print("-------")
    #-----------------Selection----------------------

    for t in range(len(total_chromosomes)):
        print(total_chromosomes[t].makespan,total_chromosomes[t].tardiness_num)
        total_chromosomes[t].target_value= 0.0001* total_chromosomes[t].makespan + 0.9999*total_chromosomes[t].tardiness_num
        print(total_chromosomes[t].target_value)
    print("-----")
    sorted_total_chromosomes = sorted(total_chromosomes, key=lambda e:e.target_value, reverse = False) #小到大


    chromosomes= deepcopy(sorted_total_chromosomes[:population_size]) #elite #下一代 #list
    MakespanRecord.append(chromosomes[0].makespan)
     
    # #輪盤法
    # def sum(num): #分母
    #     sum = 0
    #     x=1
    #     while x < num+1:
    #         sum = sum + x
    #         x+=1
    #     return sum
    # Sum=sum(population_size*2) #1+2+..+90

    # t=0
    # proba_list=[0]
    # for i in range(population_size*2-1):
    #     proba=(population_size*2-i)/Sum #90/1+...
    #     t+=proba
    #     proba_list.append(t)
    # #print(proba_list)

    # def getk2(): #得index
    #     selectone=random.random()
    #     k2=-1
    #     for i in range(len(proba_list)):
    #         if(selectone>proba_list[i]):
    #             k2+=1
    #     return k2

    # select_index=[]
    # count=0
    # while(len(select_index)<population_size): #不重複 #40個
    #     count+=1
    #     temp=getk2()
    #     if(temp not in select_index):
    #         select_index.append(temp)

    # chromosomes=[]
    # for i in select_index:
    #     chromosomes.append(sorted_total_chromosomes[i])


# -----------------Result----------------------

## final job & machine condition
# job set_probability
print("tardiness=",chromosomes[0].tardiness_num)

for j in range(len(jobs)):
    jobs[j].set_probability(chromosomes[0].get_probability(j)) 

# add jobs to machine(object) 可改在裡面
for i in range(len(machines)):
    for j in range(len(jobs)): 
        if machines[i].configure["EQP_ID"]==jobs[j].machineID:
            machines[i].jobs.append(jobs[j])
    machines[i].sort_job(setup_time)

# record makespan & clear job
for i in range(len(machines)):
    if machines[i].endTime > chromosomes[0].makespan :
        chromosomes[0].makespan=machines[i].endTime

end = time.process_time()
processT=end-start
print("執行時間:",processT)

#收斂圖
plt.plot([i for i in range(len(MakespanRecord))],MakespanRecord,'b') #x,y為list資料
plt.ylabel('makespan',fontsize=15)
plt.xlabel('generation',fontsize=15)
plt.show()

#甘特圖
#時間限制(超過24hr:1440 分)
df=[]
for i in range(len(machines)):
    for j in range(len(machines[i].sorted_jobs)): 

        if  machines[i].sorted_jobs[j].startTime > float(machines[i].sorted_jobs[j].R_QT)*60:
            df.append(
            dict(Task=str(machines[i].sorted_jobs[j].LOT_ID), 
            Start='2020-11-07 %s'%datetime.timedelta(seconds=float(machines[i].sorted_jobs[j].startTime)),
            Finish='2020-11-07 %s'%datetime.timedelta(seconds=float(machines[i].sorted_jobs[j].endTime)),
            Recipe='broken',
            Machine=machines[i].EQP_ID))
    
        else:
            df.append(
            dict(Task=str(machines[i].sorted_jobs[j].LOT_ID), 
            Start='2020-11-07 %s'%datetime.timedelta(seconds=float(machines[i].sorted_jobs[j].startTime)),
            Finish='2020-11-07 %s'%datetime.timedelta(seconds=float(machines[i].sorted_jobs[j].endTime)),
            Recipe=machines[i].sorted_jobs[j].RECIPE,
            Machine=machines[i].EQP_ID))

#呈現圖表
fig1 = px.timeline(df, x_start="Start", x_end="Finish", y="Machine", color="Recipe",text="Task")

fig1.show()


    