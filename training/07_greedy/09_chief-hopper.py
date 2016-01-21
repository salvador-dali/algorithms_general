# https://www.hackerrank.com/challenges/chief-hopper/
from math import ceil
def energy(arr):
    s, p = 0, 2.0
    for i in xrange(len(arr)):
        s += arr[i] / p
        p *= 2

    attempt = int(ceil(s))
    start = attempt
    for i in arr:
        start = 2 * start - i
        if start < 0:
            attempt += 1
            break

    return attempt

input()
print energy(list(map(float, raw_input().split())))