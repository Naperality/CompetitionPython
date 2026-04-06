# Problem
# Given two strings A and B, determine if B can be obtained by any combination A any number of times.
# Return 1 if possible, else 0.
# Example
# Input:
# A="abcd"
# B="cdab"
# Output:
# 1

def sol_(a,b):
    if len(a) != len(b): return 0
    if sorted(a)==sorted(b): return 1
    return 0







    

print(sol_(input('Enter String A: '), input('Enter String B: ')))