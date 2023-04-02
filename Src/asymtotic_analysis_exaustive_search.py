import time
from numpy.random import seed
from numpy.random import randint
import matplotlib.pyplot as plt
import networkx as nx
from itertools import combinations
from random import random
from sys import maxsize
from itertools import permutations

def travellingSalesmanProblem(graph, s, V):
 
    vertex = []
    for i in range(V):
        if i != s:
            vertex.append(i)

    min_path = maxsize
    next_permutation=permutations(vertex)
    for i in next_permutation:
        current_pathweight = 0
        k = s
        for j in i:
            current_pathweight += graph[k][j]
            k = j
        current_pathweight += graph[k][s]
        min_path = min(min_path, current_pathweight)
         
    return min_path


## HELPER FOR GRAPH GENRATION
def ER(n, p):
    V = set([v for v in range(n)])
    E = set()
    for combination in combinations(V, 2):
        a = random()
        if a < p:
            E.add(combination)

    g = nx.Graph()
    g.add_nodes_from(V)
    g.add_edges_from(E)

    return g

p = 0.4
s = 0
name = "Traveling Salesman"
name1 = "Assignment problem"
name2 = "KnapSack problem"

elements = list()
elements1 = list()
elements2 = list()

times = list()
times1 = list()
times2 = list()

def timefunction(elements, times, fun):
    for i in range(2,5):

        G = ER(i, p)
        start = time.time()
        fun(G,s,i)
        end = time.time()
        print(len(i) + "x" + len(i), end-start)
        elements.append(len(i))
        times.append(end-start)
        
timefunction(elements, times, travellingSalesmanProblem)

plt.plot(elements, times, label=name2)
# plt.plot(elements1, times1, label=name1)
plt.xlabel('Number of Digits')
plt.ylabel('Time Complexity')
plt.grid()
plt.legend()

plt.show()