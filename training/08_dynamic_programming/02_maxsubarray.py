# https://www.hackerrank.com/challenges/maxsubarray
# find the length of the maximum subarray
def subarray(arr):
    s, m = 0, -10**9
    for i in arr:
        tmp = s + i
        if tmp > m:
            m = tmp

        if tmp >= 0:
            s = tmp
        else:
            s = 0

    return m

def non_continuous_subarray(arr):
    s, flag = 0, False
    for i in arr:
        if i >= 0:
            s += i
            flag = True

    if not flag:
        return max(arr)
    else:
        return s

for i in xrange(input()):
    input()
    arr = list(map(int, raw_input().split()))
    print subarray(arr), non_continuous_subarray(arr)