import random
import math

def generate_test_case(n, m):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    s1 = "".join(random.choices(alphabet, k=n-m)) + "".join(random.choices(alphabet, k=m))
    
    return s1, s1[-m:]

    
num_test_cases = 10000
n = 10000
m = 10
j = 0
with open("As2/code/test_cases.txt", "w") as file:
    for i in range(num_test_cases):
        s1, substring = generate_test_case(i+10, math.floor((i+10)/2))
        file.write(s1 + "\n" + substring + "\n" )
        
print("Test cases generated and saved to test_cases.txt")