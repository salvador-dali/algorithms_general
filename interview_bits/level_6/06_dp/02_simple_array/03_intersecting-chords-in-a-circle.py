# https://www.interviewbit.com/problems/intersecting-chords-in-a-circle/
def catalan(n):
    prev = 1
    for i in xrange(n):
        prev = prev * 2 * (2 * i + 1) / (i + 2)
    return prev % (10**9 + 7)
