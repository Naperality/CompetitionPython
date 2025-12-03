# Write a function that returns a string in which firstname is swapped with last name.

# Example(Input --> Output)

# "john McClane" --> "McClane john"

def swap_name(name_):
    return ' '.join(name_.split()[::-1])

print(swap_name(input('Enter Name: ')))