# Write a function which takes a number as input and returns the sum of the 
# absolute value of each of the number's decimal digits.

# For example: (Input --> Output)

# 10 --> 1
# 99 --> 18
# -32 --> 5
# Let's assume that all numbers in the input will be integer values.
def sum_digits(number):
    # return sum(int(i) for i in str(abs(number)))
    return sum(map(int,str(abs(number))))

def iterative_solution(number):
    res, number = 0, abs(number)    
    while number > 0:
        res += number%10
        number //= 10
    return res

print(sum_digits(int(input('Enter Number: '))))
print(sum_digits(iterative_solution(int(input('Enter Number: ')))))