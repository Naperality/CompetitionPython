# You are given a function.
# int CheckPassword(char str[], int n);
# The function accepts string str of size n as an 
# argument. Implement the function which returns 1 if given string str is valid password else 0.
# str is a valid password if it satisfies the below conditions.

# – At least 4 characters
# – At least one numeric digit
# – At Least one Capital Letter
# – Must not have space or slash (/)
# – Starting character must not be a number
# Assumption:
# Input string will not be empty.

# Example:

# Input 1:
# aA1_67
# Input 2:
# a987 abC012

# Output 1:
# 1
# Output 2:
# 0

def CheckPassword(str, n):

    numeric, capital, spaceSlash = False, False, False
    
    if (n < 4) or str[0].isdigit():
        return 0
    
    for char in str:
        if char.isdigit():
            numeric = True
        if char.isupper():
            capital = True
        if char.isspace() or char in '\/':
            spaceSlash = True
        
    return int(numeric and capital and not spaceSlash)
            
def other_sol(str,n):
    if n<4 or str[0].isdigit() or '\/' in str:
        return 0
    return 

input_str = input()
input_len = input()

print(CheckPassword(input_str, int(input_len)))
