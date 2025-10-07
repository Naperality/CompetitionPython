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
    