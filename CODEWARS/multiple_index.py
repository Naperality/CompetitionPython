# Return a new array consisting of elements which are multiple of 
# their own index in input array (length > 1).

# Some cases:
# [22, -6, 32, 82, 9, 25] =>  [-6, 32, 25]

# [68, -1, 1, -7, 10, 10] => [-1, 10]


def multiple_of_index(arr):
    res =[ arr[0]]if arr[0]==0 else []
    return res+[arr[i] for i in range(1,len(arr)) if abs(arr[i])%i==0]

print(multiple_of_index(list(map(int,input('Enter List of Numbers: ')))))