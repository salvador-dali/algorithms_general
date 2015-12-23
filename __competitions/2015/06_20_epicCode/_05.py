def analyse(arr):
    print sum(all(a1 > a2 or b1 < b2 for a2, b2 in arr if (a1, b1) != (a2, b2)) for a1, b1 in arr)

lines = [tuple(map(int, raw_input().split())) for i in xrange(input())]
lines = list(set(lines))
analyse(lines)