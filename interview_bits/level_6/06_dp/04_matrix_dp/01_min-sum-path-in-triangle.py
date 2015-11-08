# https://www.interviewbit.com/problems/min-sum-path-in-triangle/
def find_min(arr):
    if len(arr) == 1:
        return arr[0][0]

    for i in xrange(1, len(arr)):
        attempt = [float('inf')] * len(arr[i])

        for j in xrange(len(arr[i - 1])):
            attempt[j] = min(attempt[j], arr[i - 1][j] + arr[i][j])
            attempt[j + 1] = min(attempt[j + 1], arr[i - 1][j] + arr[i][j + 1])
        arr[i] = attempt

    return min(arr[i])
