# https://www.hackerrank.com/challenges/fibonacci-modified
# completely the same as Fibonacci, but the terms are defined in a different way
def sequence(a, b, n):
    for i in xrange(n - 2):
        a, b = b, a + b**2
    return b

a, b, n = map(int, raw_input().split())
print sequence(a, b, n)