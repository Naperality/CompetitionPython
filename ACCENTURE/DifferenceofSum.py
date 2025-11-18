# Implement the following Function 

# def differenceofSum(n. m)

# The function accepts two integers n, m as arguments Find the sum of all numbers in 
# range from 1 to m(both inclusive) that are not divisible by n. Return difference 
# between sum of integers not divisible by n with sum of numbers divisible by n.

# Assumption:

# n>0 and m>0
# Sum lies between integral range
# Example

# Input
# n:4
# m:20
# Output
# 90

def differenceOfSum(n,m):
    # return sum(num for num in range(1,m+1) if num % n != 0) - sum(num for num in range(1,m+1) if num % n == 0)
    return sum(num if num%n else -num for num in range(1,m+1))

input_n = int(input("n: "))
input_m = int(input("m: "))

print(differenceOfSum(input_n, input_m))