# Prime Number Check

# Check if a number n is prime.
# Example:

# Input: 7
# Output: YES

def primeChecker(digit):
    if digit < 2:
        return 'NO'
    for num in range(2, int(digit ** 0.5) + 1):
        if digit % num == 0:
            return 'NO'
    return 'YES'

input_digit = int(input('Input: '))
print(f'Output: {primeChecker(input_digit)}')