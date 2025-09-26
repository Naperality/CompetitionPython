# Problem Statement 

# You are required to input the size of the matrix 
# then the elements of matrix, then you have to divide the main matrix in two sub matrices (even and odd) 
# in such a way that element at 0 index will be considered as even and element 
# at 1st index will be considered as odd and so on. then you have sort the even and odd 
# matrices in ascending order then print the sum of second largest number from both the matrices

# Example

# enter the size of array : 5
# enter element at 0 index : 3
# enter element at 1 index : 4
# enter element at 2 index : 1
# enter element at 3 index : 7
# enter element at 4 index : 9
# Sorted even array : 1 3 9
# Sorted odd array : 4 7

# 7
arr = []
input_size = int(input("Enter the size of the array : "))

for i in range(input_size):
    arr.append(input(f'enter element at {i} index : '))

sorted_even = sorted([num for index, num in enumerate(arr) if index % 2 == 0])
sorted_odd = sorted([num for index, num in enumerate(arr) if index % 2 != 0])

print(f'Sorted even array:', ' '.join(sorted_even))
print(f'Sorted odd array :', ' '.join(sorted_odd))
print(int(sorted_even[-2]) + int(sorted_odd[-2]))