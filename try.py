def Fact(n):
    def factorial(r):
        if r in (0,1):
            return 1
        return r * factorial(r-1)
    return factorial(n)


