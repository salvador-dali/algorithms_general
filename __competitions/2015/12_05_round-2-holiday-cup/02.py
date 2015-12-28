mod = 10**9 + 7

def factorials(n):
    f = [0] * (n + 1)
    f[1] = 1
    for i in xrange(2, n + 1):
        f[i] = (f[i - 1] * i) % mod

    return f

f = factorials(1000003)

def books(n, k, f):
    res = (pow(8, k, mod) * f[k]) % mod
    if n == k:
        return (res * 3) % mod
    
    return res

for i in xrange(input()):
    n, k = map(int, raw_input().split())
    print books(n, k, f)