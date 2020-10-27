import re
class Job():
    def __init__(self, configure,eqp_recipe): #processTime=eqp
        self.configure = configure

        for i in self.configure.index:   #LOT_ID、OPE_NO... to object
            setattr(self, i, self.configure[i])
        self.processTime = eqp_recipe[eqp_recipe["RECIPE"] == self.configure["RECIPE"]] #filter to recipe
        self.canRunMachine={}
        self.generate_canrunM()

        # self.canRunMachine = self.configure["CANRUN_TOOL"]
        #     0.33333 : "machine1",
        #     0.66666 : "machine7",
        #     1 : "machine8"
        # }
        
        self.machineID = ''  #var
        self.startTime = 0 #var
        self.endTime = 0 #var
        self.probability = 0


    # def set_probability(self, probabilities):
    #     m_probability = probabilities[0]
    #     last  = 0
    #     for key in self.canRunMachine.keys():
    #         if m_probability > last and m_probability < key:
    #             self.machineID = self.canRunMachine[key]
    #         else:
    #             last = key   
    #     pass

    def generate_canrunM(self):
        allM=self.configure["CANRUN_TOOL"]

        def cut_text(text,lenth):
            textArr = re.findall('.{'+str(lenth)+'}', text)
            textArr.append(text[(len(textArr)*lenth):])
            return textArr

        cut_canrunmachine=cut_text(allM,6)[:-1] #長度6 多餘-1
        one_prob=1/len(cut_canrunmachine)
        keys=[]
        for i in range(1,len(cut_canrunmachine)+1):
            keys.append(one_prob*i)
        self.canRunMachine = dict(zip(keys, cut_canrunmachine))

        return self.canRunMachine
    

    def set_machine_id(self, machineID):
        self.machineID = machineID

    def set_start_time(self, time):
        self.startTime = time
        processTime = int(self.processTime[ self.processTime["EQP_ID"] == self.machineID ]["PROCESS_TIME"]) #!
        self.endTime = self.startTime + processTime

    def get_end_time(self):
        return self.endTime
    
    
