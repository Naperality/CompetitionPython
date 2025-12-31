# Task
# You will be given an array of numbers. You have to sort the odd numbers in ascending order 
# while leaving the even numbers at their original positions.

# Examples
# [7, 1]  =>  [1, 7]
# [5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]
# [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]

def sort_array(source_array):
    odds = sorted([n for n in source_array if n%2!=0],reverse=True)
    res = []
    for i in range(len(source_array)):
        if source_array[i]%2!=0:
            res.append(odds.pop())
        else:
            res.append(source_array[i])
    return res

def other_solution(source_array):
    odds = sorted([n for n in source_array if n%2!=0],reverse=1)
    return [n if n%2==0 else odds.pop() for n in source_array]

print(sort_array(list(map(int,input('Enter Array: ').split()))))
print(other_solution(list(map(int,input('Enter List of Numbers: ').split()))))