# https://www.hackerrank.com/challenges/poker-nim-1
for i in xrange(input()):
    n, k = map(int, raw_input().split())
    arr = map(int, raw_input().split())
    res = reduce(lambda x,y: x^y, arr)
    if res == 0:
        print 'Second'
    else:
        print 'First'