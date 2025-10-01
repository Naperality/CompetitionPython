def fibonacci(n):
    def fibo(r):
        if r == 0 or r == 1:
            return r
        return fibo(r-1) + fibo(r-2)
    return fibo(n)

def factorial(n):
    def fact(r):
        if r in (0,1):
            return 1
        return r * fact(r-1)
    return fact(n)

for i in range(10+1):
    print(fibonacci(i), end = " ")

print(factorial(5))