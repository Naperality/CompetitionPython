# Caesar Cipher (Basic)
# Encrypt a given string using Caesar Cipher with a given shift value.
# Only shift alphabetic characters.
# Wrap around if needed (e.g., z shifted by 1 → a).
# Input: hello 3
# Output: khoor

def caeserCipher(str, shift):
    result = ''
    for letter in str: 
        base = ord('A') if letter.isupper() else ord('a')
        result += chr(((ord(letter) - base + shift) % 26) + base)
    return result

input_str = input('Input: ').split()
print(f'Output: {caeserCipher(input_str[0], int(input_str[1]))}')