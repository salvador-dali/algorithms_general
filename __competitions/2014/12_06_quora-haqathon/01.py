from bisect import bisect_right
from math import sqrt

def intersection(x, y, radii):
    r = sqrt(x**2 + y**2)
    pos = bisect_right(radii, r)
    return len(radii) - pos

def attempt(radii, lines):
    normalLines = [list(map(abs, i)) for i in lines]
    s = 0
    for x1, y1, x2, y2 in normalLines:
        n1 = intersection(x1, y1, radii)
        n2 = intersection(x2, y2, radii)
        s += abs(n2 - n1)

    print s
    
input()
radii = list(map(int, raw_input().split()))
radii.sort()
lines = []
for i in xrange(input()):
    lines.append(list(map(int, raw_input().split())))
    
attempt(radii, lines)