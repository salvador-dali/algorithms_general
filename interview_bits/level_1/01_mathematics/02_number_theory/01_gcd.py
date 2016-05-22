# https://www.interviewbit.com/problems/greatest-common-divisor/
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

