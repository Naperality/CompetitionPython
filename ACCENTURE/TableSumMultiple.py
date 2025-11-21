# Instructions: You are required to write the code. 
# You can click on compile and run anytime to check compilation/execution status. 
# The code should be logically/syntactically correct.

# Problem: Write a program to display the table of a number and print the sum of 
# all the multiples in it.

# Test Cases:

# Test Case 1:
# Input:
# 5
# Expected Result Value:
# 5, 10, 15, 20, 25, 30, 35, 40, 45, 50
# 275

# Test Case 2:
# Input:
# 12
# Expected Result Value:
# 12, 24, 36, 48, 60, 72, 84, 96, 108, 120
# 660

def MultipleSum(num):
    arr = [digit*num for digit in range(1,11)]
    result_sum = sum(arr)

    result_str = ''.join(str(digit)+', ' if index != len(arr)-1 else str(digit) for index, digit in enumerate(arr))

    print(result_str)
    print(result_sum)

def other_sol(n):
    return ', '.join(str(d*n) for d in range(1,11))+f'\n{sum(d*n for d in range(1,11))}'

MultipleSum(int(input()))
print(other_sol(int(input('Enter Number: '))))
