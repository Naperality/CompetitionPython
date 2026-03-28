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


# 1 2 3 4 5 
# 1 2 3 4
# 1 2 3
# 1 2
# 1

def inverted_right_num_col(row):
    for i in range(row+1):
        for j in range(row-i):
            print(j+1,end=' ')
        print()
    return ''

# 5 5 5 5 5 
# 5 5 5 5
# 5 5 5
# 5 5
# 5

def inverted_right_single_num(row):
    for i in range(row+1):
        for j in range(row-i):
            print('5', end=' ')
        print()
    return ''

# 5 4 3 2 1 
# 4 3 2 1
# 3 2 1
# 2 1
# 1

def inverted_right_tri_pattern1(row):
    for i in range(row+1):
        for j in range(row-i,0,-1):
            print(j, end=' ')
        print()
    return ''

# 1 2 3 4 
# 5 6 7
# 8 9
# 10

def inverted_floyd(row):
    x = 0
    for i in range(1,row+1):
        for j in range(row-i):
            x+=1
            print(x,end=' ')
        print()
    return ''

print(inverted_right(int(input('Enter Number of Row: '))))
print(inverted_right_num_col(int(input('Enter Number of Row: '))))
print(inverted_right_single_num(int(input('Enter Number of Row: '))))
print(inverted_right_tri_pattern1(int(input('Enter Number of Row: '))))
print(inverted_floyd(int(input('Enter Number of Rows: '))))