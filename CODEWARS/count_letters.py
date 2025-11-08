# Create a function that accepts a string and a single character, and 
# returns an integer of the count of occurrences the 2nd argument is found in the first one.

# If no occurrences can be found, a count of 0 should be returned.

# ("Hello", 'o')  =>  1
# ("Hello", 'l')  =>  2
# ("", 'z')       =>  0
# Notes
# The first argument can be an empty string
# In languages with no distinct character data type, the second argument will 
# be a string of length 1
from collections import Counter

def letter_count(str_, letter_):
    # return Counter(str_).get(letter_) if letter_ in str_ else 0
    return str_.count(letter_)

print(letter_count(input('Enter String: '), input('Enter Letter to Count: ')))