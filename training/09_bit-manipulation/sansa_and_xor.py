# https://www.hackerrank.com/challenges/sansa-and-xor
for i in xrange(input()):
    if input() % 2:
        s, arr = 0, list(map(int, raw_input().split()))
        for i in xrange(0, len(arr), 2):
            s ^= arr[i]
        print s
    else:
        print 0
        raw_input()