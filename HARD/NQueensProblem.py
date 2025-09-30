# # N-Queens Problem

# # Write a program that places N queens on an N x N chessboard 
# # such that no two queens attack each other. Print one valid board configuration.

# N-Queens Problem (N = 4)

# Input:
# 4
# Output (one possible solution, Q = queen, . = empty):

# . Q . .
# . . . Q
# Q . . .
# . . Q .

# Input: single integer N
# Output: one board configuration with 'Q' and '.' (or "NO" if none)

def solve_n_queens(N):
    cols = set()
    diag1 = set()  # r + c
    diag2 = set()  # r - c
    board = [["." for _ in range(N)] for _ in range(N)]
    solution = []

    def backtrack(r):
        if r == N:
            # capture solution
            sol = [" ".join(row) for row in board]
            solution.extend(sol)
            return True
        for c in range(N):
            if c in cols or (r + c) in diag1 or (r - c) in diag2:
                continue
            cols.add(c); diag1.add(r + c); diag2.add(r - c)
            board[r][c] = "Q"
            if backtrack(r + 1):
                return True
            # undo
            cols.remove(c); diag1.remove(r + c); diag2.remove(r - c)
            board[r][c] = "."
        return False

    if backtrack(0):
        return solution
    else:
        return None

if __name__ == "__main__":
    N = int(input().strip())
    sol = solve_n_queens(N)
    if sol is None:
        print("NO")
    else:
        for row in sol:
            print(row.replace(" ", ""))
