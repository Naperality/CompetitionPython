# Problem
# Convert a decimal number value into base b
# where 2 ≤ b ≤ 36.
# Digits:
# 0–9 → 0–9
# 10–35 → A–Z
# Example
# Input:
# b = 16
# value = 255
# Output:
# FF

def n_base_convert(base,num):
    res = ''
    while num != 0:
        if num%base <= 9:
            res += str(num%base)
        else:
            res += chr((num%base) - 10 + ord('A'))
        num//=base
    return res[::-1]

print(n_base_convert(int(input('Enter Base (2-36): ')),int(input('Enter Number: '))))