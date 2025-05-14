#binary search and linear search

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

arr = [7, 9, 12, 21, 27, 35, 47, 53, 5, 54]
target = 35

print("Array:", arr)
print("Target:", target)
print("Linear Search Result:", linear_search(arr, target))
print("Binary Search Result:", binary_search(arr, target))