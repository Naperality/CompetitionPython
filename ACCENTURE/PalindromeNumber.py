# Instructions: You are required to write the code. 
# You can click on compile and run anytime to check compilation/execution status. 
# The code should be logically/syntactically correct.

# Question: Write a program such that it takes a lower limit and upper limit as inputs 
# and print all the intermediate palindrome numbers.

# Test Cases:

# TestCase 1:
# Input :
# 10 , 80
# Expected Result:
# 11 , 22 , 33 , 44 , 55 , 66 , 77.

# Test Case 2:
# Input:
# 100,200
# Expected Result:
# 101 , 111 , 121 , 131 , 141 , 151 , 161 , 171 , 181 , 191.

def palindromeNumber(a, b):
    result = []
    for num in range(a, b+1):
        if str(num)[::-1] == str(num):
            result.append(num)
    return result

def other_sol(a,b):
    return [num for num in range(a,b+1) if str(num)[::-1] == str(num)]
            

a, b = input().split(", ")
print(palindromeNumber(int(a), int(b)))
print(other_sol(int(a),int(b)))