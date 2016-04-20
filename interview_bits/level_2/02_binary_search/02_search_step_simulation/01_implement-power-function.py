# https://www.interviewbit.com/problems/implement-power-function/
def power(a, b, m):
    if a == 0:
        return 0

    res, mul = 1, a % m
    while b:
        if b % 2:
            res = (res * mul) % m
        mul = (mul * mul) % m
        b /= 2

    return res