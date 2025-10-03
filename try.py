def Fact(n):
    def factorial(r):
        if r in (0,1):
            return 1
        return r * factorial(r-1)
    return factorial(n)


input_n = int(input("Factorial of : "))
print(Fact(input_n))
