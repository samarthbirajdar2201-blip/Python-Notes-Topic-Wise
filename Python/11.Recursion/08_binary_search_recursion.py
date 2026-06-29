# ------------------------------
# 8. Binary Search
# ------------------------------

def binary_search(arr, left, right, target):

    if left > right:
        return -1

    mid = (left + right) // 2

    if arr[mid] == target:
        return mid

    elif arr[mid] > target:
        return binary_search(arr, left, mid - 1, target)

    else:
        return binary_search(arr, mid + 1, right, target)

arr = [10, 20, 30, 40, 50]

print(binary_search(arr, 0, len(arr)-1, 30))