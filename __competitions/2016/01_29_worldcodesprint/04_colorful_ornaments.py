# https://www.hackerrank.com/contests/worldcodesprint/challenges/colorful-ornaments
import sys
sys.setrecursionlimit(100000000)

x00, x01, x11, x10 = map(int, raw_input().split())
A, B, C, D = x00, x01, x10, x11

def S0(a, b, c, d):
    if a < 0 or b < 0 or c < 0 or d < 0:
        return 0
    if a == 0 and b == 0 and c == 0 and d == 0:
        return 1

    return S0(a - 1, b, c, d) + S1(a, b - 1, c, d)

def S1(a, b, c, d):
    if a < 0 or b < 0 or c < 0 or d < 0:
        return 0
    if a == 0 and b == 0 and c == 0 and d == 0:
        return 1

    return S0(a, b, c - 1, d) + S1(a, b, c, d - 1)

print S0(A, B, C, D) + S1(A, B, C, D)