# https://www.interviewbit.com/problems/set-matrix-zeros/

def setZeros(M):
    # Space O(n + m), time O(n*m) actually 3 * n * m
    cols_zeros, rows_zeros = set([]), set([])
    for i in xrange(len(M)):
        for j in xrange(len(M[0])):
            if M[i][j] == 0:
                cols_zeros.add(j)
                rows_zeros.add(i)

    for r in rows_zeros:
        for i in xrange(len(M[0])):
            M[r][i] = 0

    for c in cols_zeros:
        for i in xrange(len(M)):
            M[i][c] = 0

    return M

def setZerosConstant(M):
    # takes O(1) space
    R, C = 1, 1
    for i in xrange(len(M[0])):
        if M[0][i] == 0:
            R = 0
            break

    for i in xrange(len(M)):
        if M[i][0] == 0:
            C = 0
            break

    for i in xrange(len(M)):
        for j in xrange(len(M[0])):
            if M[i][j] == 0:
                M[0][j] = 0
                M[i][0] = 0

    for i in xrange(1, len(M[0])):
        if M[0][i] == 0:
            for j in xrange(1, len(M)):
                M[j][i] = 0

    for i in xrange(1, len(M)):
        if M[i][0] == 0:
            for j in xrange(1, len(M[0])):
                M[i][j] = 0

    if R == 0:
        for i in xrange(len(M[0])):
            M[0][i] = 0

    if C == 0:
        for i in xrange(len(M)):
            M[i][0] = 0

    return M

