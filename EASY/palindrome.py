# Palindrome Check

# Check if a given string is a palindrome (same forwards and backwards).
# Example:

# Input: racecar
# Output: YES

def palindromeChecker(str):
    return str==str[::-1]

input_str = input("Please enter String: ")
print('YES' if palindromeChecker(input_str) else 'NO')