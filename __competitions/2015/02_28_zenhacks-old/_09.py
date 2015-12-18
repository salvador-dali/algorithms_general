import bisect
def main(arr):
    n = 3*10**7
    primes = sieveEratosthenes(n)
    l, composites = len(primes), []
    for i in xrange(l):
        for j in xrange(i, l):
            tmp = primes[i] * primes[j]
            if tmp > n:
                break

            composites.append(tmp)

    composites.sort()
    return [bisect.bisect_right(composites, i) for i in arr]

def sieveEratosthenes(n):
    prime = [True] * n
    result = [2]
    append = result.append
    sqrt_n = (int(n ** .5) + 1) | 1
    for p in xrange(3, sqrt_n, 2):
        if prime[p]:
            append(p)
            prime[p*p::2*p] = [False] * ((n - p*p - 1) / (2*p) + 1)
    for p in xrange(sqrt_n, n, 2):
        if prime[p]:
            append(p)
    return result

arr = [input() for i in xrange(input())]
for i in main(arr):
    print i