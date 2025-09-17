# Anagram Checker

# Check if two strings are anagrams (contain the same letters in any order).
# Example:

# Input: listen silent
# Output: YES

def anagramChecker(str1, str2):
    if len(str1) > len(str2):
        string1 = str1
        string2 = str2
    else:
        string1 = str2
        string2 = str1
    for letter in string1:
        if letter not in string2:
            return 'NO'
    return 'YES'

def fastWay(str1, str2):
    return 'YES' if sorted(str1) == sorted(str2) else 'NO'

input_str = input('Input: ').split()
print(f'Output: {anagramChecker(input_str[0], input_str[1])}')
print(f'Output: {fastWay(input_str[0], input_str[1])}')