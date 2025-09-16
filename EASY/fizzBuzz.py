# FizzBuzz
# For numbers from 1 to n:
# Print "Fizz" if divisible by 3
# Print "Buzz" if divisible by 5
# Print "FizzBuzz" if divisible by both
# Otherwise, print the number

# Example:
# Input: 5
# Output:
# 1
# 2
# Fizz
# 4
# Buzz

def fizzBuzz(digit):
    num = 1
    while num <= digit:
        if num % 3 == 0 and num % 5 == 0:
            print('FizzBuzz')
        elif num % 3 == 0:
            print('Fizz')
        elif num % 5 == 0:
            print('Buzz')
        else:
            print(num)
        num += 1

input_digit = int(input('Input: '))
print('Output:')
fizzBuzz(input_digit)