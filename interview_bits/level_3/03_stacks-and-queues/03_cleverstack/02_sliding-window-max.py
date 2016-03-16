# https://www.interviewbit.com/problems/sliding-window-max/
# http://stackoverflow.com/a/17249084/1090562
# http://stackoverflow.com/a/8499392/1090562
# http://stackoverflow.com/a/4802260/1090562

def maxSliding(arr, k):
    if len(arr) == 0:
        return []
    if len(arr) <= k:
        return [max(arr)]

    maxL, maxR = [0]*len(arr), [0] * len(arr)
    for i in xrange(len(arr)):
        maxSoFar = arr[i] if i % k == 0 else max(maxSoFar, arr[i])
        maxL[i] = maxSoFar


    maxSoFar = float("-inf")
    for i in xrange(len(arr) - 1, -1, -1):
        maxSoFar = arr[i] if i % k == k - 1 else max(maxSoFar, arr[i])
        maxR[i] = maxSoFar

    return [max(maxR[i], maxL[i + k - 1]) for i in xrange(len(arr) - k + 1)]