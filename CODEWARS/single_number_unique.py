# You are given an odd-length array of integers, in which all of them are the same, 
# except for one single number.

# Complete the method which accepts such an array, and returns that single different number.

# The input array will always be valid! (odd-length >= 3)

# Examples
# [1, 1, 2] ==> 2
# [17, 17, 3, 17, 17, 17, 17] ==> 3

def stray(arr):
    return min(arr,key=arr.count)

def stray_other(arr):
    for n in set(arr):
        if arr.count(n)==1:
            return n
    return -1


print(stray(list(map(int,input('Enter Numbers: ').split()))))
