# https://www.interviewbit.com/problems/points-on-the-straight-line/
from collections import Counter

def gcd(a, b):
    while a:
        a, b = b % a, a
    return b

def getSignature(p1, p2):
    dx, dy = p2[0] - p1[0], p2[1] - p1[1]
    m = gcd(dx, dy)
    return -1 if dx * dy < 0 else 1, abs(dx/m), abs(dy/m)

def findPoints(points):
    if not len(points):
        return 0

    pts, best = [(k, v) for k, v in Counter(points).iteritems()], 0
    if len(pts) == 1:
        return pts[0][1]

    for i in xrange(len(pts)):
        cnt = Counter()
        for j in xrange(len(pts)):
            if i != j:
                cnt[getSignature(pts[i][0], pts[j][0])] += pts[j][1]

        best = max(best, cnt.most_common(1)[0][1] + pts[i][1])

    return best
