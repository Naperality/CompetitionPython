# Jamie is a programmer, and James' girlfriend. She likes diamonds, and wants a 
# diamond string from James. Since James doesn't know how to make this happen, he needs your help.

# Task
# You need to return a string that looks like a diamond shape when printed on the 
# screen, using asterisk (*) characters. Trailing spaces should be removed, and 
# every line must be terminated with a newline character (\n).

# Return null/nil/None/... if the input is an even number or negative, as it is 
# not possible to print a diamond of even or negative size.

# Examples
# A size 3 diamond:

#  *
# ***
#  *
# ...which would appear as a string of " *\n***\n *\n"

# A size 5 diamond:

#   *
#  ***
# *****
#  ***
#   *
# ...that is:

# "  *\n ***\n*****\n ***\n  *\n"

def diamond(n):
    if not n%2 or n<0:
        return None
    return '\n'.join(' '*((n - (n-2*abs((n//2) - i)))//2)+'*'*(n-2*abs((n//2) - i))  for i in range(n))

def iterative(n):
    if not n%2 or n<0:
        return None
    res  = ''
    for i in range(n):
        s,d = 0,0
        if i < n/2:
            d = i*2+1
            s = (n-d)//2
        else:
            s = i - n//2
            d = n - 2*s
        res += ' '*s + '*'*d + '\n'
    return res

print(diamond(int(input('Enter Size of Diamond: '))))
print(iterative(int(input('Enter Size: '))))