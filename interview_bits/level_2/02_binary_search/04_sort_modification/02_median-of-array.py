arr1 = [1, 4, 5]
arr2 = [2, 3, 3, 4]

def median2(a, b):
    return (a + b) / 2.

def median3(a, b, c):
    return sorted([a, b, c])[1]

def median4(a, b, c, d):
    tmp = sorted([a, b, c, d])
    return (tmp[1] + tmp[2]) / 2.

def findMedianUtil(A, N, B, M):
    if N == 0:
        m = len(B)
        if m % 2:
            return B[m / 2]
        return median2(B[m / 2 - 1], B[m / 2])
    if N == 1:
        if M == 1:
            return median2(A[0], B[0])
        if M % 2:
            return median2(B[M/2], median3(A[0], B[M/2 - 1], B[M/2 + 1]))
        return median3(B[M/2], B[M/2 - 1], A[0])

    if N == 2:
        if M == 2:
            return median4(A[0], A[1], B[0], B[1])
        if M % 2:
            return median3(B[M/2], max(A[0], B[M/2 - 1]), min(A[1], B[M/2 + 1]))
        return median4(B[M/2], B[M/2 - 1], max(A[0], B[M/2 - 2]), min(A[1], B[M/2 + 1]))

    idxA, idxB = (N - 1) / 2, (M - 1) / 2
    if A[idxA] <= B[idxB]:
        return findMedianUtil(A + idxA, N / 2 + 1, B, M - idxA)

    return findMedianUtil( A, N / 2 + 1, B + idxA, M - idxA )

def findMedian(arr1, arr2):
    if len(arr1) > len(arr2):
        return findMedianUtil(arr2, len(arr2), arr1, len(arr1))

    return findMedianUtil(arr1, len(arr1), arr2, len(arr2))


print findMedian([], arr2)