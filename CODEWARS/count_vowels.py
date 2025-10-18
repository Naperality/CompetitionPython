# Count Vowels in sentence
# Vowels are = 'aeiou' or caps

def count_vowels(string_):
    return sum(1 for letter in string_.lower() if letter in 'aeiou')

print(count_vowels(input('Enter sentence: ')))