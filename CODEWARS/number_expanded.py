# Write Number in Expanded Form
# You will be given a number and you will need to return it as a 
# string in Expanded Form. For example:

#    12 --> "10 + 2"
#    45 --> "40 + 5"
# 70304 --> "70000 + 300 + 4"
# NOTE: All numbers will be whole numbers greater than 0.

# If you liked this kata, check out part 2!!

def expanded_form(num):
    str_n = str(num)
    nums = [d+('0'*(len(str_n)-(i+1))) for i, d in enumerate(str_n)]
    return ' + '.join(digit for digit in nums if digit[0] != '0')

print(expanded_form(int(input('Enter Number: '))))