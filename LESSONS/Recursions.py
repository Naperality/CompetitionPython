# Concept:
# A function that calls itself until a base case is met.
# Example:
# def factorial(n):
# if n == 0:
# return 1
# return n * factorial(n-1)

input_n = int(input("Number: "))

# Practice Problem 1: Factorial
# Input:
# 5
# Output:
# 120

def factorial(n):
    def fact(r):
        if r in (0,1):
            return 1
        return r * fact(r-1)
    return fact(n)

# Practice Problem 2: Fibonacci
# Input:
# 6
# Output:
# 8

def fibonacci(n):
    def fibo(r):
        if r in (0,1):
            return r
        return fibo(r - 1) + fibo(r - 2)

# Practice Problem 3: Sum of First N Numbers
# Input:
# 5
# Output:
# 15

print(factorial(input_n))