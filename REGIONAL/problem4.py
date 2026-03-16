# Problem
# Given an array of integers, a target value k, and a tolerance t,
# count how many elements satisfy:
# |element − k| < t
# Rules
# Return -1 if no such elements exist
# Example
# Input:
# arr = [10, 15, 20, 25, 30]
# k = 22
# t = 4
# Output:
# 2

def abs_diff_count(array_,k,t):
    count_ = 0
    for num in array_:
        if abs(num - k)<t: count_+=1
    return count_ if count_>0 else -1

print(abs_diff_count(list(map(int,input('Enter Array: ').split())),
                     int(input('Enter Target Value: ')), 
                     int(input('Enter Tolerance: '))))
