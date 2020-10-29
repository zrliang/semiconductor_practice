import pandas as pd
import json
from Job import * 
from Machine import * 
from Chromosome import * 
import matplotlib.pyplot as plt

# Read data
wip = pd.read_excel("./semiconductor_data.xlsx", sheet_name=2, dtype=str)
eqp = pd.read_excel("./semiconductor_data.xlsx", sheet_name=0, dtype=str)
tool = pd.read_excel("./semiconductor_data.xlsx", sheet_name=1, dtype=str)

jobs = []
for i in range(len(wip.values)): #job len
    jobs.append(Job(wip.iloc[i], eqp))

chromosomes = []
for i in range(10):
    chromosomes.append(Chromosome(len(jobs)))

machines=[]
for i in range(len(tool.values)):
    machines.append(Machine(tool.iloc[i]))

## one chromosome
for j in range(len(jobs)):
    jobs[j].set_machine_id(chromosomes[0].get_probability(j)) #one chromosome

for i in range(len(machines)): #10
    for j in range(len(jobs)): #100
        machines[i].add_job(jobs[j].LOT_ID,jobs[j].machineID)
    print(f"Machine{i+1}:" ,len(machines[i].jobs))
print("Machine 1 's jobs:",machines[0].jobs)


prob = chromosomes[0].probability
#plt.hist(prob, bins=50)
plt.scatter(range(0, len(prob)), prob)
plt.show()


# for i in range(len(jobs)):
#     print(jobs[i].machineID)

    