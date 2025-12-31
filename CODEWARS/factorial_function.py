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

print(factorial(int(input('Enter Number: '))))
print(iteratively(int(input('Enter Number: '))))