# Calculate the end diagonal of the perfect square or matrix with size of n

def calc_diagonal(mat,n):
    prim_diag, sec_diag = 0, 0
    for i in range(n):
        prim_diag += mat[i][i]
        sec_diag += mat[i][n-1-i]    
    return (prim_diag, sec_diag)


def solve_matrix(mat, n):
    for r in range(n - 1):
        for c in range(n - 1):
            # The 2x2 window
            tl = mat[r][c]
            tr = mat[r][c+1]
            bl = mat[r+1][c]
            br = mat[r+1][c+1]
            
            # Check the rule
            if (tl + br) != (tr + bl):
                row_idx = r + 1
                col_idx = c + 1
                
                # Math to find what it SHOULD be
                correct_val = (tr + bl) - tl
                
                # Output exactly what the competition asked for
                return row_idx, col_idx, correct_val
            
x = int(input("Enter size of N: "))

matrix = []

for i in range(x):
    row = list(map(int,input('').split()))
    matrix.append(row)

print(calc_diagonal(matrix,x))
print(solve_matrix(matrix,x))