# Armstrong Number Checker

# A number is called an Armstrong number 
# if the sum of its digits raised to the power of the number of digits equals the number itself.
# Example:

# Input: 153
# Output: YES   # (1^3 + 5^3 + 3^3 = 153)

def armstrongChecker(digit):
    return 'YES' if sum(int(num)**len(digit) for num in digit) == int(digit) else 'NO'

input_digit = input('Input: ')
print(f'Output: {armstrongChecker(input_digit)}')