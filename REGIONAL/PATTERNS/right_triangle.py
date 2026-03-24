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

def right_tri_odd(row):
    for i in range(row+1):
        for j in range(i):
            print(i*2-1, end=' ')
        print()
    return ''

def right_tri_row_index(row):
    for i in range(row+1):
        for j in range(i,0,-1):
            print(j, end=' ')
        print()
    return ''

def right_tri_pattern1(row):
    temp = 0
    for i in range(row+1):
        temp+=i
        for j in range(i):
            print(temp-j,end=' ')
        print()
    return ''

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

def pascal_right_tri(row):
    line = [1]
    for _ in range(row):
        print(' '.join(map(str,line)))
        line = [1] + [line[j] + line[j+1] for j in range(len(line)-1)] + [1]
    return ''

print(right_tri_num_rows(int(input('Enter Number of Rows: '))))
print(right_tri_num_col(int(input('Enter Number of Rows: '))))
print(right_tri_odd(int(input('Enter Number of Row: '))))
print(right_tri_row_index(int(input('Enter Number of Row: '))))
print(right_tri_pattern1(int(input('Enter Number of Row: '))))
print(right_angled_tri(int(input('Enter Number of Row: '))))
print(pascal_right_tri(int(input('Enter Number of Row: '))))