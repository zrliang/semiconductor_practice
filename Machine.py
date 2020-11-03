
class Machine(object):
    def __init__(self,configure):
        self.configure=configure #
        self.recoverTime = int(self.configure["RECOVER_TIME"])
        for i in self.configure.index:   #LOT_ID、OPE_NO... to object
            setattr(self, i, self.configure[i])
        self.jobs = [] #未排
        self.jobs2 = []
        self.job_sort_prob=[]
        self.sorted_jobs=[] 

    # def add_job(self,job_id,job_machine_id,job_sort_prob):
    #     if self.configure["EQP_ID"]==job_machine_id:
    #         self.jobs.append(job_id)
    #         self.job_sort_prob.append(job_sort_prob)

    def add_job(self,job):
        self.jobs.append(job)
        #self.job_sort_prob.append(job_sort_prob)

    # def sort_job(self):
    #     if len(self.jobs)>0:

    #         Job_conbine=zip(self.jobs,self.job_sort_prob)  #兩個一維轉成一個二維
    #         sort_job=sorted(Job_conbine,key=(lambda x:x[1]),reverse=True) #二維排序(x[1]針對欄位二) 由大到小
    #         for i in range(len(self.jobs)):
    #             self.sorted_jobs.append(sort_job[i][0])
    #     else:
    #         print("no add job first!")

    def convert_to_dicts(self):
        '''把物件列表轉換為字典列表'''
        obj_arr = []
        for o in self.jobs:
        #把Object物件轉換成Dict物件
            dict = {}
            dict.update(o.__dict__)
            obj_arr.append(dict)
        self.jobs2=obj_arr

        return obj_arr


    def sort_job(self):
        for i in range(len(self.jobs)):
            self.sorted_jobs = sorted(self.jobs2,key = lambda e:e['probability'][1],reverse = True) #二維排序(x[1]針對欄位二) 由大到小
            #self.sorted_jobs = sorted(self.jobs[i].probability[1], reverse = True)
    def clear_job(self):
        pass