"""
https://www.hackerrank.com/contests/w18/challenges/target
Read the array of circles `r`, sort them
Read the points, calculate the radius for each of them using pythagorean and sort them as well.

Using binary search find where each of the elements belongs to

Fully solved
"""

from math import hypot
from bisect import bisect_left

K, N = map(int, raw_input().split())
r = map(int, raw_input().split())
p = [(lambda x: hypot(x[0], x[1]))(map(int, raw_input().split())) for _ in xrange(N)]

p.sort()
r.sort()

print sum(K - bisect_left(r, i) for i in p)
