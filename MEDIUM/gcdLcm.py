# GCD and LCM Calculator

# Write a program that takes two integers and 
# outputs both their GCD (Greatest Common Divisor) and 
# LCM (Least Common Multiple).

import math
def gcdLcm(a, b):
    result = 'GCD -> ' + str(math.gcd(a,b)) + ' LCM -> ' + str(abs(a*b)//math.gcd(a,b))
    return result

a, b = map(int, input('Input: ').split())

print(f'Output: {gcdLcm(a, b)}')