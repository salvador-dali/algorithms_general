# https://www.interviewbit.com/problems/square-root-of-integer/
def sqrt(x):
    low, high = 0, x / 2 + 1
    while low <= high:
        middle = (low + high) / 2
        val = middle ** 2
        if val == x:
            return middle

        if val > x:
            high = middle - 1
        else:
            low = middle + 1

    return high

def newton(x):
    if x == 0:
        return 0
    res = x
    while True:
        res = res / 2. + x / 2. / res
        if abs(res**2 - x) < 0.01:
            return int(res)

