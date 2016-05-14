# https://www.interviewbit.com/problems/spiral-order-matrix-ii/
def generateSpiral(n):
    M = [[0 for i in xrange(n)] for j in xrange(n)]
    x1, y1, x2, y2, direction, num = 0, 0, n - 1, n - 1, 'right', 1

    while x1 <= x2 and y1 <= y2:
        if direction == 'right':
            for i in xrange(x1, x2 + 1):
                M[y1][i] = num
                num += 1
            direction, y1 = 'down', y1 + 1

        elif direction == 'down':
            for i in xrange(y1, y2 + 1):
                M[i][x2] = num
                num += 1
            direction, x2 = 'left', x2 - 1

        elif direction == 'left':
            for i in xrange(x2, x1 - 1, -1):
                M[y2][i] = num
                num += 1
            direction, y2 = 'up', y2 - 1

        elif direction == 'up':
            for i in xrange(y2, y1 - 1, -1):
                M[i][x1] = num
                num += 1
            direction, x1 = 'right', x1 + 1

    return M
