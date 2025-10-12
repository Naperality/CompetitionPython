# Complete the square sum function so that it squares each number passed into it 
# and then sums the results together.

# For example, for [1, 2, 2] it should return 9 because 
# 1^2 + 2^2 + 2^2 = 9

def square_sum(num_arr):
    return sum(num**2 for num in num_arr)

input_num = list(map(int, input("Enter Array: ").split()))
print(square_sum(input_num))