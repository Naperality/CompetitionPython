# Binary to Decimal and Decimal to Binary Converter

# Write a program that:

# Converts binary numbers to decimal

# Converts decimal numbers to binary

def binDec(digit, command):
    if command.upper() == 'B2D':
        return int(digit,2)
    else:
        return bin(int(digit))[2:]

def hexOctal(digit):
    print(hex(int(digit))[2:])
    print(oct(int(digit))[2:])

input_num = input('Input (B2D or D2B then number): ').split()
print(f'Output: {binDec(input_num[0], input_num[1])}')
hexOctal(input_num[0])