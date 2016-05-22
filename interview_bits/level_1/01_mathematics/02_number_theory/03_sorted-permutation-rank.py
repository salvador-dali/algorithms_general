# https://www.interviewbit.com/problems/sorted-permutation-rank/
def posOfPermutation(s):
    arr = [i for i in s]
    arr.sort()
    h = {arr[i]:i for i in xrange(len(arr))}
    arr = [h[i] for i in s]

    f = [1]
    for i in xrange(2, len(arr)):
        f.append((f[-1] * i) % 1000003)
    f = f[::-1]


    val = 0
    for i in xrange(len(arr) - 1):
        curr = arr[i]
        val = (val + f[i] * sum(1 for _ in arr[i + 1:] if _ < curr)) % 1000003
    return (val + 1) % 1000003