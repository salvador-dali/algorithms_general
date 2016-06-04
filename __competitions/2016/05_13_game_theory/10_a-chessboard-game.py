def mex_dict(d):
    i = 0
    while i in d:
        i += 1

    return i

def get_sg(n):
    M = [[0] * n for _ in xrange(n)]
    for i in xrange(2, n):
        for j in xrange(i + 1):
            x, y, values = i - j, j, set()
            for x_, y_ in [(x - 2, y + 1), (x - 2, y - 1), (x + 1, y - 2), (x - 1, y - 2)]:
                if 0 <= x_ < n and 0 <= y_ < n:
                    values.add(M[x_][y_])

            M[x][y] = mex_dict(values)

    for i in xrange(1, n):
        for j in xrange(n - 1, i - 1, -1):
            x, y, values = n + i - j - 1, j, set()
            for x_, y_ in [(x - 2, y + 1), (x - 2, y - 1), (x + 1, y - 2), (x - 1, y - 2)]:
                if 0 <= x_ < n and 0 <= y_ < n:
                    values.add(M[x_][y_])
            M[x][y] = mex_dict(values)
    return M

def knight_game(points):
    # points are 1 based, my SG is 0 based
    res = 0
    for x, y in points:
        res ^= SG[x - 1][y - 1]
    return res != 0

SG = get_sg(15)
for _ in xrange(input()):
    points = [map(int, raw_input().split()) for i in xrange(input())]
    print "First" if knight_game(points) else "Second"
