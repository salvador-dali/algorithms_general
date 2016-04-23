# https://www.hackerrank.com/challenges/quicksort4/

# count the number of swaps in quicksort
def quick_sort(arr, left=None, right=None):
    if left is None:
        left = 0
    if right is None:
        right = len(arr) - 1

    if left >= right:
        return 0

    lPoint = rPoint = left
    pivot, count = arr[right], 1

    while rPoint < right:
        if arr[rPoint] < pivot:
            arr[rPoint], arr[lPoint] = arr[lPoint], arr[rPoint]
            lPoint += 1
            count += 1

        rPoint += 1

    arr[lPoint], arr[right] = arr[right], arr[lPoint]

    count += quick_sort(arr, left, lPoint - 1)
    count += quick_sort(arr, lPoint + 1, right)
    return count

# number of swaps in insertion sort
def insert_sort(arr):
    l, count = len(arr), 0
    for i in xrange(l):
        for j in xrange(i + 1, l):
            if arr[i] > arr[j]:
                count += 1
    return count

input()
arr = list(map(int, raw_input().split()))
print insert_sort(arr) - quick_sort(arr)