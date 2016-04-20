# https://www.interviewbit.com/problems/sorted-insert-position/

def search(arr, el):
    low, high = 0, len(arr) - 1
    while low <= high:
        middle = (low + high) / 2
        val = arr[middle]
        if val == el:
            return middle

        if val > el:
            high = middle - 1
        else:
            low = middle + 1

    return low

