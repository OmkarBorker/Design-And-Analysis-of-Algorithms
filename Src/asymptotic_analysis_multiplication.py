import time
from numpy.random import seed
from numpy.random import randint
import matplotlib.pyplot as plt
import string
import random

# Brute Force

def IntMul(x, y,):
    n = len(x)
    m = len(y)
    result = [0]*(n + m) 
  
    for i in range(n-1, -1, -1):
        dig1 = int(x[i])
        
        for j in range(m-1, -1, -1):
            carry = int(result[i+j+1])
            dig2 = int(y[j])
            dig12 = (dig1*dig2) + carry
            carry_l = dig12//10
            carry_r = dig12%10
            result[i+j+1] = carry_r
            result[i+j] = result[i+j] + carry_l
            
    while(result[0] == 0):
        result.pop(0)

    return_this = "".join([str(dig) for dig in result])
    
    return return_this

#Naive Divide And Conquer

def DivideAndConquer(X, Y):
    
    n = max(len(X), len(Y))
    X = X.zfill(n)
    Y = Y.zfill(n)
 
    # Base case
    if n == 1: return int(X[0])*int(Y[0])
 
    fh = n//2  
    sh = n - fh  
 
    Xl = X[:fh]
    Xr = X[fh:]
 
    Yl = Y[:fh]
    Yr = Y[fh:]
 
    P1 = DivideAndConquer(Xl, Yl)
    P2 = DivideAndConquer(Xr, Yr)
    P3 = DivideAndConquer(Xl, Yr)
    P4 = DivideAndConquer(Xr, Yl)

    return P1*(1<<(2*sh)) + (P3 + P4)*(1<<sh) + P2


#Karatsuba Algorithm

def Karatsuba(X, Y):
    n = max(len(X), len(Y))
    X = X.zfill(n)
    Y = Y.zfill(n)
 
    # Base case
    if n == 1: return int(X[0])*int(Y[0])
    fh = n//2  
    sh = n - fh  
    Xl = X[:fh]
    Xr = X[fh:]
    Yl = Y[:fh]
    Yr = Y[fh:]
 
    P1 = Karatsuba(Xl, Yl)
    P2 = Karatsuba(Xr, Yr)
    P3 = Karatsuba(str(int(Xl) + int(Xr)), str(int(Yl) + int(Yr)))
 
    return P1*(1<<(2*sh)) + (P3 - P1 - P2)*(1<<sh) + P2


name = "Brute Force Integer"
name1 = "Naive Divide And Conquer"
name2 = "Karatsuba Algorithm"


def randomword(length):
   numbers = "123456789"
   return ''.join(random.choice(numbers) for i in range(length))


elements = list()
elements1 = list()
elements2 = list()

times = list()
times1 = list()
times2 = list()

def timefunction(elements, times, fun):
    for i in range(1,12):

        a = randomword(2**i)
        b = randomword(2**i)
        start = time.time()
        fun(a,b)
        end = time.time()
        print(len(a), end-start)
        elements.append(len(a))
        times.append(end-start)
        
        
timefunction(elements2, times2,IntMul)
timefunction(elements1, times1,DivideAndConquer)
timefunction(elements, times,Karatsuba)

plt.plot(elements2, times2, label=name)
plt.plot(elements, times, label=name2)
plt.plot(elements1, times1, label=name1)
plt.xlabel('Number of Digits')
plt.ylabel('Time Complexity')
plt.grid()
plt.legend()

plt.show()