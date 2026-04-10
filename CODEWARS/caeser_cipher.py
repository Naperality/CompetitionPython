# Make a program Caeser's Cipher
# where it accepts an string and a shift key for the letter to shift
# Make also a deciphering logic for it too in one function

def caeser_cipher(string_, shift_, mode_):
    if mode_==1: shift_*=-1
    return ''.join(chr((ord(l)-(b:=ord('a') if l.islower() else ord('A'))+shift_)%26+b) if l.isalpha() else l for l in string_)

print(caeser_cipher(input('Enter a string: '), int(input('Enter a shift number: ')), int(input('Enter mode (0-cipher,1-decipher): '))))