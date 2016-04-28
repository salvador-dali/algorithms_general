# https://www.hackerrank.com/challenges/maximizing-xor
def maxXor(l, r):
    return 2**(len(bin(r ^ l)) - 2) - 1

print maxXor(input(), input())

