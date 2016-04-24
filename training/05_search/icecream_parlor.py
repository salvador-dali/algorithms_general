# https://www.hackerrank.com/challenges/icecream-parlor
def sumInList(s, arr):
    l = len(arr)
    # this is if we want to find the smallest index
    h = {arr[l - i - 1]: l - i - 1 for i in range(l)}
    for i in range(l):
        if (s - arr[i]) in h and i != h[s - arr[i]]:
            if i < h[s - arr[i]]:
                return i, h[s - arr[i]]
            else:
                return h[s - arr[i]], i

    return -1

for i in xrange(int(raw_input())):
    s = int(raw_input())
    raw_input()
    arr = list(map(int, raw_input().split()))

    indexes = sumInList(s, arr)
    print indexes[0] + 1, indexes[1] + 1