# Given a string of words, you need to find the highest scoring word.

# Each letter of a word scores points according to its position in the alphabet: 
# a = 1, b = 2, c = 3 etc.

# For example, the score of abad is 8 (1 + 2 + 1 + 4).

# You need to return the highest scoring word as a string.

# If two words score the same, return the word that appears earliest in the original string.

# All letters will be lowercase and all inputs will be valid.

def highScore(x):
    res = {}
    for word in x.split():
        val = sum(((ord(c)-97)%26)+1 for c in word)
        if val not in res:
            res[val] = word
    return res[max(res.keys())]

def fast_sol(x):
    return max(x.split(), key=lambda word: sum(ord(ch) - ord('a')+1 for ch in word))

print(highScore(input('Enter String of Words: ')))
print(fast_sol(input('Enter String: ')))
print(sorted(list(map(int, input('Nums: ').split())), key = lambda n: abs(n-6)))