# Problem Statement

# A carry is a digit that is transferred to left if sum of digits exceeds 9 while adding 
# two numbers from right-to-left one digit at a time

# You are required to implement the following function.

# Int NumberOfCarries(int num1 , int num2);

# The functions accepts two numbers ‘num1’ and ‘num2’ as its arguments. 
# You are required to calculate and return  the total number of carries generated 
# while adding digits of two numbers ‘num1’ and ‘ num2’.

# Assumption: num1, num2>=0

# Example:

# Input
# Num 1: 451
# Num 2: 349
# Output
# 2

def numberOfCarries(num1, num2):
    count, temp = 0, 0
    while num1 and num2:
        if num1%10 + num2%10 + temp > 9:
            count += 1
            temp = 1
        else:
            temp = 0
        num1 //= 10
        num2 //= 10
    return count

input_num1 = int(input("Num 1: "))
input_num2 = int(input("Num 2: "))
print(numberOfCarries(input_num1, input_num2))