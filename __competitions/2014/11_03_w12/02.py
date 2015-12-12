# https://www.hackerrank.com/contests/w12/challenges/chief-hopper
# if we have starting energy x and we jump on the building a
# our energy will be 2 * x - a
# This is enough to figure out that if after the a1, a2, ... an
# s = a1 * 2^(n -1) + a2 * 2 ^ (n - 2) + ... + an
# ceil(s / 2^ n)
# to decrease the number of the computations, after division we will get:
# a1/2 + a1/4 + ... + an/2^n
# then take the ceil to get the integer. This answer is correct if we have infinite precision.
# in case of computers, where this is not the case, we need to check whether the answer is correct
# (it can be of by 1) first for loop is O(n), second check is O(n). thus solution is O(n)
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