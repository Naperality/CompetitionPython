# Given an array of integers, return a new array with each value doubled.

# For example:

# [1, 2, 3] --> [2, 4, 6]

def doubled_arr(arr_):
    return [num*2 for num in arr_]

print(doubled_arr(list(map(int, input('Enter Array of Numbers: ').split()))))