# https://www.hackerrank.com/challenges/sherlock-and-the-beast
def number(n):
    numOf3 = 5 * (2 * n % 3)
    if numOf3 > n:
        return -1
    else:
        return '5' * (n - numOf3) + '3' * numOf3

for i in xrange(input()):
    print number(input())