def count(n):
    m, r = n % 4, n / 4
    if m == 0:
        return 1 + 2*r, -2*r
    if m == 1:
        return 1 + 2*r, 2 + 2*r
    if m == 2:
        return -2 - 2*r, 2 + 2*r
    if m == 3:
        return -2 - 2*r, -2-2*r

for i in xrange(input()):
    print ' '.join(map(str, count(input() - 1)))