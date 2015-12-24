def toilet(n, m):
    # n - number of toilets
    # m - number of people

    dirtiness = (m - 1) / n
    position = m % n
    if not position:
        position = n

    if n % 2 == 0:
        if position % 2:
            return position / 2 + 1, dirtiness
        else:
            return n + 1 - position / 2, dirtiness

    if dirtiness % 2 == 0:
        if position % 2:
            return position / 2 + 1, dirtiness
        else:
            return n + 1 - position / 2, dirtiness
    else:
        if position % 2:
            return n - position / 2, dirtiness
        else:
            return position / 2, dirtiness

for i in xrange(input()):
    n, m = map(int, raw_input().split())
    print ' '.join(map(str, toilet(n, m)))