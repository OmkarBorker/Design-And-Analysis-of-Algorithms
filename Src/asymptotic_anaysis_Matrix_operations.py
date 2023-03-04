import time
from numpy.random import seed
from numpy.random import randint
import matplotlib.pyplot as plt

def MatMul(A,B,C):
    result = C
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
                
def MatAdd(A,B,C):
    result = C
    for i in range(len(A)):  

        for j in range(len(A[0])):
            result[i][j] = A[i][j] + B[i][j]

def timefunction(elements, times, fun):
    for i in range(1, 8):

        a = randint(0, 10, (100 * i,100 * i))
        b = randint(0, 10, (100 * i,100 * i))
        c = randint(0, 1, (100 * i,100 * i))
        start = time.time()
        fun(a,b,c)
        end = time.time()
        print(len(a), end-start)
        elements.append(len(a))
        times.append(end-start)
        
name = "Matrix Addition"
name1 = "Matrix Multiplication"  
        
elements = list()
elements1 = list()

times = list()
times1 = list()


timefunction(elements, times,MatAdd)
timefunction(elements1, times1,MatMul)

plt.plot(elements, times, label=name)
plt.plot(elements1, times1, label=name1)

plt.xlabel('Size of The Matrix')
plt.ylabel('Time Complexity in (seconds)')
plt.grid()
plt.legend()

plt.show()