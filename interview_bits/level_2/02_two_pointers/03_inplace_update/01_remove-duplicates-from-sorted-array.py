# https://www.interviewbit.com/problems/remove-duplicates-from-sorted-array/

def removeDups(arr):
    p1, p2 = 0, 0
    prev = None
    while p2 < len(arr):
        if prev != arr[p2]:
            arr[p1] = arr[p2]
            prev = arr[p2]
            p1 += 1
            p2 += 1
        else:
            p2 += 1

    return p1
