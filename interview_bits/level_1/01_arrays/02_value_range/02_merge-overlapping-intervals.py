# https://www.interviewbit.com/problems/merge-overlapping-intervals/

def merge(arr):
    if len(arr) == 0:
        return []

    # arr = [[i.start, i.end] for i in arr]
    arr.sort()
    res, prevInterval = [], arr[0]
    for interval in arr[1:]:
        if prevInterval[1] >= interval[0]:
            prevInterval = [prevInterval[0], max(prevInterval[1], interval[1])]
        else:
            res.append(prevInterval)
            prevInterval = [interval[0], interval[1]]

    res.append(prevInterval)

    # res = [Interval(i[0], i[1]) for i in res]
    return res
