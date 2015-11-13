# https://www.interviewbit.com/problems/scramble-string/
from collections import Counter as C

def is_scrambles(s1, s2):
    if len(s2) == 1:
        return True

    res = False
    for i in xrange(1, len(s2)):
        p1, p2, p3, p4, p5, p6 = s2[:i], s2[i:], s1[:i], s1[i:], s1[:len(s1) - i], s1[len(s1) - i:]
        c1, c2, c3, c4, c5, c6 = C(p1), C(p2), C(p3), C(p4), C(p5), C(p6)

        if c1 == c3 and c2 == c4:
            res |= is_scrambles(p1, p3) and is_scrambles(p2, p4)

        if c1 == c6 and c2 == c5:
            res |= is_scrambles(p1, p6) and is_scrambles(p2, p5)

    return res