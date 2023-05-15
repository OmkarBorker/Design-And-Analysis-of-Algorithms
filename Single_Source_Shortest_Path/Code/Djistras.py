import math
import heapq
import numpy as np
from graphviz import Digraph
from graphviz import Graph

# Define the example graph as an adjacency matrix
graph = np.array([[0, 2, 6, 1, 0],
                  [2, 0, 3, 2, 2],
                  [6, 3, 0, 0, 4],
                  [1, 2, 0, 0, 3],
                  [0, 2, 4, 3, 0]])

# Define the start node
start = 0

# Initialize the distances and previous nodes
distances = [math.inf] * len(graph)
previous = [None] * len(graph)

# Set the distance to the start node to 0
distances[start] = 0

# Create a priority queue for the nodes to visit
pq = [(0, start)]

# Run Dijkstra's algorithm
while pq:
    # Get the node with the smallest distance from the priority queue
    (distance, node) = heapq.heappop(pq)
    
    # Check if this distance is already outdated
    if distance > distances[node]:
        continue
        
    # Update the distances and previous nodes for the neighbors of this node
    for neighbor, weight in enumerate(graph[node]):
        if weight > 0:
            new_distance = distances[node] + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                previous[neighbor] = node
                heapq.heappush(pq, (new_distance, neighbor))

# Print the table of distances and previous nodes
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

# Create a graphviz visualization of the graph and the shortest paths
dot_shortest = Digraph()
for i in range(len(graph)):
    dot_shortest.node(str(i))
    if previous[i] is not None:
        dot_shortest.edge(str(previous[i]), str(i), label=str(graph[previous[i], i]))
dot_original.render("Single_Source_Shortest_Path/Img/graph_s", format="png", view=True)
dot_shortest.render("Single_Source_Shortest_Path/Img/graph_i", format="png", view=True)
