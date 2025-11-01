# Simple, given a string of words, return the length of the shortest word(s).

# String will never be empty and you do not need to account for different data types.

def shortest_word(string_):
    return min(string_.split(), key = len)

print(shortest_word(input('Enter String: ')))