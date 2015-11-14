# https://www.interviewbit.com/problems/edit-distance/
def min_distance(s1, s2):
    M = [[0] * (len(s1) + 1) for _ in xrange(len(s2) + 1)]

    M[0] = range(len(s1) + 1)
    for i in xrange(len(s2) + 1):
        M[i][0] = i

    for i in xrange(len(s2)):
        for j in xrange(len(s1)):
            M[i + 1][j + 1] = min(M[i][j + 1] + 1, M[i + 1][j] + 1, M[i][j] + 1 if s2[i] != s1[j] else M[i][j])

    return M[-1][-1]