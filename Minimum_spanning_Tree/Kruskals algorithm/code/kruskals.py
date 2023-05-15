import graphviz

def kruskal_mst(graph):
    edges = [(weight, frm, to) for frm, edges in graph.items() for to, weight in edges.items()]
    edges.sort()

    mst = set()
    parent = {vertex: vertex for vertex in graph}

    def find(vertex):
        if parent[vertex] == vertex:
            return vertex
        parent[vertex] = find(parent[vertex])
        return parent[vertex]

    def union(frm, to):
        parent[find(frm)] = find(to)

    for weight, frm, to in edges:
        if find(frm) != find(to):
            mst.add((frm, to, weight))
            union(frm, to)

    return mst

graph = {
    'A': {'B': 2, 'C': 3},
    'B': {'C': 1, 'D': 1},
    'C': {'D': 2},
    'D': {}
}

mst = kruskal_mst(graph)

dot = graphviz.Graph(comment='Original Graph')
for vertex in graph:
    dot.node(vertex)
for frm, edges in graph.items():
    for to, weight in edges.items():
        dot.edge(frm, to, label=str(weight))
dot.render('Minimum_spanning_Tree/Kruskals algorithm/img/original_graph.gv', view=False, format='png')

dot = graphviz.Graph(comment='Minimum Spanning Tree')
for vertex in graph:
    dot.node(vertex)
for frm, to, weight in mst:
    dot.edge(frm, to, label=str(weight))
dot.render('Minimum_spanning_Tree/Kruskals algorithm/img/mst.gv', view=False, format='png')
