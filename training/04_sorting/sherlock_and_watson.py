# https://www.hackerrank.com/challenges/sherlock-and-watson
N, K, Q = map(int, raw_input().split())
arr = list(map(int, raw_input().split()))

K = - (K % len(arr))

for i in range(Q):
    print arr[K + int(raw_input())]