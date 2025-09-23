# You are required to implement the following Function 

# def LargeSmallSum(arr)

# The function accepts an integers arr of size ’length’ as its arguments 
# you are required to return the sum of second largest element from the even positions 
# and second smallest from the odd position of given ‘arr’

# Assumption:

# All array elements are unique
# Treat the 0th position as even
# NOTE

# Return 0 if array is empty
# Return 0, if array length is 3 or less than 3
# Example

# Input

# arr:3 2 1 7 5 4

# Output

# 7

def largeSmallSum(arr):
    if len(arr) <= 3:
        return 0
    
    even, odd = [], []
    for index, num in enumerate(arr):
        if index == 0 or index % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
            
    even.sort(reverse = 1)
    odd.sort()

    return even[1] + odd[1]

input_arr = list(map(int, input("arr: ").split()))

print(largeSmallSum(input_arr))