# https://www.hackerrank.com/challenges/pairs
# Given N integers, count the number of pairs of integers whose difference is K.
def pairs(arr, diff):
    h, num = {i : 1 for i in arr}, 0
    for i in arr:
        if (i + diff) in h:
            num += 1

    return num

n, k = map(int, raw_input().split())
arr = map(int, raw_input().split())
print pairs(arr, k)