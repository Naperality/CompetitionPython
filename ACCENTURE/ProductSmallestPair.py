# def ProductSmallestPair(sum, arr)

# The function accepts an integers sum and an integer array arr of size n. 
# Implement the function to find the pair, (arr[j], arr[k]) 
# where j!=k, Such that arr[j] and arr[k] are the least two elements of 
# array (arr[j] + arr[k] <= sum) and return the product of element of this pair

# NOTE

# Return -1 if array is empty or if n<2
# Return 0, if no such pairs found
# All computed values lie within integer range
# Example

# Input

# sum:9

# size of Arr = 7

# Arr:5 2 4 3 9 7 1

# Output

# 2

def ProductSmallestPair(sum, arr):
    if not arr or len(arr) < 2:
        return -1
    
    sorted_arr = sorted(arr)
    return sorted_arr[0]*sorted_arr[1] if sorted_arr[0]+sorted_arr[1] <= sum else 0

def other_sol(sum_, arr_):
    if not arr_ or len(arr_)<2:
        return -1
    a,b = sorted(arr_)[:2]
    return a*b if a+b<=sum_ else 0
    

input_sum = int(input("sum: "))
input_arr = list(map(int, input("Arr: ").split()))

print(ProductSmallestPair(input_sum, input_arr))
print(other_sol(input_sum, input_arr))