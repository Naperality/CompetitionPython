# Concept:
# A list is a collection of items stored in order. You can access by index.
# Example:
# arr = [10, 20, 30]
# print(arr[0]) # Output: 10

input_arr = list(map(int, input("Arr = ").split()))
# Practice Problem 1: Sum of Elements
# Input:
# 5
# 1 2 3 4 5
# Output:
# 15

def SumOfElements(arr):
    return sum(arr)

# Practice Problem 2: Find Maximum
# Input:
# 4
# -1 -7 0 9
# Output:
# 9

def FindMax(arr):
    return max(arr)

# Practice Problem 3: Reverse a List
# Input:
# 5
# 10 20 30 40 50
# Output:
# 50 40 30 20 10

def reverseList(arr):
    return ' '.join(str(num) for num in arr[::-1])

print(SumOfElements(input_arr), FindMax(input_arr), reverseList(input_arr))