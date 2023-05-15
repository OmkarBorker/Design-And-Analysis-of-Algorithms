import math
import heapq
import numpy as np
from graphviz import Digraph
from graphviz import Graph

graph = np.array([[0, 2, 6, 1, 0],
                  [2, 0, 3, 2, 2],
                  [6, 3, 0, 0, 4],
                  [1, 2, 0, 0, 3],
                  [0, 2, 4, 3, 0]])

start = 0

distances = [math.inf] * len(graph)
previous = [None] * len(graph)

distances[start] = 0

pq = [(0, start)]

while pq:
    (distance, node) = heapq.heappop(pq)
    
    if distance > distances[node]:
        continue
        
    for neighbor, weight in enumerate(graph[node]):
        if weight > 0:
            new_distance = distances[node] + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                previous[neighbor] = node
                heapq.heappush(pq, (new_distance, neighbor))

print("Table:")
print("Node\tDistance\tPrevious")
for i, (d, p) in enumerate(zip(distances, previous)):
    print(f"{i}\t{d}\t\t{p}")

dot_original = Graph()
for i in range(len(graph)):
    dot_original.node(str(i))
    for j in range(i+1, len(graph)):
        if graph[i, j] > 0:
            dot_original.edge(str(i), str(j), label=str(graph[i, j]))

dot_shortest = Digraph()
for i in range(len(graph)):
    dot_shortest.node(str(i))
    if previous[i] is not None:
        dot_shortest.edge(str(previous[i]), str(i), label=str(graph[previous[i], i]))
dot_original.render("Single_Source_Shortest_Path/Img/graph_s", format="png", view=True)
dot_shortest.render("Single_Source_Shortest_Path/Img/graph_i", format="png", view=True)
