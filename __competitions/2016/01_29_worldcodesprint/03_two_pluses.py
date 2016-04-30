# https://www.hackerrank.com/contests/worldcodesprint/challenges/two-pluses
def getBiggestPossibleStar(M):
    n, m = len(M), len(M[0])
    t = min(n, m)
    if t % 2 == 0:
        t -= 1

    return t

def findStars(M, l):
    stars = []
    for i in xrange(len(M) - l + 1):
        for j in xrange(len(M[0]) - l + 1):
            if all(M[i + l / 2][k] == 0 for k in xrange(j, j + l)) and all(M[k][j + l / 2] == 0 for k in xrange(i, i + l)):
                stars.append((i, j))
    return stars

def removeStar(M, l, pos):
    M_copy = [row[:] for row in M]
    i, j = pos

    for k in xrange(j, j + l):
        M_copy[i + l / 2][k] = 1

    for k in xrange(i, i + l):
        M_copy[k][j + l / 2] = 1

    return M_copy

def isStartExist(M, l):
    for i in xrange(len(M) - l + 1):
        for j in xrange(len(M[0]) - l + 1):
            if all(M[i + l / 2][k] == 0 for k in xrange(j, j + l)) and all(M[k][j + l / 2] == 0 for k in xrange(i, i + l)):
                return True
    return False

def solution(M):
    bestAnswer = 0
    t = getBiggestPossibleStar(M)

    for size1 in xrange(t, 0, -2):
        stars = findStars(M, size1)
        for star in stars:
            M_ = removeStar(M, size1, star)
            for size2 in xrange(size1, 0, -2):
                if isStartExist(M_, size2):
                    attempt = (2 * size1 - 1) * (2 * size2 - 1)
                    if attempt > bestAnswer:
                        bestAnswer = attempt
    return bestAnswer

n, m = map(int, raw_input().split())
s = [raw_input() for i in xrange(n)]
M = [[int(i == 'B') for i in list(s_)] for s_ in s]
print solution(M)