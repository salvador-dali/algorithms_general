# https://www.hackerrank.com/challenges/manasa-and-stones
for _ in xrange(int(raw_input())):
    n, a, b = int(raw_input()), int(raw_input()), int(raw_input())
    s = set()
    for i in range(0, n):
        s.add(i * a + (n - i - 1) * b)

    s = list(s)
    s = sorted(s)
    print ' '.join(map(str, s))