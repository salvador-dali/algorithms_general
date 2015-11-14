# https://www.interviewbit.com/problems/repeating-sub-sequence/
def repeating(s):
    n = len(s) + 1
    M = [[0] * n for _ in xrange(n)]

    for i in xrange(1, n):
        for j in xrange(1, n):
            if s[i - 1] == s[j - 1] and i != j:
                M[i][j] = 1 + M[i - 1][j - 1]
            else:
                M[i][j] = max(M[i - 1][j], M[i][j - 1])

    return M[-1][-1] >= 2
