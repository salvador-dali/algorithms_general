# https://www.interviewbit.com/problems/intersection-of-sorted-arrays/
def intersection(arr1, arr2):
    p1, p2, res = 0, 0, []
    while p1 < len(arr1) and p2 < len(arr2):
        if arr1[p1] < arr2[p2]:
            p1 += 1
        elif arr1[p1] > arr2[p2]:
            p2 += 1
        else:
            res.append(arr1[p1])
            p1 += 1
            p2 += 1
    return res
