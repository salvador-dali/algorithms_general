# https://www.hackerrank.com/contests/worldcodesprint/challenges/powerplants-in-flatland/
n, _ = map(int, raw_input().split())
arr = map(int, raw_input().split(' '))

arr.sort()
m = 0
if len(arr) == 1:
    m = max(arr[0], n - 1 - arr[0])
if len(arr) > 1:
    m = max((j - i) / 2 for i, j in zip(arr, arr[1:]))
    m = max(m, arr[0], n - 1 - arr[-1])

print m
