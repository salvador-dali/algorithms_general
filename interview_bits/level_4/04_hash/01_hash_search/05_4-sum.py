# https://www.interviewbit.com/problems/4-sum/

from collections import defaultdict
def sum_4(arr, target):
    h, n = defaultdict(list), len(arr)
    for i in xrange(n):
        for j in xrange(i + 1, n):
            h[arr[i] + arr[j]].append((i, j))

    all_res = set([])
    for i in xrange(n):
        for j in xrange(i + 1, n):
            look_for = target - arr[i] - arr[j]
            for i1, j1 in h[look_for]:
                if len(set([i, j, i1, j1])) == 4:
                    candidate = [arr[i], arr[j], arr[i1], arr[j1]]
                    candidate.sort()
                    all_res.add(tuple(candidate))

    all_res = list(all_res)
    all_res.sort()
    return all_res
