# https://www.hackerrank.com/challenges/manasa-and-stones
for _ in xrange(input()):
    n, a, b = input(), input(), input()
    s = set()
    for i in range(0, n):
        s.add(i * a + (n - i - 1) * b)

    s = list(s)
    s = sorted(s)
    print ' '.join(map(str, s))