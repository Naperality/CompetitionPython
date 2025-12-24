# Given an array of integers.

# Return an array, where the first element is the count of positives numbers 
# and the second element is sum of negative numbers. 0 is neither positive nor negative.

# If the input is an empty array or is null, return an empty array.

# Example
# For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], 
# you should return [10, -65].

def count_positives_sum_negatives(arr):
    if not arr:
        return []
    count_, sum_ = 0,0
    for n in arr:
        if n>0: count_+=1
        else: sum_+=n
    return [count_,sum_]

def other_sol(arr):
    if not arr:
        return []
    x = sum(1 for n in arr if n > 0)
    y = sum(n for n in arr if n < 0)
    return [x,y]

print(count_positives_sum_negatives(list(map(int, input('Enter Array: ').split()))))
print(other_sol(list(map(int, input('Enter Array: ').split()))))