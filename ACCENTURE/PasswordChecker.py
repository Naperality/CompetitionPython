def CheckPassword(str, n):

    numeric, capital, spaceSlash = False, False, False
    
    if (n < 4) or str[0].isdigit():
        return 0
    
    for char in str:
        if char.isdigit():
            numeric = True
        if char.isupper():
            capital = True
        if char.isspace() or char in '\/':
            spaceSlash = True
        
    return int(numeric and capital and not spaceSlash)
            

input_str = input()
input_len = input()

print(CheckPassword(input_str, int(input_len)))
