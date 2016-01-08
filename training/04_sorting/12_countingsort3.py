# https://www.hackerrank.com/challenges/countingsort3
def countLess(arr):
    n = 100
    l = [0] * n
    for i in arr:
        l[i] += 1

    s, l1 = 0, []
    for i in xrange(n):
        s += l[i]
        l1.append(s)

    return l1

arr = []
for i in xrange(int(raw_input())):
    t = raw_input().split()
    arr.append(int(t[0]))

print ' '.join(map(str, countLess(arr)))