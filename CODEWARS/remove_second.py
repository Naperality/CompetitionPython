# Take an array and remove every second element from the array. 
# Always keep the first element and start removing with the next element.

# Example:
# ["Keep", "Remove", "Keep", "Remove", "Keep", ...] --> ["Keep", "Keep", "Keep", ...]

# None of the arrays will be empty, so you don't have to worry about that!

def remove_second(list_):
    # return list_[::2]
    return [j for i, j in enumerate(list_) if not i%2]

print(remove_second(list(map(str, input('Enter List: ').split()))))