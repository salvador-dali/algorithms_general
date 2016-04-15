# https://www.interviewbit.com/problems/longest-common-prefix/

def longestCommon(arr):
    if len(arr) == 0:
        return 0
    if len(arr) == 1:
        return arr[0]

    for pos in xrange(len(arr[0])):
        char = arr[0][pos]
        for i in xrange(1, len(arr)):
            if pos >= len(arr[i]) or arr[i][pos] != char:
                return arr[0][:pos]

    return arr[0]

