# # Full Sudoku Validator

# # Given a 9×9 Sudoku grid, check if it is valid.

# # Every row contains numbers 1–9 without repetition.

# # Every column contains numbers 1–9 without repetition.

# # Each 3×3 subgrid contains numbers 1–9 without repetition.

# Example:

# Input: 
# 5 3 4 6 7 8 9 1 2
# 6 7 2 1 9 5 3 4 8
# 1 9 8 3 4 2 5 6 7
# 8 5 9 7 6 1 4 2 3
# 4 2 6 8 5 3 7 9 1
# 7 1 3 9 2 4 8 5 6
# 9 6 1 5 3 7 2 8 4
# 2 8 7 4 1 9 6 3 5
# 3 4 5 2 8 6 1 7 9

# Output:
# Valid

# Input: 9 lines, each with 9 integers separated by spaces.
# Output: YES if valid Sudoku, otherwise NO

def is_valid_sudoku(grid):
    # check rows
    for r in grid:
        if sorted(r) != list(range(1, 10)):
            return False
    # check columns
    for c in range(9):
        col = [grid[r][c] for r in range(9)]
        if sorted(col) != list(range(1, 10)):
            return False
    # check 3x3 boxes
    for br in range(0, 9, 3):
        for bc in range(0, 9, 3):
            box = []
            for r in range(br, br + 3):
                for c in range(bc, bc + 3):
                    box.append(grid[r][c])
            if sorted(box) != list(range(1, 10)):
                return False
    return True

grid = [list(map(int, input().split())) for _ in range(9)]
print("YES" if is_valid_sudoku(grid) else "NO")
