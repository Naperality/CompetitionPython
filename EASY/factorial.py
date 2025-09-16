# Factorial (Iterative) and (Recursively)

# Write a program to compute the factorial of a given number n.
# Example:

# Input: 5
# Output: 120

def factorialBasic(digit):
    result = 1
    while digit:
        result *= digit
        digit -= 1
    return result

def factRecursive(digit):
    if digit == 0:
        return 1
    else:
        return digit * factRecursive(digit - 1)

input_digit = int(input('Input: '))
print(f'Output: {factorialBasic(input_digit)}')
print(f'Output: {factRecursive(input_digit)}')