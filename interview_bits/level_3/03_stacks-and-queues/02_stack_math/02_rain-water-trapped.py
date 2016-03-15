# https://www.interviewbit.com/problems/rain-water-trapped/
arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

def water_trapped(arr):
    maximumRight, prevMax = [0] * len(arr), 0
    for i in xrange(len(arr)):
        maximumRight[i] = max(prevMax, arr[i])
        prevMax = maximumRight[i]

    maximumLeft, prevMax = [0] * len(arr), 0
    for i in xrange(len(arr) - 1, -1, -1):
        maximumLeft [i] = max(prevMax, arr[i])
        prevMax = maximumLeft[i]

    res = 0
    for i in xrange(len(arr)):
        h = min(maximumLeft[i], maximumRight[i])
        if h > arr[i]:
            res += h - arr[i]

    return res

def water_trapped2(arr):
    if len(arr) <= 2:
        return 0

    total, pos_left, pos_right, best_height = 0, 0, len(arr) - 1, 0
    while pos_left < pos_right:
        if arr[pos_left] < arr[pos_right]:
            best_height = max(best_height, arr[pos_left])
            total += best_height - arr[pos_left]
            pos_left += 1

        else:
            best_height = max(best_height, arr[pos_right])
            total += best_height - arr[pos_right]
            pos_right -= 1

    return total


import random
for i in xrange(1000):
    arr = [random.randint(1, 500) for i in xrange(5000)]
    if water_trapped(arr) != water_trapped2(arr):
        print 'AAAA'