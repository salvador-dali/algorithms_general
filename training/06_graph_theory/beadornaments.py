# https://www.hackerrank.com/challenges/beadornaments
for a in xrange(input()):
    n = input()
    arr = list(map(int, raw_input().split()))
    res = 1
    for i in arr:
        res *= i**(i-1)

    res *= sum(arr)**(n-2)
    print int(res) % 1000000007