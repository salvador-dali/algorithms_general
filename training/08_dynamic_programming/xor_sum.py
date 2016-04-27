a = '1011001'
b = '1010'

a, b = int(a, 2), int(b, 2)
n = 314159
n = 5


s = 0
for i in xrange(n + 1):
    t = a ^ b

    print '{:015b}'.format(a)
    print '{:015b}'.format(b)
    print '{:015b}'.format(t)
    print

    b *= 2
    s += t

print s % (10**9 + 7)