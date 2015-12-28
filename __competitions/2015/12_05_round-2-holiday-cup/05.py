mod = 10**9 + 9
for i in xrange(input()):
    n, k, c = map(int, raw_input().split())
    a = c * n * (n - 1) / 2 + (n - 1) * n * (n + 1) / 6 * k
    print a % mod