str_ = 'Hello World: 80 o : o o'
print(str_.count('o'))
print(str_.translate(str.maketrans({'o':'','0':''})))
print(str_.partition(':'))





str_1 = 'AAAAAAA'
print([str_1[i:i+3] for i in range(0,len(str_1)-3+1,3) if str_1[i:i+3].startswith('A')])