# http://articles.leetcode.com/the-painters-partition-problem-part-ii
# https://www.interviewbit.com/problems/painters-partition-problem/

def isPossible(arr, goal, k):
    sum_now, res = 0, []
    for i in arr:
        if sum_now + i <= goal:
            sum_now += i
        else:
            res.append(sum_now)
            sum_now = i

    res.append(sum_now)
    return len(res) <= k

def getMaximumPartition(arr, k):
    lo, hi = max(arr), sum(arr)
    while lo < hi:
        mid = lo + (hi - lo) / 2
        if isPossible(arr, mid, k):
            hi = mid
        else:
            lo = mid + 1
    return lo

