# https://www.interviewbit.com/problems/pascal-triangle-rows/
def generateRows(k):
    if k == 0:
        return []

    res, arr = [[1]], [1]
    for i in xrange(k - 1):
        arr = [1] + [arr[j] + arr[j - 1] for j in xrange(1, len(arr))] + [1]
        res.append(arr)

    return res
