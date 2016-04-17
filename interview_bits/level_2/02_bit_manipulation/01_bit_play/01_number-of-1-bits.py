# https://www.interviewbit.com/problems/number-of-1-bits/
def getNumberOfBits(n):
    num = 0
    while n:
        num += n % 2
        n /= 2

    return num
