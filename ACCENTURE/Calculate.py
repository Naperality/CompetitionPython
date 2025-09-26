# Problem Statement

# You are required to implement the following function:

# Int Calculate(int m, int n);

# The function accepts 2 positive integer ‘m’ and ‘n’ as its arguments.
# You are required to calculate the sum of numbers divisible both by 3 and 5, 
# between ‘m’ and ‘n’ both inclusive and return the same.
# Note
# 0 < m <= n

# Example

# Input:

# m : 12

# n : 50

# Output

# 90

def calculate(m, n):
    return sum(num for num in range(m, n+1) if num % 3 == 0 and num % 5 == 0)

input_m = int(input("m : "))
input_n = int(input("n : "))

print(calculate(input_m, input_n))