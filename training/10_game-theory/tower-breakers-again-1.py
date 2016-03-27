# https://www.hackerrank.com/challenges/tower-breakers-again-1
def mex(d):
    i = 0
    while i in d:
        i += 1

    return i

def get_divisors(n):
    small, large = [], []
    for i in xrange(1, int(n**0.5) + 1):
        if n % i == 0:
            small.append(i)
            if i != n / i:
                large.append(n / i)

    return small + large[::-1]

def get_sg_values(n):
    sg = [0, 0]
    for i in xrange(2, n + 1):
        vals = set()
        for towers_num in get_divisors(i)[1:]:
            if towers_num % 2 == 0:
                vals.add(0)
            else:
                vals.add(sg[i / towers_num])
        sg.append(mex(vals))

    return sg

sg = get_sg_values(100002)
for i in xrange(input()):
    input()
    res = 0
    for val in map(int, raw_input().split()):
        res ^= sg[val]

    print 1 if res != 0 else 2