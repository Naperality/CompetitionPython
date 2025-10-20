def high_low(string_):
    return string_[(len(string_)-1)//2:(len(string_)//2)+1]

print(high_low(input('Enter string: ')))