# Write a python program that takes a list of integer input
# and removes the consecutive duplicates leaving only one instance

def remove_consec_dup(list_):
    return [list_[i] for i in range(len(list_)) if i == 0 or list_[i]!=list_[i-1]]

print(remove_consec_dup(list(map(int,input('Enter list of integers: ').split()))))