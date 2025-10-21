# Build Tower
# Build a pyramid-shaped tower, as an array/list of strings, 
# given a positive integer number of floors. A tower block is represented with "*" character.

# For example, a tower with 3 floors looks like this:

# [
#   "  *  ",
#   " *** ", 
#   "*****"
# ]
# And a tower with 6 floors looks like this:

# [
#   "     *     ", 
#   "    ***    ", 
#   "   *****   ", 
#   "  *******  ", 
#   " ********* ", 
#   "***********"
# ]
# Go challenge Build Tower Advanced once you have finished this :)

def build_tower(num):
    if num <= 0:
        return []
    
    tower, max_width = [], 2 * num - 1
    for i in range(1, num+1):
        asterisks = '*' * (2 * i -1)
        tower.append(asterisks.center(max_width, ' '))
    return ''.join(line+'\n' for line in tower)

print(build_tower(int(input('Enter height of tower: '))))
