# Problem Statement

# You are given a function,

# Void *ReplaceCharacter(Char str[], int n, char ch1, char ch2);

# The function accepts a string  ‘ str’ of length n and two characters 
# ‘ch1’ and ‘ch2’ as its arguments . 
# Implement the function to modify and return the string 
# ‘ str’ in such a way that all occurrences of ‘ch1’ in original 
# string are replaced by ‘ch2’ and all occurrences of ‘ch2’  in original string are replaced by ‘ch1’.

# Assumption: String Contains only lower-case alphabetical letters.

# Note:

# Return null if string is null.
# If both characters are not present in string or both of them are same , then return the string unchanged.
# Example:

# Input:
# Str: apples
# ch1:a
# ch2:p
# Output:
# paales

def ReplaceCharacter(character_string, char1, char2):
    temp = character_string.translate(str.maketrans({char2:char1, char1:char2}))
    if not character_string:
        return ''
    
    return temp

input_str = input("Str: ")
input_ch1 = input("ch1: ")
input_ch2 = input("ch2: ")

print(ReplaceCharacter(input_str, input_ch1, input_ch2))