class Machine(object):
    def __init__(self,configure):
        self.configure=configure #?
        self.jobs = []

    def add_job(self,job):
        self.jobs.append(job)