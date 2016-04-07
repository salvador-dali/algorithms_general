# https://www.interviewbit.com/problems/3-sum-zero/

def sum_three(arr):
    arr.sort()
    n, res = len(arr), set()
    for i in xrange(n - 2):
        start, end = i + 1, n - 1
        while start < end:
            tmp = arr[i] + arr[start] + arr[end]
            if tmp == 0:
                res.add((arr[i], arr[start], arr[end]))
                end -= 1
            elif tmp > 0:
                end -= 1
            else:
                start += 1

    res = list(res)
    res.sort()
    return res