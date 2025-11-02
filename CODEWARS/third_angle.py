# You are given two interior angles (in degrees) of a triangle.

# Write a function to return the 3rd.

# Note: only positive integers will be tested.

def third_angle(a,b):
    return 180 - a - b

print(third_angle(*map(int, input('Enter A and B: ').split())))