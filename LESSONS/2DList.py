# Concept:
# A 2D list is like a grid or matrix. Access with two indices.
# Example:
# grid = [[1,2,3],
# [4,5,6]]
# print(grid[1][2]) # Output: 6
input_n = int(input("Row of Matrix: "))
input_matrix = [list(map(int, input().split())) for _ in range(input_n)]

# Practice Problem 1: Sum of All Elements
# Input:
# 2 3
# 1 2 3
# 4 5 6
# Output:
# 26

def SumOfAll(matrix):
    return sum(sum(row) for row in matrix)

# Practice Problem 2: Row Sum
# Input:
# 3 3
# 1 2 3
# 4 5 6
# 7 8 9
# Output:
# 6 15 24

def RowSum(matrix):
    return ' '.join(set(str(sum(row)) for row in matrix))

# Practice Problem 3: Column Sum
# Input:
# 2 3
# 1 2 3
# 4 5 6
# Output:
# 5 7 9

from itertools import zip_longest

def ColSum(matrix):
    return ' '.join(str(sum(col)) for col in zip_longest(*matrix, fillvalue = 0))

# or use this iterative version

def IterativeColSum(matrix):
    max_len = max(len(row) for row in matrix)
    res = [sum(row[col] for row in matrix if col < len(row)) for col in range(max_len)]
    return ' '.join(str(num) for num in res)

print(SumOfAll(input_matrix), RowSum(input_matrix), ColSum(input_matrix), IterativeColSum(input_matrix))