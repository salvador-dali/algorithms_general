# https://www.interviewbit.com/problems/subset/
def subset_original(arr):
    arr.sort()
    n, all_values = len(arr), []
    for val in xrange(pow(2, n)):
        tmp = ('{:0' + str(n) + 'b}').format(val)
        res = []
        for i in xrange(n):
            if tmp[i] == '1':
                res.append(arr[i])
        all_values.append(tuple(res))

    all_values.sort()
    return [list(i) for i in all_values]

def subset_fast(s):
    res = [[]]
    for e in s:
        res += [i + [e] for i in res]
    return res
