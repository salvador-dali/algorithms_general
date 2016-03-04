# https://www.hackerrank.com/challenges/crush
a, b = map(int, raw_input())
arr = [0] * (a + 1)     # initialize empty array

for i in xrange(b):
    n, m, k = map(int, raw_input())
    # save only mark start and end + 1 element
    arr[n - 1] += k
    arr[m] += -k

s, maximum = 0, 0
for i in xrange(len(arr)):
    arr[i], s = arr[i] + s, s + arr[i]
    if arr[i] > maximum:
        maximum = arr[i]


print maximum

