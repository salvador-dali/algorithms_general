for _ in xrange(input()):
    N, K = map(int, raw_input().split())
    arr = list(map(int, raw_input().split()))
    if sum(x <= 0 for x in arr) < K:
        print 'YES'
    else:
        print 'NO'