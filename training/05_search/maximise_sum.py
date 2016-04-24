# https://www.hackerrank.com/challenges/maximise-sum
def maximum_sum_modulo(arr, mod):
    max_v, min_v, s = 0, mod, 0
    for i in xrange(len(arr)):
        s = (arr[i] + s) % mod
        max_v, arr[i] = max(max_v, s), (s, i)
    
    arr.sort(key=lambda x: (x[0], x[1]))
    print arr
    for i in xrange(len(arr) - 1):
        if arr[i][1] > arr[i + 1][1]:
            print arr[i + 1][0] - arr[i][0]
            min_v = min((arr[i + 1][0] - arr[i][0]) % mod, min_v)
    
    return max(max_v, mod - min_v)

for _ in xrange(input()):
    _, mod = map(int, raw_input().split())
    arr = map(int, raw_input().split())
    print maximum_sum_modulo(arr, mod)
