# https://www.interviewbit.com/problems/max-continuous-series-of-1s/
def maxone(arr, k):
    p1, p2, start, end = 0, 0, None, None
    nZero, width = 0, -1
    while p2 < len(arr):
        if nZero <= k:
            nZero += int(arr[p2] == 0)
            p2 += 1

        if nZero > k:
            nZero -= int(arr[p1] == 0)
            p1 += 1

        if p2 - p1 + 1 > width:
            width = p2 - p1 + 1
            start, end = p1, p2

    return range(start, end)


