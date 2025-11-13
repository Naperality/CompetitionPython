# ROT13 is a simple letter substitution cipher that replaces a letter with the 
# letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.

# Create a function that takes a string and returns the string ciphered with Rot13. 
# If there are numbers or special characters included in the string, 
# they should be returned as they are. Only letters from the latin/english 
# alphabet should be shifted, like in the original Rot13 "implementation".

# Please note that using encode is considered cheating.

def rot13(message):
    res = ''
    for l in message:
        if l.isalpha():
            base = ord('A') if l.isupper() else ord('a')
            res += chr((((ord(l)-base)+13)%26)+base)
        else:
            res += l
    return res

def one_liner_style(message):
    return ''.join(chr((ord('A') if l.isupper() else ord('a')) + ((ord(l)-(ord('A') if l.isupper() else ord('a')) + 13)%26) ) if l.isalpha() else l for l in message)

print(one_liner_style(input('Enter String to Encode: ')))
print(rot13(input('Enter String: ')))