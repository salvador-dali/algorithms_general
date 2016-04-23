# https://www.hackerrank.com/challenges/quicksort2
def quicksort(arr):
    if len(arr) <= 1:
        return arr

    small, big, pivots, pivot = [], [], [], arr[0]
    for i in arr:
        if i > pivot:
            big.append(i)
        elif i < pivot:
            small.append(i)
        else:
            pivots.append(i)

    return quicksort(small) + pivots + quicksort(big)

input()
print ' '.join(map(str, quicksort(map(int, raw_input().split()))))