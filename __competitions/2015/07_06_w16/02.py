# http://math.stackexchange.com/q/1352997/50804

def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise ValueError
    return x % m

def analyse(digits, counts, factorials, reverse_factorials, mod):
    n = sum(counts)
    if n == 0:
        return 0

    M = factorials[n]
    for i in counts:
        M = (M * reverse_factorials[i]) % mod

    s = sum(j * d for j, d in zip(digits, counts)) % mod

    part1 = s * ((pow(10, n, mod) - 1) % mod) * M
    return (part1 * modinv(9 * n, mod)) % mod


def solution(d1, d2, d3):
    factorials, mod = [1], 10**9 + 7
    for i in xrange(1, 301):
        factorials.append((factorials[-1] * i) % mod)

    reverse_factorials = [modinv(i, mod) for i in factorials]

    s = 0
    for i in xrange(d1 + 1):
        for j in xrange(d2 + 1):
            for k in xrange(d3 + 1):
                s = (s + analyse([4, 5, 6], [i, j, k], factorials, reverse_factorials, mod)) % mod
    return s % mod

d1, d2, d3 = map(int, raw_input().split())
print solution(d1, d2, d3)