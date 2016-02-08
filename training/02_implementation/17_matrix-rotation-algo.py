# https://www.hackerrank.com/challenges/matrix-rotation-algo
def matrix2lines(M):
    pos, y, x = 0, len(M), len(M[0])
    m, lines = min(y, x), []

    while pos < m / 2:
        line = [M[pos][i] for i in xrange(pos, x - pos)] +\
               [M[i][x - pos - 1] for i in xrange(pos + 1, y - pos - 1)] +\
               [M[y - pos - 1][i] for i in xrange(pos, x - pos)][::-1] +\
               [M[i][pos] for i in xrange(pos + 1, y - pos - 1)][::-1]
        lines.append(line)
        pos += 1

    return lines, x, y

def shiftLines(lines, n):
    newLines = []
    for line in lines:
        tmp = n % len(line)
        newLines.append(line[tmp:] + line[:tmp])
    return newLines

def lines2matrix(lines, x, y):
    M = [[0 for i in xrange(x)] for j in xrange(y)]

    for pos in xrange(len(lines)):
        line = lines[pos]
        top = line[:x - 2*pos]
        right = line[x-2*pos: x+y-2-4*pos]
        bottom = line[x+y-2-4*pos: x+y-2-4*pos+x-2*pos][::-1]
        left = line[x+y-2-4*pos+x-2*pos:][::-1]

        for i in xrange(len(top)):
            M[pos][i+pos] = top[i]
            M[y-1-pos][i+pos] = bottom[i]

        for i in xrange(len(right)):
            M[i + 1 + pos][x-1-pos] = right[i]
            M[i + 1 + pos][pos] = left[i]

    return M

def printMatrix(M):
    for i in M:
        print ' '.join(map(str, i))

y, x, r = map(int, raw_input().split())
M = []
for i in xrange(y):
    M.append(map(int, raw_input().split()))

lines, x, y = matrix2lines(M)
lines = shiftLines(lines, r)
M = lines2matrix(lines, x, y)
printMatrix(M)