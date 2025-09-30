# # Maze Solver (Backtracking)

# # Given a maze represented as a 2D grid (0 = wall, 1 = path), 
# # find a path from the start (top-left) to the exit (bottom-right).

# Maze Solver (Backtracking)

# Input (0 = wall, 1 = path, n=4):
# 4
# 1 0 0 0
# 1 1 0 1
# 0 1 0 0
# 1 1 1 1
# *Output (path marked with ):
# * 0 0 0
# * * 0 0
# 0 * 0 0
# 0 * * *

# Input:
# n
# n lines with n numbers (0 wall, 1 path)
# Output: prints grid with '*' marking path from (0,0) to (n-1,n-1), or "NO PATH"

def solve_maze(grid):
    n = len(grid)
    path = [[False]*n for _ in range(n)]
    dirs = [(1,0), (0,1), (-1,0), (0,-1)]

    def valid(r,c):
        return 0 <= r < n and 0 <= c < n and grid[r][c] == 1

    found = False
    def backtrack(r,c):
        nonlocal found
        if not valid(r,c) or path[r][c] or found:
            return False
        path[r][c] = True
        if r == n-1 and c == n-1:
            found = True
            return True
        for dr,dc in dirs:
            nr, nc = r+dr, c+dc
            if backtrack(nr,nc):
                return True
        if not found:
            path[r][c] = False
        return found

    if not valid(0,0) or not valid(n-1,n-1):
        return None
    backtrack(0,0)
    if not found:
        return None
    # construct output grid with '*' for path
    out = []
    for r in range(n):
        row = []
        for c in range(n):
            if path[r][c]:
                row.append("*")
            else:
                row.append(str(grid[r][c]))
        out.append(" ".join(row))
    return out

n = int(input().strip())
grid = [list(map(int, input().split())) for _ in range(n)]
ans = solve_maze(grid)
if ans is None:
    print("NO PATH")
else:
    for line in ans:
        print(line)
