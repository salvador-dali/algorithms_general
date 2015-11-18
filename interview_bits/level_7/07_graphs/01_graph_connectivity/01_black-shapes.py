# https://www.interviewbit.com/problems/black-shapes/
def grow_mold(M, i, j):
    frontier = [(i, j)]
    tried = set([])
    while len(frontier):
        y, x = frontier.pop()
        tried.add((y, x))
        M[y][x] = 0
        for y1, x1 in [(y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)]:
            if (y1, x1) not in tried and y1 >= 0 and x1 >= 0 and y1 < len(M) and x1 < len(M[0]) and M[y1][x1] == 'X':
                frontier.append((y1, x1))


def connected(M):
    x, y = len(M[0]), len(M)
    count = 0
    for i in xrange(y):
        for j in xrange(x):
            if M[i][j] == '0':
                M[i][j] = 0
            elif M[i][j] == 'X':
                count += 1
                grow_mold(M, i, j)
    return count

s = ['OOOXOOO', 'OOXXOXO', 'OXOOOXO']
M = [list(i) for i in s]
connected(M)

