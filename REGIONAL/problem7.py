# Problem
# Given an integer array and a limit L, find the two smallest distinct elements
# whose sum is ≤ L, and return their product.
# Rules
# Return -1 if array size < 2
# Return 0 if no valid pair exists
# Example
# Input:
# L = 8
# arr = [6, 1, 2, 9, 4]
# Output:
# 2

def smallest_pair_prod(array_,l):
    if not array_ or len(array_)<2: return -1
    sorted_ = sorted(array_)
    if sorted_[0]+sorted_[1] <= l: return sorted_[0]*sorted_[1]
    return 0
    

print(smallest_pair_prod(list(map(int,input('Enter Numbers: ').split())),
                         int(input('Enter Limit: '))))