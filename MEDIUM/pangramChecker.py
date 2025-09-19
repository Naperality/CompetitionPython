# Pangram Checker

# Check if a given string is a pangram (contains every letter of the English alphabet at least once).
# Example:

# Input: The quick brown fox jumps over the lazy dog
# Output: YES

def pangramChecker(str):
    return 'YES' if set('abcdefghijklmnopqrstuvwxyz').issubset(set(str)) else 'NO'

input_str = input('Input: ')
print(f'Output: {pangramChecker(input_str)}')