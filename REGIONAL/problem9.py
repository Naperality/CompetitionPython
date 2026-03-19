# Given an integer array, calculate: 
# (sum of elements at prime indices) - (sum of elements at composite indices). 
# Indexing starts at 0. Return 0 if array is empty.
# Example
# Input:
# arr = [5,8,2,7,1,6]
# Output:
# 14

def is_prime(num):
    if num == 2: return True
    if num<2 or num%2==0: return False
    target = int(num**0.5)
    while target>1:
        if num%target == 0: return False
        target-=1
    return True

def sum_prime_composite(array_):
    if not array_: return 0
    primes_t, composites_t = 0,0
    for i,j in enumerate(array_):
        if is_prime(i): primes_t+=j
        elif i>1: composites_t+=j
    return primes_t-composites_t


print(sum_prime_composite(list(map(int, input("Enter Array Numbers: ").split()))))
