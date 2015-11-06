# https://www.interviewbit.com/problems/stairs/
def fib(n):
    el1, el2 = 1, 2
    if n < 2:
        return 1

    for i in xrange(n - 2):
        el1, el2 = el2, el1 + el2

    return el2