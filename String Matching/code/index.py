import time

#Brute Force Approach
def brute_force(s, p):
    n = len(s)
    m = len(p)
    for i in range(n-m+1):
        if s[i:i+m] == p:
            return i
    return -1

#KMP Algorithm
def kmp(s, p):
    n = len(s)
    m = len(p)
    pi = [0] * m
    j = 0
    for i in range(1, m):
        while j > 0 and p[j] != p[i]:
            j = pi[j-1]
        if p[j] == p[i]:
            j += 1
        pi[i] = j
    j = 0
    for i in range(n):
        while j > 0 and s[i] != p[j]:
            j = pi[j-1]
        if s[i] == p[j]:
            j += 1
        if j == m:
            return i - m + 1
    return -1

with open("As2/code/test_cases.txt", "r") as file, open("As2/code/output1.txt", "w") as outfile:
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
            
with open("As2/code/test_cases.txt", "r") as file, open("As2/code/output2.txt", "w") as outfile:
    for i, line in enumerate(file):
        if i % 2 == 0:
            s1 = line.strip()
        else:
            pat = line.strip()
            start_time = time.time()
            kmp(s1, pat)
            end_time = time.time()
            elapsed_time = end_time - start_time
            outfile.write(f"{len(s1)} {elapsed_time}\n")

print("Test cases generated and saved to test_cases.txt") 
print("Running times saved to output.txt")