for i in xrange(input()):
    A, N, M = map(int, raw_input().split())
    if A == 0 or A % M == 0:
        print 0
        break
    
    t = 10**len(str(A))
    print (A * (1 - pow(t, N)) / (1 - t)) % M