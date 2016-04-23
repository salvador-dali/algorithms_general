# https://www.hackerrank.com/challenges/runningtime
m, arr, num = input(), map(int, raw_input().split()), 0
for j in range(1, len(arr)):
    key = arr[j]
    i = j
    while i > 0 and key < arr[i-1]:
        arr[i] = arr[i-1]
        i -= 1
        arr[i] = key
        num += 1

print num