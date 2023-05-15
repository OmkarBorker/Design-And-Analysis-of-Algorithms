import heapq
import graphviz

# define a function to find the minimum spanning tree using Prim's algorithm
def prim_mst(graph):
    # initialize variables
    mst = set()
    visited = set()
    start_vertex = next(iter(graph))
    visited.add(start_vertex)
    edges = [(weight, start_vertex, to) for to, weight in graph[start_vertex].items()]
    heapq.heapify(edges)

    # loop until all vertices are visited or all edges are explored
    while edges and len(visited) < len(graph):
        # get the edge with the smallest weight
        weight, frm, to = heapq.heappop(edges)
        if to not in visited:
            # add the edge to the minimum spanning tree
            mst.add((frm, to, weight))
            visited.add(to)
            # add the edges from the new vertex to the heap
            for next_to, next_weight in graph[to].items():
                if next_to not in visited:
                    heapq.heappush(edges, (next_weight, to, next_to))

    return mst

# define the graph as a dictionary
graph = {
    'A': {'B': 2, 'C': 3},
    'B': {'C': 1, 'D': 1},
    'C': {'D': 2},
    'D': {}
}

# find the minimum spanning tree
mst = prim_mst(graph)

# display the original graph and the minimum spanning tree using graphviz
dot = graphviz.Graph(comment='Original Graph')
for vertex in graph:
    dot.node(vertex)
for frm, edges in graph.items():
    for to, weight in edges.items():
        if to > frm:
            dot.edge(frm, to, label=str(weight))
dot.render('Minimum_spanning_Tree/Primms algorithm/img/original_graph.gv', view=False, format='png')

dot = graphviz.Graph(comment='Minimum Spanning Tree')
for vertex in graph:
    dot.node(vertex)
for frm, to, weight in mst:
    dot.edge(frm, to, label=str(weight))
dot.render('Minimum_spanning_Tree/Primms algorithm/img/mst.gv', view=False, format='png')
