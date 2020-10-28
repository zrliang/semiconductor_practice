import random
import numpy as np 

class Chromosome():
    def __init__(self,size=0):
        self.probability=[]
        self.size = size
        self.generate_probability()

    def __str__(self): #須為字串str
        return self.probability
    # def get_random(self):
    #     self.gene=random.random()
    #     return self.gene

    def get_probability(self, index): #return [選機,排序]
        
        if len(self.probability) > 0 and self.size + index < len(self.probability):
            return self.probability[index], self.probability[self.size + index]

    def generate_probability(self):
        # randomlist=[]
        # for i in range(10000):
        #     randomlist.append(random.uniform(0, 1))
        # self.probability=random.sample(randomlist, self.size*2)

        # linspace = np.linspace(0, 1, 10000)
        # print(type(linspace))
        # self.probability = random.sample(list(linspace), self.size * 2)
        for i in range(self.size * 2):
            self.probability.append(random.random()) 
            
        return self.probability

        # # if self.size != 0:
        # #     for i in range(self.size * 2):
        # #         self.probability.append(random.random())
        #     return self.probability

