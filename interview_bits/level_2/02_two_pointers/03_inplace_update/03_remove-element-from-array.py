arr = [5, 1, 1, 3, 4, 5, 1, 1, 6, 2]

def remove(arr, val):
    p1, p2 = 0, 0
    while p2 < len(arr):
        if arr[p2] != val:
            arr[p1] = arr[p2]
            p1 += 1
            p2 += 1
        else:
            p2 += 1

    return p1

remove(arr, 1)