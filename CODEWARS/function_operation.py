# This time we want to write calculations using functions and get the results. 
# Let's have a look at some examples:

# seven(times(five()))    #  must return 35
# four(plus(nine()))      #  must return 13
# eight(minus(three()))   #  must return 5
# six(divided_by(two()))  #  must return 3
# Requirements:

# There must be a function for each number from 0 ("zero") to 9 ("nine")
# There must be a function for each of the following mathematical operations:
#  plus, minus, times, divided_by
# Each calculation consist of exactly one operation and two numbers
# The most outer function represents the left operand, the most inner function 
# represents the right operand
# Division should be integer division. For example, this should return 2, not 2.666666...:
# eight(divided_by(three()))

def apply_operation(number, operation_tuple):
    if operation_tuple:
        operator, right_operand = operation_tuple
        return operator(number, right_operand)
    return number

def zero(operation=None): return apply_operation(0, operation)
def one(operation=None): return apply_operation(1, operation)
def two(operation=None): return apply_operation(2, operation)
def three(operation=None): return apply_operation(3, operation)
def four(operation=None): return apply_operation(4, operation)
def five(operation=None): return apply_operation(5, operation)
def six(operation=None): return apply_operation(6, operation)
def seven(operation=None): return apply_operation(7, operation)
def eight(operation=None): return apply_operation(8, operation)
def nine(operation=None): return apply_operation(9, operation)

def plus(right_operand):
    return (lambda x, y: x + y, right_operand)

def minus(right_operand):
    return (lambda x, y: x - y, right_operand)

def times(right_operand):
    return (lambda x, y: x * y, right_operand)

def divided_by(right_operand):
    return (lambda x, y: x // y, right_operand)

# or 

def identity(a): return a

def zero(f=identity): return f(0)
def one(f=identity): return f(1)
def two(f=identity): return f(2)
def three(f=identity): return f(3)
def four(f=identity): return f(4)
def five(f=identity): return f(5)
def six(f=identity): return f(6)
def seven(f=identity): return f(7)
def eight(f=identity): return f(8)
def nine(f=identity): return f(9)

def plus(b): return lambda a: a + b
def minus(b): return lambda a: a - b
def times(b): return lambda a: a * b
def divided_by(b): return lambda a: a // b