# https://www.interviewbit.com/problems/single-number-ii/
# http://stackoverflow.com/a/7338465/1090562

def onlyOnce(arr):
    e1, e2 = 0, 0
    for i in arr:
        e1 = (e1 ^ i) & ~e2
        e2 = (e2 ^ i) & ~e1
    return e1