# The number 
# 89
# 89 is the first integer with more than one digit that fulfills the property partially 
# introduced in the title of this kata. What's the use of saying "Eureka"? Because this sum 
# gives the same number: 
# 89 = 8 + 81 = 89

# The next number in having this property is 
# 135
# 135:
# See this property again: 
# 135 = 1 + 9 + 125 = 135
 
# Task
# We need a function to collect these numbers, that may receive two integers 
# [a,b] (inclusive) and outputs a list of the sorted numbers in the range 
# that fulfills the property described above.

# Examples
# Let's see some cases (input -> output):

# 1, 10  --> [1, 2, 3, 4, 5, 6, 7, 8, 9]
# 1, 100 --> [1, 2, 3, 4, 5, 6, 7, 8, 9, 89]
# If there are no numbers of this kind in the range 
# [a,b] the function should output an empty list.

# 90, 100 --> []
# Enjoy it!!

def sum_dig_pow(a, b): # range(a, b + 1) will be studied by the function
    # your code here
    return []

print(sum_dig_pow(int(input('Enter Number A: ')), int(input('Enter Number B: '))))