# https://www.interviewbit.com/problems/verify-prime/
def isPrime(n):
    if n == 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    for i in xrange(3, int(n**0.5) + 3, 2):
        if n % i == 0:
            return False

    return True
