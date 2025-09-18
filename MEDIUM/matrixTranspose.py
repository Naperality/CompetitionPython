# Matrix Transpose

# Given an n x m matrix, print its transpose.
# Example:

# Input:
# 1 2 3
# 4 5 6
# Output:
# 1 4
# 2 5
# 3 6

def matrixTranspose(matrix, m, n):
    for i in range(m):
        for j in range(n):
            print(matrix[j][i], end = ' ')
        print()

n, m = map(int, input('Enter rows and columns: ').split())
ogMatrix = [list(map(int, input().split())) for _ in range(n)]

print(ogMatrix)
matrixTranspose(ogMatrix, m, n)