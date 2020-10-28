class Machine(object):
    def __init__(self,configure):
        self.configure=configure #?
        for i in self.configure.index:   #LOT_ID、OPE_NO... to object
            setattr(self, i, self.configure[i])
        self.jobs = []

    def add_job(self,job_id,job_machine_id):
        if self.configure["EQP_ID"]==job_machine_id:
            self.jobs.append(job_id)
        

    def sort_job(self):
        pass

    def clear_job(self):
        pass