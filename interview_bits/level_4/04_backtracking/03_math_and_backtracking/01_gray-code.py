# https://www.interviewbit.com/problems/gray-code/

def generateGrey(n):
    start, cur_n, mul = [0, 1], 1, 2
    if n == 1:
        return start

    while n != cur_n:
        start = start + [i + mul for i in start[::-1]]
        cur_n, mul = cur_n + 1, mul * 2
    return start

def generateGreyFaster(n):
    return [i ^ (i / 2) for i in xrange(2**n)]







