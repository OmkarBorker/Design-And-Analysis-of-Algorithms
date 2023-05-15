import heapq
import matplotlib.pyplot as plt
import time

class HuffmanNode:
    def __init__(self, char=None, freq=None, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(freq_dict):
    pq = [HuffmanNode(k, v) for k, v in freq_dict.items()]
    heapq.heapify(pq)

    while len(pq) > 1:
        left_node = heapq.heappop(pq)
        right_node = heapq.heappop(pq)

        merged_node = HuffmanNode(left=left_node, right=right_node, freq=left_node.freq+right_node.freq)
        heapq.heappush(pq, merged_node)

    return pq[0]

def build_codebook(node, code="", codebook={}):
    if node.char:
        codebook[node.char] = code
        return

    build_codebook(node.left, code+"0", codebook)
    build_codebook(node.right, code+"1", codebook)

def huffman_encoding(text):
    freq_dict = {}
    for char in text:
        freq_dict[char] = freq_dict.get(char, 0) + 1

    if len(freq_dict) == 1:
        char, freq = list(freq_dict.items())[0]
        return "0"*freq, {char: "0"}

    huffman_tree = build_huffman_tree(freq_dict)
    codebook = {}
    build_codebook(huffman_tree, code="", codebook=codebook)

    encoded_text = "".join([codebook[char] for char in text])
    return encoded_text, codebook

def huffman_decoding(encoded_text, codebook):
    rev_codebook = {v: k for k, v in codebook.items()}
    decoded_text = ""
    code = ""
    for bit in encoded_text:
        code += bit
        if code in rev_codebook:
            decoded_text += rev_codebook[code]
            code = ""
    return decoded_text

if __name__ == "__main__":
    min_input_size = 100
    max_input_size = 10000
    input_sizes = range(min_input_size, max_input_size + 1, 100)
    time_complexity = []
    for size in input_sizes:
        text = "a"*size
        start_time = time.time()
        encoded_text, codebook = huffman_encoding(text)
        decoded_text = huffman_decoding(encoded_text, codebook)
        end_time = time.time()
        time_complexity.append(end_time - start_time)
    plt.plot(input_sizes, time_complexity, '-o')
    plt.xlabel('Input Size')
    plt.ylabel('Time (in seconds)')
    plt.title('Time Complexity Analysis of Huffman Algorithm')
    plt.show()