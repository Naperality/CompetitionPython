# Write a program that shows this pattern:
# 0 1 2 3 4 5 
# 0 1 2 3 4 
# 0 1 2 3 
# 0 1 2 
# 0 1
# where r = row

def inverted_half(row):
    for i in range(row): # or use for i in range(row,0,-1)
        for j in range(row+1-i): #or use for j in range(0,i+1)
            print(j, end=' ')
        print()
    return ''

print(inverted_half(int(input('Enter Number of Rows: '))))