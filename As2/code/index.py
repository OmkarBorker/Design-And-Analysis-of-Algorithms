import time

def brute_force(s, p):
    n = len(s)
    m = len(p)
    for i in range(n-m+1):
        if s[i:i+m] == p:
            return i
    return -1

with open("As2/code/test_cases.txt", "r") as file, open("As2/code/output.txt", "w") as outfile:
    for i, line in enumerate(file):
        if i % 2 == 0:
            s1 = line.strip()
        else:
            pat = line.strip()
            start_time = time.time()
            brute_force(s1, pat)
            end_time = time.time()
            elapsed_time = end_time - start_time
            outfile.write(f"{len(s1)} {elapsed_time}\n")

print("Test cases generated and saved to test_cases.txt") 
print("Running times saved to output.txt")