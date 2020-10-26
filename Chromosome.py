import random
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

    def get_probability(self, index):
        
        # if len(self.probability) > 0 and self.size + index < len(self.probability):
        #     return self.probability[index], self.probability[self.size + index]

    def generate_probability(self):
        if self.size != 0:
            for i in range(self.size * 2):
                self.probability.append(random.random())
            return self.probability

        return