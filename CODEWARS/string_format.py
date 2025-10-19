# You probably know the "like" system from Facebook and other pages. People can 
# "like" blog posts, pictures or other items. 
# We want to create the text that should be displayed next to such an item.

# Implement the function which takes an array containing the names of 
# people that like an item. It must return the display text as shown in the examples:

# []                                -->  "no one likes this"
# ["Peter"]                         -->  "Peter likes this"
# ["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
# ["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
# ["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"
# Note: For 4 or more names, the number in "and 2 others" simply increases.

def like_system(arr):
    return {
        0: 'no one likes this',
        1: '{} likes this',
        2: '{} and {} like this',
        3: '{}, {} and {} like this',
        4: '{}, {} and {n} others like this'
    }[min(4, len(arr))].format(*arr, n = len(arr)-2)

print(like_system(list(map(str, input('Enter number of people: ').split()))))