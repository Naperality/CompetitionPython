# Problem Statement :

# An Autobiographical Number is a number N such that 
# the first digit of N represents the count of how many zeroes are there in N, 
# the second digit represents the count of how many ones are there in N and so on.

# You are given a function, def FindAutoCount(n):

# The function accepts string “n” which is a 
# number and checks whether the number is an autobiographical number or not. 
# If it is, an integer is returned, i.e. the count of distinct numbers in ‘n’. If not, it returns 0.

# Assumption:

# The input string will not be longer than 10 characters.
# Input string will consist of numeric characters.
# Note:

# If string is None return 0.

# Example:

# Input:

# n: “1210”

# Output:

# 3

def findAutoCount(string_num):
    if string_num is None:
        return 0
    no_duplicate = set()
    for index, num in enumerate(string_num):
        no_duplicate.add(num)
        if int(num) != sum(1 for digit in string_num if int(digit) == int(index)):
            return 0
    return len(no_duplicate)

def fasterSolution(string_num):
    if string_num is None:
        return 0
    arr_freq = [0]*10

    for digit in string_num:
        arr_freq[int(digit)] += 1

    for index, num in enumerate(string_num):
        if int(num) != arr_freq[index]:
            return 0
    
    return len(set(string_num))

input_string_num = input("n: ")
print(findAutoCount(input_string_num))
print(fasterSolution(input_string_num))