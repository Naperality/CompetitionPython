# Problem Description :
# The Binary number system only uses two digits, 0 and 1 and 
# number system can be called binary string. You are required to implement the following function:

# int OperationsBinaryString(char* str);

# The function accepts a string str as its argument. 
# The string str consists of binary digits separated with an alphabet as follows:

# – A denotes AND operation
# – B denotes OR operation
# – C denotes XOR Operation
# You are required to calculate the result of the string str, 
# scanning the string to right taking one opearation at a time, and return the same.

# Note:

# No order of priorities of operations is required
# Length of str is odd
# If str is NULL or None (in case of Python), return -1

# Input:
# str: 1C0C1C1A0B1

# Output:
# 1

def binOperation(str):
    if not str or str is None:
        return -1
    
    value = int(str[0])

    for i in range(1, len(str), 2):
        if str[i] == 'A':
            value &= int(str[i+1])
        elif str[i] == 'B':
            value |= int(str[i+1])
        else:
            value ^= int(str[i+1])

    return value

input_bin = input('str: ')
print(binOperation(input_bin))