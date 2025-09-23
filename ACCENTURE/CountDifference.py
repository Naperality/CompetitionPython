# You are given a function,
# int findCount(int arr[], int length, int num, int diff);

# The function accepts an integer array ‘arr’, its length 
# and two integer variables ‘num’ and ‘diff’. 
# Implement this function to find and return the number of elements of ‘arr’ 
# having an absolute difference of less than or equal to ‘diff’ with ‘num’.
# Note: In case there is no element in ‘arr’ whose absolute difference with ‘num’ 
# is less than or equal to ‘diff’, return -1.

# Example:
# Input:

# arr: 12 3 14 56 77 13
# num: 13
# diff: 2
# Output:
# 3

def countDifference(arr, length, num, diff):
    result = sum(1 for digit in arr if abs(digit - num) <= diff)
    return result if result != 0 else -1

input_arr = list(map(int, input("arr: ").split()))
input_num = int(input("num: "))
input_diff = int(input("diff: "))

print(countDifference(input_arr, len(input_arr), input_num, input_diff))