# https://www.interviewbit.com/problems/array-3-pointers/

def analyze(arr1, arr2, arr3):
    p1, p2, p3 = 0, 0, 0
    minimum = float("inf")

    num = 0
    while p1 < len(arr1) and p2 < len(arr2) and p3 < len(arr3):
        num += 1
        delta12, delta23, delta31 = abs(arr1[p1] - arr2[p2]), abs(arr2[p2] - arr3[p3]), abs(arr3[p3] - arr1[p1])
        m = max(delta12, delta23, delta31)
        minimum = min(m, minimum)
        if m == delta12:
            if arr1[p1] < arr2[p2]:
                p1 += 1
            else:
                p2 += 1
            continue
        if m == delta23:
            if arr2[p2] < arr3[p3]:
                p2 += 1
            else:
                p3 += 1
            continue
        if m == delta31:
            if arr1[p1] < arr3[p3]:
                p1 += 1
            else:
                p3 += 1
            continue
    return minimum
