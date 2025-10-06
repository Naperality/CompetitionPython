# Concept:
# Backtracking tries all possibilities and undoes wrong ones.
# Example: Generate all binary strings of length n.

# Practice Problem 1: Generate All Binary Strings
# Input:
# 3
# Output:
# 000
# 001
# 010
# 011
# 100
# 101
# 110
# 111

input_n = int(input("Number: "))

def GenBinPerm(n):
    current = []
    def backtrack(r):
        if len(current) == r:
            print(''.join(current))
            return
        current.append('0')
        backtrack(r)  
        current.pop()
        current.append('1')
        backtrack(r) 
        current.pop()
    backtrack(n)


print(GenBinPerm(input_n))

# Practice Problem 2: N-Queens (n=4)
# Output (one valid solution):
# . Q . .
# . . . Q
# Q . . .
# . . Q .

def GenNQueens(n):
    col_used = [False] * n
    diag1 = [False] * (2 * n - 1)  # for row + col
    diag2 = [False] * (2 * n - 1)  # for row - col + (n-1)
    queens = [-1] * n  # queens[row] = col
    def backtrack(row):
        if row == n:
            # Print the board for this solution
            for r in range(n):
                line = ['.'] * n
                line[queens[r]] = 'Q'
                print(' '.join(line))
            return True  # Found a solution, propagate to stop
        for col in range(n):
            d1 = row + col
            d2 = row - col + n - 1
            if not col_used[col] and not diag1[d1] and not diag2[d2]:
                # Place queen
                queens[row] = col
                col_used[col] = True
                diag1[d1] = True
                diag2[d2] = True
                # Recurse
                if backtrack(row + 1):
                    return True
                # Backtrack
                col_used[col] = False
                diag1[d1] = False
                diag2[d2] = False
                queens[row] = -1
        return False  # No solution from this path
    backtrack(0)

print(GenNQueens(input_n))