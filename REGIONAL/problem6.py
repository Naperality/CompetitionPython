# Problem
# From an array:
# Extract elements at even indices
# Extract elements at odd indices
# Return:
# (second largest even-index value)
# +
# (second smallest odd-index value)
# Rules
# Return 0 if array size ≤ 3
# All values are unique
# Example
# Input:
# [9, 4, 7, 1, 6, 3]
# Output:
# 10

def even_odd_diff(array_):
    if len(array_) < 4:
        return 0
    res_, even_, odd_ = 0, [], []
    for i in range(len(array_)):
        if i%2==0:
            even_.append(array_[i])
        else:
            odd_.append(array_[i])
    res_ = sorted(even_, reverse=1)[1]+sorted(odd_)[1]
    return res_

print(even_odd_diff(list(map(int, input('Enter numbers: ').split()))))