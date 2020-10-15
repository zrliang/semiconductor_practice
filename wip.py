import pandas as pd
import json
# from wip import WIP

class WIP():
    def __init__(self, configure):
        self.configure = configure  
        for i in self.configure.index:
            setattr(self, i, self.configure[i])
        
        self.processTime = []
        

df = pd.read_excel("./semiconductor_data.xlsx", sheet_name=2, dtype=str)
jobs = []

for i in range(len(df.values)):
    jobs.append(WIP(df.iloc[i]))