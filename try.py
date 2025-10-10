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

def remove_vowels(string_):
    return ''.join(letter for letter in string_ if letter.lower() not in 'aeiou')

def remove_vowels_iteration(string_):
    for letter in string_:
        if letter.lower() in 'aeiou':
            string_ = string_.replace(letter, "")
    return string_

print(remove_vowels('Hello World 101'), remove_vowels_iteration('Hello World 101'))

# Write a program that finds the summation of every number from 1 to num (both inclusive). 
# The number will always be a positive integer greater than 0. 
# Your function only needs to return the result, what is shown between 
# parentheses in the example below is how you reach that result and it's not part of it, 
# see the sample tests.

# For example (Input -> Output):

# 2 -> 3 (1 + 2)
# 8 -> 36 (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8)
def summation(num):
    return sum(i for i in range(num+1))
    
print(summation(5))