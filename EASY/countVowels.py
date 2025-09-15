# Count Vowels

# Count how many vowels (a, e, i, o, u) are in a given string.
# Example:

# Input: programming
# Output: 3

def countVowels(str):
    count = 0
    for letter in str:
        if letter in ['a','e','i','o','u']:
            count += 1
    return count

input_str = input('Input: ')
print(f'Output: {countVowels(input_str)}')