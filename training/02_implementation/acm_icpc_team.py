# https://www.hackerrank.com/challenges/acm-icpc-team/
def maximum(arr):
    l, m, n = len(arr), 0, 0
    for i in xrange(l):
        for j in xrange(i + 1, l):
            num = bin(arr[i] | arr[j]).count("1")
            if num > m:
                m, n = num, 1
            elif num == m:
                n += 1

    print m
    print n

a, b = map(int, raw_input().split())
maximum([int(raw_input(), 2) for i in range(a)])