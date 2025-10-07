def twoSum(arr, target):
    seen = {}

    for index, num in enumerate(arr):
        complement = target - num

        if complement in seen:
            return (index, seen[complement])
        
        seen[num] = index
    return -1

input_arr = list(map(int, input("Array: ").split()))
target = int(input("Target: "))

print(twoSum(input_arr, target))

# Caeser Code

def caeserCipher(word, shift):
    result = ''
    for letter in word:
        base = ord('A') if letter.isupper() else ord('a')
        result += chr((ord(letter)-base+shift) % 26 + base)
    return result

input_word = input("Enter Word: ")
input_shift = int(input("Enter Shift: "))
print(caeserCipher(input_word, input_shift))