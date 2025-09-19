# Longest Word in a Sentence

# Find and print the longest word in a sentence.
# Example:

# Input: I love programming challenges
# Output: programming

def longestWord(str):
    return max(str.split(), key = len)

input_str = input('Input: ')
print(f'Output: {longestWord(input_str)}')