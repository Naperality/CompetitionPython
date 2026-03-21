# Write a program with this pattern
# 1  
# 2 2  
# 3 3 3  
# 4 4 4 4  
# 5 5 5 5 5
# where r = rows

def right_tri(row):
    for i in range(row+1):
        for j in range(i):
            print(i, end='')
        print()
    return ''

print(right_tri(int(input('Enter Number of Rows: '))))