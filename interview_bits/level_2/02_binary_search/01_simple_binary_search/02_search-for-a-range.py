# https://www.interviewbit.com/problems/search-for-a-range/
def search(arr, el):
    low, high, first = 0, len(arr) - 1, -1
    while low <= high:
        middle = (low + high) / 2
        val = arr[middle]
        if val == el:
            high = middle - 1
            first = middle
        elif val > el:
            high = middle - 1
        else:
            low = middle + 1

    if first == -1:
        return [-1, -1]

    low, high, second = first, len(arr) - 1, -1
    while low <= high:
        middle = (low + high) / 2
        val = arr[middle]
        if val == el:
            low = middle + 1
            second = middle
        elif val > el:
            high = middle - 1
        else:
            low = middle + 1

    return [first, second]
