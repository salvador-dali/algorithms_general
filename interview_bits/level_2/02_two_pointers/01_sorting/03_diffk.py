# https://www.interviewbit.com/problems/diffk/
def diff(arr, k):
    p1, p2, n = 0, 1, len(arr)
    while p1 < n and p2 < n:
        tmp = arr[p2] - arr[p1] - k
        if p1 != p2 and tmp == 0:
            return 1

        if tmp < 0:
            p2 += 1
        else:
            p1 += 1

    return 0
