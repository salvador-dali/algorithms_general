# https://www.interviewbit.com/problems/dungeon-princess/

def best_hp(arr):
    m, n = len(arr), len(arr[0])

    h = [[0] * m for i in xrange(n)]
    h[m - 1][n - 1] = max(1 - arr[m - 1][n - 1], 1)

    for i in xrange(m - 2, -1, -1):
        h[i][n - 1] = max(h[i + 1][n - 1] - arr[i][n - 1], 1)

    for i in xrange(n - 2, -1, -1):
        h[m - 1][i] = max(h[m - 1][i + 1] - arr[m - 1][i], 1)

    for i in xrange(m - 2, -1, -1):
        for j in xrange(n - 2, -1, -1):
            a = max(h[i + 1][j] - arr[i][j], 1)
            b = max(h[i][j + 1] - arr[i][j], 1)
            h[i][j] = min(a, b)

    return h[0][0]