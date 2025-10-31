# Bob needs a fast way to calculate the volume of a rectangular cuboid 
# with three values: the length, width and height of the cuboid.

# Write a function to help Bob with this calculation.

def rec_cuboid(l,w,h):
    return l*w*h

print(rec_cuboid(int(input('Enter Length: ')), int(input('Enter Width: ')), int(input('Enter Height: '))))