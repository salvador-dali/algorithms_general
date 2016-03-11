# https://www.interviewbit.com/problems/subsets-ii/
def subset(arr):
    res = [[]]
    for i in arr:
        res += [r + [i] for r in res]

    res = list({tuple(sorted(i)) for i in res})
    res.sort()
    return [list(i) for i in res]
