# Write function RemoveExclamationMarks which 
# removes all exclamation marks from a given string.

def RemoveExclamationMarks(string_):
    return ''.join(l for l in string_ if l != '!')

print(RemoveExclamationMarks(input('Enter String: ')))
