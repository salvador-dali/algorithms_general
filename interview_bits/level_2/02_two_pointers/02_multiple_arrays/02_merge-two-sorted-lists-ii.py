# https://www.interviewbit.com/problems/merge-two-sorted-lists-ii/
def mergeSorted(arr1, arr2):
    res, p1, p2 = [], 0, 0

    while p1 < len(arr1) and p2 < len(arr2):
        if arr1[p1] < arr2[p2]:
            res.append(arr1[p1])
            p1 += 1
        else:
            res.append(arr2[p2])
            p2 += 1

    res += arr1[p1:] + arr2[p2:]
    return res

