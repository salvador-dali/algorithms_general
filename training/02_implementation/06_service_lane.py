# https://www.hackerrank.com/challenges/service-lane
num = map(int, raw_input().split())[1]
arr = list(map(int, raw_input().split()))

for k in range(num):
    i, j = map(int, raw_input().split())
    print min(arr[e] for e in range(i, j+1))