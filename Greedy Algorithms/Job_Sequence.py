class Job:
    id_job = 1

    def __init__(self, deadline, profit):
        self.deadline = deadline
        self.profit = profit
        self.id_job = Job.id_job
        Job.id_job += 1

    def getID(self):
        return self.id_job

    def getProfit(self):
        return self.profit

    def getDeadline(self):
        return self.deadline


def JobSequence(jobs, t):
    n = len(jobs)
    arr_jobs = [0] * n
    for i in range(n):
        arr_jobs[i] = Job(jobs[i][0], jobs[i][1])

    arr_jobs.sort(key=lambda x: x.profit, reverse=True)

    schedule_jobs = [0] * t
    slots = [0] * t

    for i in range(n):
        for j in range(min(t-1, arr_jobs[i].getDeadline()-1), -1, -1):
            if slots[j] == 0:
                schedule_jobs[j] = arr_jobs[i].getID()
                slots[j] = 1
                break
            j -= 1

    for i in range(t):
        if slots[i] == 1:
            print(f'job: {schedule_jobs[i]}')


jobs = [[2, 40], [4, 15], [3, 60], [2, 20], [3, 10],
        [1, 45], [1, 55]]
JobSequence(jobs, 4)

