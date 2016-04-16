# https://www.interviewbit.com/problems/single-number/
def getElement(arr):
    res = 0
    for i in arr:
        res ^= i

    return res

