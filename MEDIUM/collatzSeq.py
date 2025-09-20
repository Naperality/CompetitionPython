# Collatz Sequence

# Given a number n, generate its Collatz sequence until it reaches 1.

# If n is even → divide by 2

# If n is odd → multiply by 3 and add 1
# Example:

# Input: 6
# Output: 6 3 10 5 16 8 4 2 1

def collatz(digit):
    while digit != 1:
        print(digit, end = ' ')
        if digit % 2 == 0:
            digit//=2
        else:
           digit = digit*3+1

input_num = int(input('Input: '))
print(f'Output: ')
collatz(input_num)