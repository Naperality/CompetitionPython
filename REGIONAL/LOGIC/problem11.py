# Make a program to calculate the Area of the Regular Pentagon
import math
def area_(side_ = 1):
    res = ((math.sqrt(5*(5+(2*math.sqrt(5))))/4))*side_**2
    return f'Area is: {res}'

print(area_(float(input('Enter one side: '))))