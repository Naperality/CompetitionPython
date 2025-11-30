# The Fibonacci numbers are the numbers in the following integer sequence 
# (Fn): 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, ...

# Given a number, say prod (for product), we search two Fibonacci 
# numbers F(n) and F(n+1) verifying:
# Your function takes an integer (prod) and returns an array/tuple 
# (check the function signature/sample tests for the return type in your language):

# if F(n) * F(n+1) = prod:
# (F(n), F(n+1), true)
# If you do not find two consecutive F(n) verifying F(n) * F(n+1) = prod:
# (F(n), F(n+1), false)
# where F(n) is the smallest one such as F(n) * F(n+1) > prod.
# Examples:
# 714 ---> (21, 34, true)
# --> since F(8) = 21, F(9) = 34 and 714 = 21 * 34

# 800 --->  (34, 55, false)

def product_fib(_prod):
    f,n = 0, 1
    while f*n<=_prod:
        if f*n==_prod:
            return [f,n,True]
        t = f+n
        f,n = n,t
    return [f,n,False]

def other_sol(_prod):
    f,n = 0,1
    while f*n<_prod:
        f,n = n,f+n
    return [f,n,_prod==f*n]

print(other_sol(int(input('Enter Number: '))))
print(product_fib(int(input('Enter Number: '))))