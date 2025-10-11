# write a program that removes all the vowels of the string

def remove_vowels(string_):
    return ''.join(letter for letter in string_ if letter.lower() not in 'aeiou')

def remove_vowels_iteration(string_):
    for letter in string_:
        if letter.lower() in 'aeiou':
            string_ = string_.replace(letter, "")
    return string_

print(remove_vowels('Hello World 101'), remove_vowels_iteration('Hello World 101'))