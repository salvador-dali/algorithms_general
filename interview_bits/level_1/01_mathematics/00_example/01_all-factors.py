# https://www.interviewbit.com/problems/all-factors/
def getFactors(n):
    small, big = [], []
    for i in xrange(1, int(n**0.5) + 1):
        if n % i == 0:
            small.append(i)
            big.append(n / i)

    if small[-1] == big[-1]:
        return small[:-1] + big[::-1]

    return small + big[::-1]

