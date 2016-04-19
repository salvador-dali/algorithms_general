# https://www.interviewbit.com/problems/allocate-books/
def isPossible(arr, maximum, k):
    sum_now, res = 0, []
    for i in arr:
        if sum_now + i <= maximum:
            sum_now += i
        else:
            res.append(sum_now)
            sum_now = i

    res.append(sum_now)
    print res
    return len(res) <= k

def allocation(arr, m):
    if m > len(arr):
        return -1
    lo, hi = max(arr), sum(arr)
    while lo < hi:
        mid = lo + (hi - lo) / 2
        if isPossible(arr, mid, m):
            hi = mid
        else:
            lo = mid + 1

    return lo