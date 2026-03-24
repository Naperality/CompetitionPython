# Write a program that shows this pattern:
# 1 1 1 1 1 
# 2 2 2 2 
# 3 3 3 
# 4 4 
# 5
# where r = row

def inverted_right(row):
    for i in range(row+1): # can use for i in range(row,0,-1)
        for j in range(row-i): # can use for j in range(1,i+1)
            print(i+1, end=' ')
        print()
    return ''

def inverted_right_num_col(row):
    for i in range(row+1):
        for j in range(row-i):
            print(j+1,end=' ')
        print()
    return ''

def inverted_right_single_num(row):
    for i in range(row+1):
        for j in range(row-i):
            print('5', end=' ')
        print()
    return ''

def inverted_right_tri_pattern1(row):
    for i in range(row+1):
        for j in range(row-i,0,-1):
            print(j, end=' ')
        print()
    return ''

print(inverted_right(int(input('Enter Number of Row: '))))
print(inverted_right_num_col(int(input('Enter Number of Row: '))))
print(inverted_right_single_num(int(input('Enter Number of Row: '))))
print(inverted_right_tri_pattern1(int(input('Enter Number of Row: '))))