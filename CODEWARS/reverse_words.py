# You need to write a function that reverses the words in a given string. 
# Words are always separated by a single space.

# As the input may have trailing spaces, you will also need to ignore unneccesary whitespace.

# Example (Input --> Output)

# "Hello World" --> "World Hello"
# "Hi There." --> "There. Hi"
# Happy coding!

def reverse(st):
    # return ' '.join(word[::-1] for word in st[::-1].strip().split())
    return ' '.join(st.split()[::-1])

print(reverse(input('Enter Sentence: ')))