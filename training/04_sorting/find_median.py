# https://www.hackerrank.com/challenges/find-median/
import random

def partition(arr, left, right, index):
    pivotValue = arr[index]
    arr[index], arr[right] = arr[right], arr[index]  # Move pivot to end
    storeIndex = left
    for i in range(left, right):
        if arr[i] < pivotValue:
            arr[storeIndex], arr[i] = arr[i], arr[storeIndex]
            storeIndex += 1
    arr[right], arr[storeIndex] = arr[storeIndex], arr[right]  # Move pivot to its final place
    return storeIndex

def _select(vector, left, right, k):
    while True:
        pivotIndex = random.randint(left, right)     # select pivotIndex between left and right
        pivotNewIndex = partition(vector, left, right, pivotIndex)
        pivotDist = pivotNewIndex - left
        if pivotDist == k:
            return vector[pivotNewIndex]
        elif k < pivotDist:
            right = pivotNewIndex - 1
        else:
            k -= pivotDist + 1
            left = pivotNewIndex + 1

def select(vector, k, left=None, right=None):
    if left is None:
        left = 0
    lv1 = len(vector) - 1
    if right is None:
        right = lv1
    return _select(vector, left, right, k)

def median(arr):
    l = len(arr)
    if l % 2:
        return select(arr, l / 2)

    return (select(arr, l / 2) + select(arr, l/2 + 1)) / 2.0

raw_input()
print median(map(int, raw_input().split()))