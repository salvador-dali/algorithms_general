n, q = map(int, raw_input().split())
arr = list(map(int, raw_input().split()))

arr2 = [arr[0] % 2]
for i in xrange(1, len(arr)):
    arr2.append((arr2[i - 1] + arr[i]) % 2)

for i in xrange(q):
    l, r = map(int, raw_input().split())
    s = arr2[r - 1]
    if l - 1 == 0:
        s += 0
    else:
        s += arr2[l - 2]

    print "Odd" if s % 2 else "Even"