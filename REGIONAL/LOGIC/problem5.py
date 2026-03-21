# Problem
# Given two integers x and y, calculate:
# (sum of numbers from 1 to y NOT divisible by x)
# −
# (sum of numbers from 1 to y divisible by x)
# Example
# Input:
# x = 5
# y = 15
# Output:
# 60

def divisible_count(x,y):
    return sum(n if not n%x==0 else -n for n in range(1,y+1))

print(divisible_count(int(input('Enter X: ')), int(input('Enter Y: '))))