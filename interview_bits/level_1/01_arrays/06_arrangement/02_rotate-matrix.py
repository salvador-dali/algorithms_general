# https://www.interviewbit.com/problems/rotate-matrix/

def rotate(M):
    n = len(M)
    for i in xrange(n):
        for j in xrange(i, n):
            M[i][j], M[j][i] = M[j][i], M[i][j]

    for i in xrange(n):
        for j in xrange(n / 2):
            M[i][j], M[i][n - j - 1] = M[i][n - j - 1], M[i][j]

    return M
