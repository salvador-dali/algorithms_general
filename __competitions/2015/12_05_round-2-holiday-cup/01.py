def check(n, h):
    if n % 2 == 0:
        return False

    m = n / 2
    if h[:m] != h[m+1:][::-1]:
        return False

    return all(h[i] < h[i+1] for i in xrange(m))

n = input()
H = map(int,raw_input().strip().split(' '))

print "Perfect" if check(n, H) else "Not perfect"