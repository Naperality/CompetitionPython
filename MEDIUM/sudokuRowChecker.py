# Sudoku Row Validator

# Given a 9×9 Sudoku grid, check if each row contains unique numbers from 1 to 9 
# (ignore columns/boxes for now, just rows).

def rowChecker(matrix):
    valid = True
    for row in matrix:
        if sorted(row) != list(range(1,10)):
            valid = False
            break
    return valid


input_matrix = [list(map(int, input('').split())) for _ in range(3)]
print(rowChecker(input_matrix))