# Problem
# Write a function that checks whether a given password is acceptable.
# A password is acceptable if:
# Minimum length is 5
# Contains at least one uppercase letter
# Contains at least one digit
# Does not contain space or '*'
# First character must be an alphabet
# Return 1 if valid, else 0.
# Example
# Input: Ab3$k
# Output: 1
# Input: 9Abc1
# Output: 0

def password_validator(string_):
    if len(string_) < 5 or not string_[0].isalpha():
        return 0
    upper_, digit_, space_ = False, False, True 
    for letter in string_:
        if letter.isupper():
            upper_ = True
        if letter.isdigit():
            digit_ = True
        if letter in ('*',' '):
            space_ = False

    return upper_&digit_&space_

def other_sol(string_):
    if len(string_)<5 or not string_[0].isalpha() or any(l in ' *' for l in string_): return 0
    return 1 if any(l.isupper() for l in string_) and any(l.isdigit() for l in string_) else 0

print(password_validator(input('Enter Password: ')))
print(other_sol(input('Enter string: ')))