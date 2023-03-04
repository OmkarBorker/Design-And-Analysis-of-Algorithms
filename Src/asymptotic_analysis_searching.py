import time
from numpy.random import seed
from numpy.random import randint
import matplotlib.pyplot as plt
import random

def linearSearch(arr, x):
 
    for i in range(len(arr)):
 
        if arr[i] == x:
            return i
 
    return -1

def binarySearch(arr, l, r, x):
 
    if r >= l:
        mid = l + (r - l) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binarySearch(arr, l, mid-1, x)
        else:
            return binarySearch(arr, mid + 1, r, x)
    else:
        return -1

name = "linear search"
name1 = "binary search"

elements = list()
elements1 = list()

times = list()
times1 = list()

def timefunction(elements, times, fun):
    for i in range(1, 10000):

        a = randint(1, 10 , 1000 * i)
        b = random.randrange(10)
        a.sort()
        start = time.time()
        fun(a,b)
        end = time.time()
        print(len(a), end-start)
        elements.append(len(a))
        times.append(end-start)
        
def timefunction2(elements, times, fun):
    for i in range(1, 1000):

        a = randint(1, 10 , 1000 * i)
        b = random.randrange(10)
        c = 0
        d = len(a)-1
        a.sort()
        start = time.time()
        fun(a,b,c,d)
        end = time.time()
        print(len(a), end-start)
        elements.append(len(a))
        times.append(end-start)
        

timefunction(elements, times,linearSearch)
timefunction2(elements1, times1,binarySearch)

plt.plot(elements, times, label=name)
plt.plot(elements1, times1, label=name1)
plt.xlabel('Size of Array')
plt.ylabel('Time Complexity in seconds')
plt.grid()
plt.legend()

plt.show()