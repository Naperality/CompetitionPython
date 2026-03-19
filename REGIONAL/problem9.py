# Given an integer array, calculate: 
# (sum of elements at prime indices) - (sum of elements at composite indices). 
# Indexing starts at 0. Return 0 if array is empty.
# Example
# Input:
# arr = [5,8,2,7,1,6]
# Output:
# -4

def is_prime(num):
    target = int(num**1/2)
    while target!=0:
        if num%target == 0: return False
        target-=1
    return True

def sum_prime_composite(array_):
    if not array_: return 0
    primes_t, composites_t = 0,0
    for i,j in enumerate(array_):
        if is_prime(i): primes_t+=j
        else: composites_t+=j
    return primes_t-composites_t


print(sum_prime_composite(list(map(int, input("Enter Array Numbers: ").split()))))
