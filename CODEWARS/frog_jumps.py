# Help the frog to find a way to freedom
# You have an array of integers and have a frog at the first position

# [Frog, int, int, int, ..., int]

# The integer itself may tell you the length and the direction of the jump

# For instance:
#  2 = jump two indices to the right
# -3 = jump three indices to the left
#  0 = stay at the same position
# Your objective is to find how many jumps are needed to jump out of the array.

# Return -1 if Frog can't jump out of the array

# Example:
# array = [1, 2, 1, 5]; 
# jumps = 3  (1 -> 2 -> 5 -> <jump out>)    
# All tests for this Kata are randomly generated.

def solution(a):
    if not a:
        return -1
    i, count = 0,0
    visited = set()
    while 0 <= i < len(a):
        if i in visited:
            return -1
        visited.add(i)
        i += a[i]
        count += 1
    return count

print(solution(list(map(int,input('Enter Array: ').split()))))