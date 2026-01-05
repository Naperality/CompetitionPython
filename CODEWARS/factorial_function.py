# Task is to make a factorial function

def factorial(n):
    if n<=1:
        return 1
    return factorial(n-1)*n

def iteratively(n):
    res = 1
    while n>0:
        res*=n
        n-=1
    return res

def factorial_exception_error(n):
    if 0 > n or n > 12:
        raise ValueError('Invalid Input Range!')
    if n == 0:
        return 1
    return n*factorial(n-1)

print(factorial(int(input('Enter Number: '))))
print(iteratively(int(input('Enter Number: '))))
print(factorial_exception_error(int(input('Enter Number: '))))