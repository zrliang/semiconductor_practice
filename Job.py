class Job():
    def __init__(self, configure,processTime): #processTime=eqp
        self.configure = configure
        #print(configure)
        #self.processTime = processTime
        self.processTime = processTime[processTime["RECIPE"] == self.configure["RECIPE"]] #filter to recipe
        self.canRunMachine = {
            0.33333 : "machine1",
            0.66666 : "machine7",
            1 : "machine8"
        }
        self.machineID = ''  #var
        self.startTime = 0 #var
        self.endTime = 0 #var
        self.probability = 0

        for i in self.configure.index:   #LOT_ID、OPE_NO... to object
            setattr(self, i, self.configure[i])

    
    # def set_probability(self, probabilities):
    #     m_probability = probabilities[0]
    #     last  = 0
    #     for key in self.canRunMachine.keys():
    #         if m_probability > last and m_probability < key:
    #             self.machineID = self.canRunMachine[key]
    #         else:
    #             last = key   
    #     pass

    def set_machine_id(self, machineID):
        self.machineID = machineID

    def set_start_time(self, time):
        self.startTime = time
        processTime = int(self.processTime[ self.processTime["EQP_ID"] == self.machineID ]["PROCESS_TIME"]) #!
        self.endTime = self.startTime + processTime

    def get_end_time(self):
        return self.endTime
    
    
