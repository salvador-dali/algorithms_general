# https://www.interviewbit.com/problems/flip/
def flip(s):
    l = [1 if i == '0' else -1 for i in s]
    best = cur = 0
    curi = starti = besti = 0
    for ind, i in enumerate(l):
        if cur+i >= 0:
            cur += i
        else:
            cur, curi = 0, ind+1

        if cur > best:
            starti, besti, best = curi, ind + 1, cur

    if starti == besti:
        return []
    return [starti + 1, besti]