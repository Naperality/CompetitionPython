# Write a program with this pattern
# 1  
# 2 2  
# 3 3 3  
# 4 4 4 4  
# 5 5 5 5 5
# where r = rows

def right_tri_num_rows(row):
    for i in range(row+1):
        for j in range(i):
            print(i, end=' ')
        print()
    return ''

def right_tri_num_col(row):
    for i in range(row+1):
        for j in range(i):
            print(j+1, end=' ')
        print()
    return ''

print(right_tri_num_rows(int(input('Enter Number of Rows: '))))
print(right_tri_num_col(int(input('Enter Number of Rows: '))))