# https://www.interviewbit.com/problems/rearrange-array/
def rearrange(arr):
    n = len(arr)
    for i in xrange(n):
        arr[i] += n * (arr[arr[i]] % n)

    for i in xrange(n):
        arr[i] /= n

    return arr
