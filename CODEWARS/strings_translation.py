def fake_bin(x):
    # return ''.join('1' if int(digit) < 5 else '0' for digit in x)
    return x.translate(str.maketrans('0123456789', '0000011111'))

print(fake_bin('1123455678'))