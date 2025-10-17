# Welcome.

# In this kata you are required to, given a string, replace every letter with its 
# position in the alphabet.

# If anything in the text isn't a letter, ignore it and don't return it.

# "a" = 1, "b" = 2, etc.

# Example
# Input = "The sunset sets at twelve o' clock."
# Output = "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"

def pos_alphabet(string_):
    # res = []
    # for letter in string_:
    #     base = ord('A') if letter.isupper() else ord('a')
    #     if letter.isalpha():
    #         res.append((ord(letter)-base)%26+1)
    # return ' '.join(str(num) for num in res)
    return ' '.join(str(ord(letter) - ord('a')+1) for letter in string_.lower() if letter.isalpha())


print(pos_alphabet(input("Enter String: ")))