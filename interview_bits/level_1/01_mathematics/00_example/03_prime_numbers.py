# https://www.interviewbit.com/problems/prime-numbers/
def eratosthenes_sieve(n):
    prime, result, sqrt_n = [True] * n, [2], (int(n ** .5) + 1) | 1
    append = result.append
    for p in xrange(3, sqrt_n, 2):
        if prime[p]:
            append(p)
            prime[p*p::p << 1] = [False] * ((n - p*p - 1) / (p << 1) + 1)

    return result + [p for p in xrange(sqrt_n, n, 2) if prime[p]]