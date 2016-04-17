# https://www.interviewbit.com/problems/divide-integers/
def divide(a, b):
    if a == 0:
        return 0
    sign = (-1 if a < 0 else 1) * (-1 if b < 0 else 1)
    a, b = abs(a), abs(b)
    if b == 1:
        return a * sign


