# https://www.interviewbit.com/problems/coins-in-a-line/
def best_sum(arr):
    if len(arr) == 0:
        return 0
    F = {(i, i): arr[i] for i in xrange(len(arr))}
    for i in xrange(len(arr) - 1):
        F[(i, i + 1)] = max(arr[i], arr[i + 1])

    def calcF(arr, i, j):
        if (i, j) in F:
            return F[(i, j)]

        v1 = arr[i] + min(calcF(arr, i + 2, j), calcF(arr, i + 1, j - 1))
        v2 = arr[j] + min(calcF(arr, i + 1, j - 1), calcF(arr, i, j - 2))
        res = max(v1, v2)
        F[(i, j)] = res
        return res

    return calcF(arr, 0, len(arr) - 1)

