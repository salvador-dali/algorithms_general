# https://www.hackerrank.com/contests/w14/challenges/number-list
def numbersBigger(arr, k):
    """
    Just a bruteforce solution to test correctness of my solution
    :param arr:
    :param k:
    :return:
    """
    bigList = []
    for i in xrange(len(arr)):
        bigList.extend([arr[j: j + i + 1] for j in xrange(len(arr) - i)])

    total = 0
    for i in bigList:
        total += int(max(i) > k)

    return total

def test():
    """
    Just tests to figure out whether the answer is correct.
    Runs brute force together with optimal algorithm and check whether the answer is correct
    :return:
    """
    from random import randint
    for i in xrange(1000):
        arr, k = [int(randint(2, 10000)) for i in xrange(randint(50, 100))], randint(2, 10000)
        if numbersBigger(arr, k) != numSubarraysMaxBiggerThenK(arr, k):
            print k, arr

def numSubarraysMaxBiggerThenK(arr, k):
    """
    Find the number of contiguous sub-arrays, where maximum value is bigger then k

    Notice that this is the same as find the number of contiguous sub-arrays,
    in the array of 0 and 1 where there is 1. For example:
    [0, 0, 1, 0, 0, 0].
    Using combinatorics, one can find that the answer is 3 * 4 (3 elements before the 1 with one)
    and (4 elements after 1 with 1).

    Every array can be divided in this arrays. For example
    [0, 0, 1, 0, 0, 0, 1, 1, 0, 1].
    here it is 3 * 8 + 4 * 4 + 1 * 3 + 2 * 1. Notice that we are counting from the last 1 element
    :param arr:
    :param k:
    :return:
    """
    lastLeft, total, l = 0, 0, len(arr)
    for i in xrange(l):
        if arr[i] > k:
            total += (i + 1 - lastLeft) * (l - i)
            lastLeft = i + 1

    return total

for i in xrange(input()):
    a, k = map(int, raw_input().split())
    print numSubarraysMaxBiggerThenK(list(map(int, raw_input().split())), k)