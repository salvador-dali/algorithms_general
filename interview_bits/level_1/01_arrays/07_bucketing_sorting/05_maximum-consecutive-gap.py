# https://www.interviewbit.com/problems/maximum-consecutive-gap/

def solution(arr):
    arr.sort()
    m = 0
    for i in xrange(len(arr) - 1):
        m = max(arr[i + 1] - arr[i], m)

    return m

print solution([1])