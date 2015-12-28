def sub_task(a1, a2):
    b1 = set(map(int, list(str(a1))))
    b2 = set(map(int, list(str(a2))))
    return sum((b1 - b2) | (b2 - b1))

def solution(n):
    return sum(sub_task(i, j) for i in xrange(1, n + 1) for j in xrange(1, n + 1))

def analyze(a1, a2):
    b1 = set(map(int, list(str(a1))))
    b2 = set(map(int, list(str(a2))))
    a = list((b1 - b2) | (b2 - b1))
    a.sort()
    return tuple(a)

def analyze_more(n):
    from collections import defaultdict

    d = defaultdict(int)
    for i in xrange(1, n + 1):
        for j in xrange(1, n + 1):
            d[analyze(i, j)] += 1

    print len(d)


def analyze_lot(n, arr):
    total = 0
    for i in xrange(1, n + 1):
        for j in xrange(1, n + 1):
            if arr == analyze(i, j):
                print i, j
                total += 1

    print
    print total


analyze_lot(234, (1, 2, 6))