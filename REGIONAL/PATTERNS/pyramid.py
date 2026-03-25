#    1 
#   3 2 
#  6 5 4 
# 10 9 8 7

def pyramid_1(row):
    for i in range(1,row+1):
        print(" "*(row-i), end='')
        print('* '*i)
    return ''

print(pyramid_1(int(input('Enter Number of Rows: '))))