# The goal of this exercise is to convert a string to a 
# new string where each character in the new string is "(" 
# if that character appears only once in the original string, 
# or ")" if that character appears more than once in the original string. 
# Ignore capitalization when determining if a character is a duplicate.

# Examples
# "din"      =>  "((("
# "recede"   =>  "()()()"
# "Success"  =>  ")())())"
# "(( @"     =>  "))((" 
# Notes
# Assertion messages may be unclear about what 
# they display in some languages. If you read 
# "...It Should encode XXX", the "XXX" is the expected result, not the input!

from collections import Counter

def duplicate_encoder(word):
    return ''.join('(' if word.lower().count(c)==1 else ')' for c in word.lower())

def other_sol(word):
    return ''.join(')' if Counter(word)[c]>1 else '(' for c in word)

print(duplicate_encoder(input('Enter String to Encode: ')))
print(other_sol(input('Enter String: ')))