# https://www.interviewbit.com/problems/remove-duplicates-from-sorted-array-ii/
def removeDup2(arr):
    prev, p1, p2, num = None, 0, 0, 0
    while p2 < len(arr):
        if arr[p2] != prev:
            prev = arr[p2]
            arr[p1] = arr[p2]
            p1 += 1
            p2 += 1
            num = 0
        elif num == 0:
            arr[p1] = arr[p2]
            p1 += 1
            p2 += 1
            num += 1
        else:
            p2 += 1
            num += 1

    return p1, arr[:p1]