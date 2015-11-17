# https://www.interviewbit.com/problems/distribute-candy/
def part(arr):
    curr, prev, res = 0, float('-inf'), [0] * len(arr)
    for i in xrange(len(arr)):
        curr = curr + 1 if arr[i] > prev else 1
        res[i], prev = curr, arr[i]

    return res

def solution(arr):
    r1, r2 = part(arr), part(arr[::-1])
    return sum(max(i) for i in zip(r1, r2[::-1]))

