# https://www.interviewbit.com/problems/equal/
arr = [3, 4, 7, 1, 2, 9, 8]

from collections import defaultdict
def equal(arr):
    h, n = defaultdict(list), len(arr)
    for i in xrange(n):
        for j in xrange(i + 1, n):
            h[arr[i] + arr[j]].append((i, j))

    for i in xrange(n):
        for j in xrange(i + 1, n):
            for i1, j1 in h[arr[i] + arr[j]]:
                if len({i1, j1, i, j}) == 4:
                    res = [(i1, j1), (i, j)]
                    res.sort()
                    return [res[0][0], res[0][1], res[1][0], res[1][1]]

    return []
