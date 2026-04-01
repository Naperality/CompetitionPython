def swap_bitwise(num1, num2):
    print(f'Before swapping: num1 = {num1}, num2 = {num2}')
    num1^=num2; num2^=num1; num1^=num2
    return f'After swapping: num1 = {num1}, num2 = {num2}'

x,y = int(input('Enter num1: ')), int(input('Enter num2: '))
print(swap_bitwise(x,y))