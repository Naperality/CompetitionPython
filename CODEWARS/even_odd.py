# Create a function that takes an integer as an argument and returns "Even" 
# for even numbers or "Odd" for odd numbers.

def even_or_odd(number):
    return ['Even','Odd'][number%2]

print(even_or_odd(int(input('Enter Number: '))))
