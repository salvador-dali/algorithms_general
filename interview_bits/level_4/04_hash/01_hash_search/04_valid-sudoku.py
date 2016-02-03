# https://www.interviewbit.com/problems/valid-sudoku/
from collections import Counter

def isValidCounter(cnt):
    del cnt[0]
    for i in cnt:
        if cnt[i] > 1:
            return False
    return True

def isValid(arr):
    M = [[int(i) if i != '.' else 0 for i in line] for line in arr]

    # rows
    for i in M:
        if not isValidCounter(Counter(i)):
            return False

    # columns
    for i in xrange(9):
        if not isValidCounter(Counter(M[j][i] for j in xrange(9))):
            return False

    # squares
    squares = [
        [M[0][i] for i in xrange(0, 3)] + [M[1][i] for i in xrange(0, 3)] + [M[2][i] for i in xrange(0, 3)],
        [M[0][i] for i in xrange(3, 6)] + [M[1][i] for i in xrange(3, 6)] + [M[2][i] for i in xrange(3, 6)],
        [M[0][i] for i in xrange(6, 9)] + [M[1][i] for i in xrange(6, 9)] + [M[2][i] for i in xrange(6, 9)],

        [M[3][i] for i in xrange(0, 3)] + [M[4][i] for i in xrange(0, 3)] + [M[5][i] for i in xrange(0, 3)],
        [M[3][i] for i in xrange(3, 6)] + [M[4][i] for i in xrange(3, 6)] + [M[5][i] for i in xrange(3, 6)],
        [M[3][i] for i in xrange(6, 9)] + [M[4][i] for i in xrange(6, 9)] + [M[5][i] for i in xrange(6, 9)],

        [M[6][i] for i in xrange(0, 3)] + [M[7][i] for i in xrange(0, 3)] + [M[8][i] for i in xrange(0, 3)],
        [M[6][i] for i in xrange(3, 6)] + [M[7][i] for i in xrange(3, 6)] + [M[8][i] for i in xrange(3, 6)],
        [M[6][i] for i in xrange(6, 9)] + [M[7][i] for i in xrange(6, 9)] + [M[8][i] for i in xrange(6, 9)]
    ]
    for square in squares:
        if not isValidCounter(Counter(square)):
            return False

    return True


print isValid(arr)