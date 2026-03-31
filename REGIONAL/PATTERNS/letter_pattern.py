# generate a program that shows the pattern CODE
# CCCCC   OOOOO   DDDDD   EEEEE
# C       O   O   D   D   E
# C       O   O   D   D   EEE
# C       O   O   D   D   E
# CCCCC   OOOOO   DDDDD   EEEEE

def letter_pattern(spacing_=3):
    for i in range(5):
        # letter C
        for j in range(5):
            if i==0 or i==4 or j==0:
                print('C', end='')
            else:
                print(' ', end='')
        print(' '*spacing_, end='')

        # letter O
        for j in range(5):
            if i==0 or i==4 or j==0 or j==4:
                print('O', end='')
            else:
                print(' ', end='')
        print(' '*spacing_, end='')

        # letter D
        for j in range(5):
            if i==0 or i==4 or j==0 or j==4:
                print('D', end='')
            else:
                print(' ', end='')
        print(' '*spacing_, end='')

        # letter E
        for j in range(5):
            if i==0 or i==4 or j==0 or (i==2 and j<3):
                print('E', end='')
            else:
                print(' ', end='')
        print(' '*spacing_, end='')

        print()
    return ''

print(letter_pattern())