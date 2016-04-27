# https://www.hackerrank.com/challenges/red-john-is-back
def numOfPossibilities(n):
    arr = [1, 1, 1, 2]
    if n < 5:
        return arr[n - 1]

    i, num = 0, n - 4
    while i < num:
        arr.append(arr[-1] + arr[-4])
        i += 1

    return arr[-1]

# Sieve of Eratosthenes
# http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
def sieve(n):
    import math
    nums = [1] * (n + 1)
    nums[:2] = [0] * 2
    nums[4::2] = [0] * int(math.ceil((n - 3) / 2.0))
    for i in range(3, int((n + 1)**.5) + 1, 2):
        if nums[i]:
            for j in range(i*i, n+1, 2*i):
                nums[j] = 0

    return [i for i, k in enumerate(nums) if k]


for i in xrange(input()):
    print len(sieve(numOfPossibilities(input())))