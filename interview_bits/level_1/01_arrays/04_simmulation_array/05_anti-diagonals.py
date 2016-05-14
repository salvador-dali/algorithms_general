# https://www.interviewbit.com/problems/anti-diagonals/
def getAnti(M):
    n, res = len(M), []
    for x in xrange(n):
        res.append([M[i][x - i] for i in xrange(x + 1)])

    for x in xrange(1, n):
        res.append([M[x + i - 1][n - i] for i in xrange(1, n - x + 1)])

    return res
