def findNum(n, arr):
    arr.sort()
    total = (arr[0] - 1) / 2 + len(arr)
    for i in xrange(1, len(arr)):
        total += (arr[i] - arr[i - 1] - 2) / 2

    total += (n - arr[-1]) / 2
    return total

n, k = map(int, raw_input().split())
arr = list(map(int, raw_input().split()))
print findNum(n, arr)