# Two Sum

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

# Rock Paper Scissor
import random
def AnswerChecker(answer):
    choices = ['rock', 'paper', 'scissors']
    comp_answer = random.choice(choices)

    winner = {('rock','scissors'), ('paper', 'rock'), ('scissors', 'paper')}

    if (answer, comp_answer) in winner:
        return f'Player wins, {answer} > {comp_answer}'
    elif answer == comp_answer:
        return f'It\'s a Draw, {answer} = {comp_answer}'
    else:
        return f'Computer wins, {answer} < {comp_answer}'

while True:
    input_answer = input("Enter Choice (Rock, Paper, or Scissors): ")
    if input_answer.strip().lower() in ['rock', 'paper', 'scissors', 'exit']:
        if input_answer.strip().lower() == 'exit':
            print('Thank you for playing!')
            break
        print(AnswerChecker(input_answer.strip().lower()))
    else:
        print('Your Choice is not Correct, Try Again!')


# Write a function that accepts an integer argument n and 
# generates an array containing the pairs of integers [a, b] that satisfy the condition

# 0 <= a <= b <= n
# The pairs should be sorted by increasing values of a, then by increasing values of b.

# For example,
# for input: 2
# it should return: [  [0, 0], [0, 1], [0, 2],  [1, 1], [1, 2],  [2, 2]  ]

def generate_pairs(n):
    return [[x,y] for x in range(n+1) for y in range(x, n+1)]

print(generate_pairs(int(input("Number: "))))