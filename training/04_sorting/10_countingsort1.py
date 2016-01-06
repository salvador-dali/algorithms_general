# https://www.hackerrank.com/challenges/countingsort1/
def count(arr):
    h = {}
    for i in arr:
        if i in h:
            h[i] += 1
        else:
            h[i] = 1

    l = []
    for i in xrange(0, 100):
        if i in h:
            l.append(h[i])
        else:
            l.append(0)
    return l

raw_input()
arr = list(map(int, raw_input().split()))
print ' '.join(map(str, count(arr)))