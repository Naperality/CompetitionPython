# Fibonacci Sequence (First N Terms) Recursively and Iteratively

# Generate the first n numbers of the Fibonacci sequence.
# Example:

# Input: 6
# Output: 0 1 1 2 3 5

def fiboIterative(digit):
    first = 0
    second = 1
    result = [first, second]
    if digit == 1:
        return first
    elif digit <= 2:
        return ' '.join(str(num) for num in result)
    for _ in range(digit-2):
        result.append(first+second)
        temp = first
        first = second
        second += temp
    return ' '.join(str(num) for num in result)

def fastItereative(digit):
    first, second = 0, 1
    for _ in range(digit):
        print(first, end = ' ')
        first, second = second, first + second

def fiboRecursive(digit):
    if digit <= 1:
        return digit
    return fiboRecursive(digit - 1) + fiboRecursive(digit - 2)

input_num = int(input('Input: '))
print(f'Output: {fiboIterative(input_num)}')

print('Output:', end = ' ')
for i in range(input_num):
    print(fiboRecursive(i), end=' ')

print('Output: ', end = ' ')
print(fastItereative(input_num))
