_, p, x = map(int, raw_input().split())
arr = list(map(int, raw_input().split()))

print max(((arr[i] * (p - i * x), i) for i in xrange(len(arr))))[1] + 1