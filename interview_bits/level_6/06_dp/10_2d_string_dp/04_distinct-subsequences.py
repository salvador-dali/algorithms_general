# https://www.interviewbit.com/problems/distinct-subsequences/
def distinct_subsequences(s1, s2):
    M = [[0] * (len(s2) + 1) for _ in xrange(len(s1) + 1)]
    for i in xrange(len(s1) + 1):
        M[i][0] = 1

    for i in xrange(1, len(s1) + 1):
        for j in xrange(1, len(s2) + 1):
            M[i][j] += M[i - 1][j] + (0 if s1[i - 1] != s2[j - 1] else M[i - 1][j - 1])

    return M[-1][-1]
