# Problem
# Given two strings A and B, determine if B can be obtained by rotating A any number of times.
# Return 1 if possible, else 0.
# Example
# Input:
# A="abcd"
# B="cdab"
# Output:
# 1

def rotate_string(a,b):
    if len(a) != len(b): return 0
    stack_ = [l for l in a]
    for _ in range(len(stack_)):
        if ''.join(stack_)==b:
            return 1
        stack_.insert(0,stack_.pop())
    return 0

print(rotate_string(input('Enter String A: '), input('Enter String B: ')))