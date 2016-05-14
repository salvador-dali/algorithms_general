# https://www.interviewbit.com/problems/kth-row-of-pascals-triangle/
def pascal(k):
    arr = [1]
    for i in xrange(k):
        arr = [1] + [arr[j] + arr[j - 1] for j in xrange(1, len(arr))] + [1]
    return arr
