def smallPerm(n):
    if n % 2:
        a, b = range(n/2 + 1, n), range(n/2, 0, -1)
    else:
        a, b = range(n/2, 0, -1), range(n/2 + 1, n + 1)
    
    arr = []
    for i in xrange(len(a)):
        arr.append(a[i])
        arr.append(b[i])

    if n % 2:
        arr.append(n)
    return arr

for i in xrange(input()):
    print ' '.join(map(str, smallPerm(input())))