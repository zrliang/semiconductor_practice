import pandas as pd
import json
#from Machine import *
from Job import * 
from Chromosome import * 

# Read data
wip = pd.read_excel("./semiconductor_data.xlsx", sheet_name=2, dtype=str)
eqp = pd.read_excel("./semiconductor_data.xlsx", sheet_name=0, dtype=str)
tool = pd.read_excel("./semiconductor_data.xlsx", sheet_name=1, dtype=str)


jobs = []
# for i in range(len(wip.values)): #job len
#     jobs.append(Job(wip.iloc[i], eqp))
for i in range(len(wip.values)): #job len
    jobs.append(Job(wip.iloc[i], eqp))


chromosomes = []
for i in range(10):
    chromosomes.append(Chromosome(len(jobs)))

#for i in range(len(chromosomes)):
# for j in range(len(jobs)):
#     jobs[j].set_probability(chromosomes[0].get_probability(0))

print(jobs[1].canRunMachine)

#chromosomes[0].get_probability(0)



    