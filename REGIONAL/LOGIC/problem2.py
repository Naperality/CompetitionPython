# Problem
# You are given a string made of 0s and 1s separated by operators:
# X → AND
# Y → OR
# Z → XOR
# Evaluate the expression from left to right and return the final binary result.
# Rules
# No operator precedence
# String length is always odd
# Return -1 if string is empty
# Example
# Input:
# "1Z0Y1X1"
# Output:
# 1

def binary_operation(string_):
    total = int(string_[0])
    for i in range(1,len(string_),2):
        if string_[i] == 'X':
            total &= int(string_[i+1])
        if string_[i] == 'Y':
            total |= int(string_[i+1])
        if string_[i] == 'Z':
            total ^= int(string_[i+1])
    return total

print(binary_operation(input('Enter String: ')))