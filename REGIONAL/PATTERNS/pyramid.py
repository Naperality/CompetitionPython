#     * 
#    * *
#   * * *
#  * * * *
# * * * * *

def pyramid_1(row):
    for i in range(1,row+1):
        print(" "*(row-i), end='')
        print('* '*i)
    return ''

# * * * * * 
#  * * * *
#   * * *
#    * *
#     *

def inverted_pyramid(row):
    for i in range(row,0,-1):
        print(' '*(row-i)+'* '*i)
    return ''

def pascal_pyramid(row):
    line = [1]
    for i in range(1,row+1):
        print(' '*(row-i)+(' '.join(map(str,line))))
        line = [1]+[line[j]+line[j+1] for j in range(len(line)-1)]+[1]
    return ''

print(pyramid_1(int(input('Enter Number of Rows: '))))
print(inverted_pyramid(int(input('Enter Number of Rows: '))))
print(pascal_pyramid(int(input('Enter Number of Rows: '))))