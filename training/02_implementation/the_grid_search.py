# https://www.hackerrank.com/challenges/the-grid-search
def find_all(a_str, sub):
    arr, start = [], 0
    while True:
        start = a_str.find(sub, start)
        if start == -1:
            break
        arr.append(start)
        start += len(sub)

    return arr

def tryPattern(positions, M, sM, line):
    l = len(sM[0])
    for pos in positions:
        exist = 1
        for i in xrange(len(sM)):
            if sM[i] != M[i + line][pos:pos + l]:
                exist = 0
                break

        if exist:
            return 1

    return 0

def submatrix_search(M, sM):
    for i in xrange(len(M)):
        line = M[i]
        positions = find_all(line, sM[0])
        if positions:
            if tryPattern(positions, M, sM[1:], i + 1):
                return 1

    return 0


for i in xrange(int(raw_input())):
    a, b = map(int, raw_input().split())
    M = [raw_input() for j in xrange(a)]

    a, b = map(int, raw_input().split())
    sM = [raw_input() for j in xrange(a)]

    if submatrix_search(M, sM):
        print 'YES'
    else:
        print 'NO'
