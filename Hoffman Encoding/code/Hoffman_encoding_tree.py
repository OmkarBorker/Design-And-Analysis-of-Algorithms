import heapq
import graphviz

class Node:
    def __init__(self, char=None, freq=0):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_tree(freq_dict):
    heap = []
    for char, freq in freq_dict.items():
        heapq.heappush(heap, Node(char, freq))
    while len(heap) > 1:
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)
        parent = Node(freq=node1.freq + node2.freq)
        parent.left = node1
        parent.right = node2
        heapq.heappush(heap, parent)
    return heap[0]

def build_codebook(node, code="", codebook={}):
    if node.char:
        codebook[node.char] = code
        return
    build_codebook(node.left, code+"0", codebook)
    build_codebook(node.right, code+"1", codebook)

def display_tree(node, g):
    if node.left:
        g.edge(str(node.freq), str(node.left.freq), "0")
        display_tree(node.left, g)
    if node.right:
        g.edge(str(node.freq), str(node.right.freq), "1")
        display_tree(node.right, g)

freq_dict = {'a': 0.1, 'b': 0.25, 'c': 0.15, 'd': 0.2, 'e': 0.05}
huffman_tree = build_tree(freq_dict)
codebook = {}
build_codebook(huffman_tree, code="", codebook=codebook)
print("Huffman Codebook:", codebook)

g = graphviz.Graph(format="png")
g.node(str(huffman_tree.freq))
display_tree(huffman_tree, g)
g.view()
