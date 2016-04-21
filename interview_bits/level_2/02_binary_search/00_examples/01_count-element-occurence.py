# https://www.interviewbit.com/problems/count-element-occurence/

def findCount(arr, b):
    low, high, left = 0, len(arr) - 1, -1
    while low <= high:
        middle = (low + high) / 2
        if arr[middle] == b:
            left = middle
            high = middle - 1
        elif arr[middle] < b:
            low = middle + 1
        else:
            high = middle - 1

    if left == -1:
        return 0

    low, high, right = left, len(arr) - 1, -1
    while low <= high:
        middle = (low + high) / 2
        if arr[middle] == b:
            right = middle
            low = middle + 1
        elif arr[middle] < b:
            low = middle + 1
        else:
            high = middle - 1

    return right - left + 1
