_, mod = map(int, raw_input().split())
arr = map(int, raw_input().split())

cnt = 0
for i in xrange(len(arr)):
    for j in xrange(i + 1, len(arr)):
        if (arr[i] + arr[j]) % mod == 0:
            cnt += 1

print cnt