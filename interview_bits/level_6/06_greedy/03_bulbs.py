# https://www.interviewbit.com/problems/bulbs/
def bulb(arr):
    if not len(arr):
        return 0

    prev, arr2 = -1, []
    for i in arr:
        if i != prev:
            arr2.append(i)
            prev = i

    if arr2[0] == 1:
        return len(arr2) - 1
    return len(arr2)


print bulb([1, 1, 1, 0, 1, 1])