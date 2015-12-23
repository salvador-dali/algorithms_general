N, Q = map(int, raw_input().split())
mod = 10**9 + 7
arr = [0] * N
for _ in xrange(Q):
    t, x, y = map(int, raw_input().split())
    x -= 1
    y -= 1
    if t == 1:
        for i in xrange(x, y + 1):
            arr[i] = (arr[i] + (i - x + 1) * (i - x + 2)) % mod
    else:
        print sum(arr[x:y+1]) % mod
