import time
from numpy.random import seed
from numpy.random import randint
import matplotlib.pyplot as plt
import random

#Helper function

#test case generation

def generate_test_case(num_jobs):
    priorities = [random.randint(1, 2**num_jobs) for _ in range(num_jobs)]
    lengths = [random.randint(1, 2**num_jobs) for _ in range(num_jobs)]
    jobs = list(zip(range(1, num_jobs+1), priorities, lengths))
    random.shuffle(jobs)

    return jobs

# Example usage:
# num_jobs = 5
# test_case = generate_test_case(num_jobs)


def JobScheduling(jobs):
    jobs = sorted(jobs, key=lambda x: x[1], reverse=True)
    schedule = []
    completion_time = [0] * len(jobs)

    for job in jobs:
        available_time = max(completion_time[:job[0]-1], default=0)
        schedule.append((job[0], available_time+job[2]))
        completion_time[job[0]-1] = available_time+job[2]

    return schedule

name = "job scheduling"


elements = list()

times = list()

def timefunction(elements, times, fun):
    for i in range(1, 1500):
        b = generate_test_case(2*i)
        start = time.time()
        fun(b)
        end = time.time()
        times.append(end-start)
        elements.append(2*i)
        
timefunction(elements, times,JobScheduling)

plt.plot(elements, times, label=name)
plt.xlabel('number of jobs')
plt.ylabel('Time Complexity in seconds')
plt.grid()
plt.legend()

plt.show()