# Word Frequency Counter

# Write a program that counts how many times each word appears in a given sentence.
# Example:

# Input: the cat and the dog and the cat
# Output:
# the 2
# cat 2
# and 2
# dog 1
import collections

def wordCounter(str):
    for word, freq in collections.Counter(str.split()).items():
        print(word, freq)

input_str = input('Input: ')
print(f'Output: ')
wordCounter(input_str)