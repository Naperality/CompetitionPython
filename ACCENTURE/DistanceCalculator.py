# Instructions: You are required to write the code. 
# You can click on compile & run anytime to check the compilation/ 
# execution status of the program. The submitted code should be logically/
# syntactically correct and pass all the test cases.

# Ques: The program is supposed to calculate the sum of  distance between three points from each other.

# For
# x1 = 1 y1 = 1
# x2 = 2 y2 = 4
# x3 = 3 y3 = 6

# Distance is calculated as : sqrt(x2-x1)2 + (y2-y1)2
import math
def DistanceCalculator(x, y, z):
    
    x, y, z = [int(num) for num in x], [int(num) for num in y], [int(num) for num in z]

    diff_one = math.sqrt(pow(y[0]-x[0],2)+pow(y[1]-x[1],2))
    diff_two = math.sqrt(pow(z[0]-y[0],2)+pow(z[1]-y[1],2))
    diff_three = math.sqrt(pow(z[0]-x[0],2)+pow(z[1]-x[1],2))

    return f'{round(diff_one, 2)}, {round(diff_two, 2)}, and {round(diff_three, 2)}'
    
input_one = input("Point 1: ").split()
input_two = input("Point 2: ").split()
input_three = input("Point 3: ").split()

print(DistanceCalculator(input_one, input_two, input_three))
