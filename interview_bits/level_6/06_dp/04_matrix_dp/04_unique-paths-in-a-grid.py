# https://www.interviewbit.com/problems/unique-paths-in-a-grid/
def find_solutions(arr):
    if arr[0][0] == 1 or arr[-1][-1] == 1:
        return 0

    for i in xrange(len(arr)):
        arr[i] = [0] + arr[i]

    arr = [[0] * (len(arr[0]))] + arr
    y, x = len(arr), len(arr[0])
    for i in xrange(y):
        for j in xrange(x):
            arr[i][j] = -arr[i][j]

    arr[1][1] = 1

    for i in xrange(1, y):
        for j in xrange(1, x):
            if arr[i][j] == -1:
                continue
            a = 0 if arr[i - 1][j] == -1 else arr[i - 1][j]
            b = 0 if arr[i][j - 1] == -1 else arr[i][j - 1]
            arr[i][j] += a + b

    return arr[-1][-1]