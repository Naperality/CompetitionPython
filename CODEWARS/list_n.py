# Create a function that accepts a list/array and a number n, and returns a list/array 
# of the first n elements from the list/array.

def take(arr,n):
    # return [arr[i] for i in range(min(n,len(arr)))]
    return arr[:n]

print(
    take(list(map(int,input('Enter Array: ').split())),
    int(input('Enter Number: ')))
)