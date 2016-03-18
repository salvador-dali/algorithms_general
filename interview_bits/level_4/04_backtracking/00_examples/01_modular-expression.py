# https://www.interviewbit.com/problems/modular-expression/
def power(a, b, m):
    if m == 1:
        return 0
    if b == 0:
        return 1
    a = a % m
    curr, res = a, 1
    while b:
        if b % 2:
            res = (res * curr) % m
        b /= 2
        curr = (curr * curr) % m
    return res