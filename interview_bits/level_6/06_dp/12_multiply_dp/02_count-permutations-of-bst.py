# https://www.interviewbit.com/problems/count-permutations-of-bst/

# https://oeis.org/A244108
from math import factorial as f
def C(n, k):
    return f(n) / f(k) / f(n - k)

values = {}

def B(n, k):
    if n < 2:
        if k < n:
            return 0
        else:
            return 1

    if (n, k) in values:
        return values[(n, k)]

    s = 0
    for r in xrange(n):
        s += C(n - 1, r) * B(r, k - 1) * B(n - 1 - r, k - 1)

    values[(n, k)] = s
    return s

def solution(n, k):
    return B(n, k) - B(n, k - 1)

print solution(3, 3)