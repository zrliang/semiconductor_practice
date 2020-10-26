import pandas as pd
import json
#from Machine import *
from Job import * 
from Chromosome import * 

wip = pd.read_excel("./semiconductor_data.xlsx", sheet_name=2, dtype=str)
eqp = pd.read_excel("./semiconductor_data.xlsx", sheet_name=0, dtype=str)
tool = pd.read_excel("./semiconductor_data.xlsx", sheet_name=1, dtype=str)

J1=Job(wip.iloc[0], eqp) #instance
J1.processTime

chr1=Chromosome(len(wip.values))
#chr1.get_probability()
chr1.probability
print(len(wip.values))


jobs = []
for i in range(len(wip.values)): #100
    jobs.append(Job(wip.iloc[i], eqp))
# jobs[0].processTime

chromosomes = []
for i in range(100):
    chromosomes.append(Chromosome(len(jobs)))

for i in range(len(chromosomes)):
    for j in range(len(jobs)):
        jobs[j].set_probability( chromosomes[j].get_probability(i))


