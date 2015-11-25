# https://www.interviewbit.com/problems/increasing-subarrays
def count_inc(arr):
    arr.append(float('-inf'))
    cnt, res = 0, 0
    for i in xrange(len(arr) - 1):
        if arr[i + 1] > arr[i]:
            cnt += 1
        else:
            res += (cnt + 1) * cnt / 2
            cnt = 0

    return res + len(arr) - 1
