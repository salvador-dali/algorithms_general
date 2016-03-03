# https://www.interviewbit.com/problems/kth-permutation-sequence/
def permutation_k(n, k):
    permutations = [1]
    for i in xrange(1, n):
        permutations.append(permutations[-1] * i)

    representation = []
    for i in permutations[::-1]:
        val = k / i
        representation.append(val)
        k -= val * i

    res = []
    curr = range(1, n + 1)
    for i in representation:
        selected = curr[i]
        res.append(selected)
        curr = [el for el in curr if el != selected]

    return res