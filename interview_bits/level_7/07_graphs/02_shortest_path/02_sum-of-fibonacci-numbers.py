# https://www.interviewbit.com/problems/sum-of-fibonacci-numbers/
from bisect import bisect_right

def generate(n):
    arr = [1, 1]
    while arr[-1] <= n:
        arr.append(arr[-1] + arr[-2])

    return arr[:-1]

def present_as_fib(fibs, n):
    res = []
    while n:
        pos = bisect_right(fibs, n)
        res.append(fibs[pos - 1])
        n -= fibs[pos - 1]

    return len(res)

def result(n):
    fibs = generate(n)
    return present_as_fib(fibs, n)
