N, S, M = map(int, raw_input().split())
sets = [sorted(list(map(int, raw_input().split()))[1:]) for _ in xrange(S)]
arr = [0] * N
mod = 10**9 + 9
for _ in xrange(M):
    q = list(map(int, raw_input().split()))
    if q[0] == 1:
        currentSet = sets[q[1] - 1]
        for i in currentSet:
            arr[i - 1] += q[2]
    if q[0] == 2:
        currentSet = sets[q[1] - 1]
        print sum(arr[i - 1] for i in currentSet) % mod
    if q[0] == 3:
        for i in xrange(q[1] - 1, q[2]):
            arr[i] += q[3]
    if q[0] == 4:
        print sum(arr[q[1] - 1:q[2]]) % mod
