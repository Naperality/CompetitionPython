# Problem Statement

# You are given a function,

# Int MaxExponents (int a , int b);

# You have to find and return the number between ‘a’ and ‘b’ 
# ( range inclusive on both ends) which has the maximum exponent of 2.

# The algorithm to find the number with maximum exponent of 2 between the given range is

# Loop between ‘a’ and ‘b’. Let the looping variable be ‘i’.
# Find the exponent (power) of 2 for each ‘i’ and store the number 
# with maximum exponent of 2 so faqrd in a variable , let say ‘max’. Set ‘max’ to 
# ‘i’ only if ‘i’ has more exponent of 2 than ‘max’.
# Return ‘max’.
# Assumption: a <b

# Note: If two or more numbers in the range have the same exponents of  2 , return the small number.

# Example

# Input:
# 7
# 12
# Output:
# 8

def exponent_of_2(n):
    count = 0
    while n % 2 == 0:
        count += 1
        n //= 2 
    return count


def maxExponents(a, b):
    max_num = a
    max_exp = exponent_of_2(a)

    for i in range(a + 1, b + 1):
        current_exp = exponent_of_2(i)
        if current_exp > max_exp:
            max_exp , max_num= current_exp, i
        elif current_exp == max_exp and i < max_num:
            max_num = i

    return max_num

input_a = int(input())
input_b = int(input())

print(maxExponents(input_a, input_b))