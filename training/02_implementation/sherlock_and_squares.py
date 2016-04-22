# https://www.hackerrank.com/challenges/sherlock-and-squares
import math

def numSquares(a, b):
    c = math.ceil(a**(1/2.0))
    num = 0
    while c ** 2 <= b:
        c += 1
        num += 1

    return num


for i in xrange(input()):
    a, b = map(int, raw_input().split())
    print numSquares(a, b)