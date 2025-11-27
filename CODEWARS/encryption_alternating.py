# Implement a pseudo-encryption algorithm which given a string S and an integer 
# N concatenates all the odd-indexed characters of S with all the even-indexed 
# characters of S, this process should be repeated N times.

# Examples:

# encrypt("012345", 1)  =>  "135024"
# encrypt("012345", 2)  =>  "135024"  ->  "304152"
# encrypt("012345", 3)  =>  "135024"  ->  "304152"  ->  "012345"

# encrypt("01234", 1)  =>  "13024"
# encrypt("01234", 2)  =>  "13024"  ->  "32104"
# encrypt("01234", 3)  =>  "13024"  ->  "32104"  ->  "20314"
# Together with the encryption function, you should also implement a decryption 
# function which reverses the process.

# If the string S is an empty value or the integer N is not positive, return 
# the first argument without changes.

# This kata is part of the Simple Encryption Series:

# Simple Encryption #1 - Alternating Split
# Simple Encryption #2 - Index-Difference
# Simple Encryption #3 - Turn The Bits Around
# Simple Encryption #4 - Qwerty
# Have fun coding it and please don't forget to vote and rank this kata! :-)

def decrypt(encrypted_text, n):
    text = encrypted_text
    length = len(text)
    for _ in range(n):
        mid = length // 2
        odd_chars = text[:mid]
        even_chars = text[mid:]
        
        decrypted_list = []
        max_len = max(len(even_chars), len(odd_chars))
        
        for i in range(max_len):
            if i < len(even_chars):
                decrypted_list.append(even_chars[i])
            if i < len(odd_chars):
                decrypted_list.append(odd_chars[i])
                
        text = "".join(decrypted_list)
        
    return text

def encrypt(text, n):
    return text if n<=0 else encrypt(text[1::2]+text[::2], n-1)

print(encrypt(input('Enter Numbers: '), int(input('Enter Number of times: '))))
print(decrypt(input('Enter Numbers: '), int(input('Enter Number of times: '))))