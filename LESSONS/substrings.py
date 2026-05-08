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