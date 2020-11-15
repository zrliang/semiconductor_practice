import random
import numpy as np 

class Chromosome():
    def __init__(self,size=0):
        self.probability=[]
        self.size = size
        self.generate_probability()

        self.jobs=[] # X
        self.machines=[] # X
        self.makespan=0

    def __str__(self): #須為字串str
        return self.probability

    def get_probability(self, index): #return [選機,排序]
        
        if len(self.probability) > 0 and self.size + index < len(self.probability):
            return self.probability[index], self.probability[self.size + index]

    def generate_probability(self):
 
        for i in range(self.size * 2): #
            self.probability.append(random.random())  
        return self.probability
    
    def getMakespan(self):
        for i in range(len(self.machines)):
            print(self.machines[i].endTime)
            if self.machines[i].endTime > self.makespan:
                self.makespan= self.machines[i].endTime
        print(self.makespan)
        print("--------")

    #交配

    def Mating(self):
        pass

    #突變
    def mutation(self):
        pass