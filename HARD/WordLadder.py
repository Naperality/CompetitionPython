# # Word Ladder (Shortest Transformation)
# # Given two words (start and end) and a dictionary of words, 
# # find the minimum number of steps to transform the start into the end.
# # You can only change one letter at a time.
# # Each transformed word must exist in the dictionary.
# Word Ladder

# Input:
# begin hit
# end cog
# dictionary: [hot, dot, dog, lot, log, cog]
# Output:
# 5
# (Explanation: hit → hot → dot → dog → cog, 5 words in ladder)

# Input style used here:
# first line: start end   (e.g., "hit cog")
# second line: integer m (number of dict words)
# next m lines: each a dictionary word
# Output: integer length of shortest ladder including start and end, or 0 if no path.

from collections import deque

def ladder_length(start, end, word_set):
    if end not in word_set:
        return 0
    L = len(start)
    queue = deque([(start, 1)])
    visited = {start}
    while queue:
        word, steps = queue.popleft()
        if word == end:
            return steps
        # try all single-letter transformations
        for i in range(L):
            for ch in "abcdefghijklmnopqrstuvwxyz":
                if ch == word[i]:
                    continue
                nxt = word[:i] + ch + word[i+1:]
                if nxt in word_set and nxt not in visited:
                    visited.add(nxt)
                    queue.append((nxt, steps + 1))
    return 0

start_end = input().split()
start, end = start_end[0], start_end[1]
m = int(input().strip())
word_set = set(input().strip() for _ in range(m))
print(ladder_length(start, end, word_set))
