# Your job is to write a function which increments a string, to create a new string.

# If the string already ends with a number, the number should be incremented by 1.
# If the string does not end with a number. the number 1 should be appended to the new string.
# Examples:

# foo -> foo1

# foobar23 -> foobar24

# foo0042 -> foo0043

# foo9 -> foo10

# foo099 -> foo100

# Attention: If the number has leading zeros the amount of digits should be considered.
def increment_string(s):
    i = len(s) - 1
    while i >= 0 and s[i].isdigit():
        i -= 1
    num_start_index = i + 1
    text_part = s[:num_start_index]
    num_str = s[num_start_index:]
    
    if not num_str:
        return s + '1'
    else:
        num_len = len(num_str)
        incremented_num = int(num_str) + 1
        new_num_str = f'{incremented_num:0{num_len}d}'
        return text_part + new_num_str

def increment_string_v2(string_):
    head_str = string_.rstrip('0123456789')
    tail_str = string_[len(head_str):]
    if tail_str == '': return head_str+'1'
    return head_str+str(int(tail_str)+1).zfill(len(tail_str))


print(increment_string(input('Enter String: ')))
print(increment_string_v2(input('Enter Word with Number or None: ')))