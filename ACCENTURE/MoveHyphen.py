# Implement the following functions.a

# char*MoveHyphen(char str[],int n);

# The function accepts a string “str” of length ‘n’, 
# that contains alphabets and hyphens (-). Implement the function to move 
# all hyphens(-) in the string to the front of the given string.

# NOTE:- Return null if str is null.

# Example :-

# Input:
# str: Move-Hyphens-to-Front
# Output:
# ---MoveHyphenstoFront

def MoveHyphen(str):
    result, count = '', 0
    for char in str:
        if char == '-':
            count += 1
        else:
            result += char
    
    return '-'*count + result

input_str = input("str: ")

print(MoveHyphen(input_str))
