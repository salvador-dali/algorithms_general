# https://www.hackerrank.com/contests/indeed-prime-codesprint/challenges/divyam-and-sorted-list
def analyse(a1, a2):
    prev = 0
    for i in xrange(len(a1)):
        changed = False
        m, M = min(a1[i], a2[i]), max(a1[i], a2[i])
        if m >= prev:
            prev = m
            changed = True
        elif M >= prev:
            prev = M
            changed = True

        if not changed:
            return False

    return True

for i in xrange(input()):
    input()
    arr1 = map(int, raw_input().split())
    arr2 = map(int, raw_input().split())
    print 'YES' if analyse(arr1, arr2) else 'NO'