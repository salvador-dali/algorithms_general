# https://www.hackerrank.com/challenges/closest-numbers/
# Given a list of unsorted numbers, can you find the numbers that have the smallest absolute
# difference between them? If there are multiple pairs, find them all.
def closestNumbers(arr):
    arr.sort()
    smallestList, smallestDiff = [], 10**10

    for i in range(len(arr) - 1):
        diff = abs(arr[i] - arr[i + 1])
        if diff == smallestDiff:
            smallestList.extend([arr[i], arr[i + 1]])
        if diff < smallestDiff:
            smallestList = [arr[i], arr[i + 1]]
            smallestDiff = diff

    return smallestList

raw_input()
print ' '.join(map(str, closestNumbers(map(int, raw_input().split()))))