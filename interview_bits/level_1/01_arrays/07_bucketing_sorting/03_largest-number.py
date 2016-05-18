# https://www.interviewbit.com/problems/largest-number/
def comparison(s1, s2):
    return -1 if s1 + s2 > s2 + s1 else 1


def largest(arr):
    arr = map(str, arr)

    arr.sort(cmp=comparison)
    res = ''.join(arr)
    if res[0] == '0':
        return 0

    return res