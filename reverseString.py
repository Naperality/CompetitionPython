# Write a program that takes a string and prints it in reverse.
# Example:

# Input: hello
# Output: olleh

def reverse(str):
    return str[::-1]

input_str = input('Please Enter String: ')
print(f'Reversed of {input_str} is {reverse(input_str)}')