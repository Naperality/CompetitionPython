# Make a program that can calculate the number of substrings in a string or array with 
# length of k

def max_substrings_length(arr_,k_):
    res = 0
    for i in range(len(arr_)):
        temp = min(i+1,k_)
        res+=temp
    return res

print(max_substrings_length(
    list(map(int, input('Enter list of Numbers: ').split())),
    int(input('Enter K(number) max size of substring: '))
))

# Make another program that calculates the number of substrings with
# max sum of limit K 

def max_sum_substring(array_,k_):
    count_, total, left= 0, 0, 0
    for right in range(len(array_)):
        total += array_[right]
        while total > k_ and left <= right:
            total -= array_[left]
            left += 1
        count_ += (right-left+1)
    return count_

print(max_sum_substring(
    list(map(int, input('Enter array of numbers: ').split())),
    int(input('Enter K Sum Limit: '))
))