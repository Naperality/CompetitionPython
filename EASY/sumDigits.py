# Sum of Digits

# Find the sum of all digits in an integer.
# Example:

# Input: 1234
# Output: 10

def sumDigits(digit):
    sum = 0
    while digit > 0:
        sum += digit % 10
        digit //= 10
    return sum

def fastWay(digit):
    return sum(int(num) for num in str(digit))

input_digit = int(input("Input: "))
print(f'Output: {sumDigits(input_digit)}')
print(f'Output: {fastWay(input_digit)}')