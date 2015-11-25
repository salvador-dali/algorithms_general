# https://www.interviewbit.com/problems/distinct-initial-matrices

def factorial_mod(n, mod):
    r = 1
    for i in xrange(1, n + 1):
        r = (r * i) % mod

    return r

def get_divisors(n):
    small, large = [], []
    for i in xrange(1, int(n**0.5) + 1):
        if n % i == 0:
            small.append(i)
            if i != n / i:
                large.append(n / i)

    return small + large[::-1]

def chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i+n]

def is_increasing(l):
    return all(l[i] <= l[i+1] for i in xrange(len(l)-1))

def is_n_increasing(arr, n):
    return all(is_increasing(i) for i in chunks(arr, n))

def solve(arr):
    s, mod = 0, 10**9 + 7
    for div in get_divisors(len(arr)):
        is_incr = is_n_increasing(arr, div)
        if is_incr:
            s = (s + pow(factorial_mod(div, mod), len(arr) / div, mod)) % mod

    return s

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 46, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 25, 47, 48, 49, 50 ]
print solve(arr)
