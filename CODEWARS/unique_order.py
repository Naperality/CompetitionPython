# Implement the function unique_in_order which takes as argument a sequence and 
# returns a list of items without any elements with the same value next to 
# each other and preserving the original order of elements.

# For example:

# unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
# unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
# unique_in_order([1, 2, 2, 3, 3])   == [1, 2, 3]
# unique_in_order((1, 2, 2, 3, 3))   == [1, 2, 3]

def unique_in_order(sequence):
    if not sequence:
        return []
    res = []
    for i in range(len(sequence)):
        if i+1!=len(sequence) and sequence[i]!=sequence[i+1]:
            res.append(sequence[i])
    return res+[sequence[-1]]

def other_solution(sequence):
    res = []
    for n in sequence:
        if len(res)==0 or n!=res[-1]:
            res.append(n)
    return res

print(unique_in_order(list(map(str,input('Enter List of Letters: ').split()))))
print(other_solution(list(map(str,input('Enter Array: ').split()))))