# https://www.interviewbit.com/problems/power-of-two-integers/
from collections import Counter

def factorize(n):
    step = lambda x: 1 + (x << 2) - ((x >> 1) << 1)
    maximum, d = n ** 0.5, 1
    q = n % 2 == 0 and 2 or 3
    while q <= maximum and n % q != 0:
        q = step(d)
        d += 1

    return [q] + factorize(n / q) if q <= maximum else [n]

def gcd(a, b):
    while b:
        a, b = b, a % b

    return a

def gcd_multiple(arr):
    prev = arr[0]
    for i in xrange(len(arr)):
        prev = gcd(prev, arr[i])
    return prev

def isPower(n):
    if n == 1:
        return True
    if n < 4:
        return False

    v = Counter(factorize(n)).values()
    res = gcd_multiple(v)
    return res != 1
