import random
import math

def generate_test_case(n, m):
    alphabet = "abcdefghijklmnopqrstuvw"
    test = "x"
    s1 = "".join(random.choices(test, k=n-m)) + "".join(random.choices(test, k=(m-1))) +"".join(random.choices(alphabet,k=1))
    
    return s1, s1[-m:]

    
num_test_cases = 500
m = 1000
i = 100
with open("As2/code/test_cases.txt", "w") as file:
    for i in range(num_test_cases):
        s1, substring = generate_test_case(1000*(i), m)
        file.write(s1 + "\n" + substring + "\n" )
        
print("Test cases generated and saved to test_cases.txt")