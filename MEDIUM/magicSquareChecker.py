# Magic Square Validator

# Check if a given square matrix is a magic square.
# (A magic square has the same sum across all rows, columns, and diagonals).

def magicSquareChecker(sqr):
    valid, target = True, sum(sqr[0])

    for row in sqr:
        if sum(row) != target:
            valid = False
    
    for col in range(len(sqr)):
        if sum(sqr[row][col] for row in range(len(sqr))) != target:
            valid = False
    
    if sum(sqr[i][i] for i in range(len(sqr))) != target:
        valid = False
    
    if sum(sqr[i][len(sqr) - 1 - i] for i in range(len(sqr))) != target:
        valid = False
        
    return valid

n = int(input('Enter size of square: '))
input_square = [list(map(int, input('').split())) for _ in range(n)]
print(magicSquareChecker(input_square))