# replicate the function string.swapcase
#  it is where every letter in the string is swapped case
# if it is lower then turned into upper
# else vice versa

def swap_case(string):
    return ''.join(l.lower() if l.isupper() else l.upper() for l in string)

print(swap_case(input('Enter String: ')))