def twoSum(arr, target):
    seen = {}

    for index, num in enumerate(arr):
        complement = target - num

        if complement in seen:
            return (index, seen[complement])
        
        seen[num] = index
    return -1

input_arr = list(map(int, input("Array: ").split()))
target = int(input("Target: "))

print(twoSum(input_arr, target))