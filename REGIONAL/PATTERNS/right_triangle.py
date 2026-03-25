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

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

def right_tri_num_col(row):
    for i in range(row+1):
        for j in range(i):
            print(j+1, end=' ')
        print()
    return ''

# 1
# 3 3
# 5 5 5
# 7 7 7 7
# 9 9 9 9 9

def right_tri_odd(row):
    for i in range(row+1):
        for j in range(i):
            print(i*2-1, end=' ')
        print()
    return ''

# 1
# 2 1
# 3 2 1
# 4 3 2 1
# 5 4 3 2 1

def right_tri_row_index(row):
    for i in range(row+1):
        for j in range(i,0,-1):
            print(j, end=' ')
        print()
    return ''

# 1
# 3 2
# 6 5 4
# 10 9 8 7
# 15 14 13 12 11

def right_tri_pattern1(row):
    temp = 0
    for i in range(row+1):
        temp+=i
        for j in range(i):
            print(temp-j,end=' ')
        print()
    return ''


#         1
#       1 2
#     1 2 3
#   1 2 3 4
# 1 2 3 4 5

def right_angled_tri(row):
    for i in range(row+1):
        x = 1
        for j in range(row,0,-1):
            if j>i:
                print(' ',end=' ')
            else:
                print(x, end=' ')
                x+=1
        print()
    return ''


# 1 
# 1 1 
# 1 2 1 
# 1 3 3 1 
# 1 4 6 4 1 
# 1 5 10 10 5 1 
# 1 6 15 20 15 6 1

def pascal_right_tri(row):
    line = [1]
    for _ in range(row):
        print(' '.join(map(str,line)))
        line = [1] + [line[j] + line[j+1] for j in range(len(line)-1)] + [1]
    return ''

# 1  
# 2  4  
# 3  6  9  
# 4  8  12  16  
# 5  10  15  20  25  
# 6  12  18  24  30  36  
# 7  14  21  28  35  42  49  
# 8  16  24  32  40  48  56  64  

def multi_right_tri(row):
    for i in range(1,row+1):
        for j in range(1,i+1):
            print(j*i, end=' ')
        print()
    return ''

print(right_tri_num_rows(int(input('Enter Number of Rows: '))))
print(right_tri_num_col(int(input('Enter Number of Rows: '))))
print(right_tri_odd(int(input('Enter Number of Row: '))))
print(right_tri_row_index(int(input('Enter Number of Row: '))))
print(right_tri_pattern1(int(input('Enter Number of Row: '))))
print(right_angled_tri(int(input('Enter Number of Row: '))))
print(pascal_right_tri(int(input('Enter Number of Row: '))))
print(multi_right_tri(int(input('Enter Number of Rows: '))))