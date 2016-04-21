# https://www.interviewbit.com/problems/rotated-array/
def bs(num, st, ed, res):
    if st > ed:
        return res
    else:
        mid = st + (ed - st)/2
        if num[mid] < num[ed]:
            res = min(res, num[mid])
            return bs(num, st, mid-1, res)
        else:
            res = min(res, num[st])
            return bs(num, mid+1, ed, res)
