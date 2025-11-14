# Complete the solution so that the function will break up 
# camel casing, using a space between words.

# Example
# "camelCasing"  =>  "camel Casing"
# "identifier"   =>  "identifier"
# ""             =>  ""

def break_camel(string_):
    return ''.join(' '+l if l.isupper() else l for l in string_)

print(break_camel(input('Enter Camel Case: ')))