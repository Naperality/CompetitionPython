# Problem Statement

# You are required to implement the following function.

# Int OperationChoices(int c, int n, int a , int b )

# The function accepts 3 positive integers ‘a’ , ‘b’ and ‘c ‘ as its arguments. Implement the function to return.

# ( a+ b ) , if c=1
# ( a – b ) , if c=2
# ( a * b ) ,  if c=3
# (a / b) ,  if c =4
# Assumption : All operations will result in integer output.

# Example:

# Input
# c :1
# a:12
# b:16
# Output:
# 28
# Sample Input

#  c : 2

#  a : 16

#  b : 20

# Sample Output

# -4

def operationsChoices(a, b, c):
    match c:
        case 1:
            return a + b
        case 2:
            return a - b
        case 3:
            return a * b
        case 4:
            return a / b
        case _:
            return ''
        
input_c = int(input("c: "))
input_a = int(input("a: "))
input_b = int(input("b: "))


print(operationsChoices(input_a, input_b, input_c))