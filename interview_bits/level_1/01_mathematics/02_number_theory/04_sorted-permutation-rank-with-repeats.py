# https://www.interviewbit.com/problems/sorted-permutation-rank-with-repeats/
from collections import Counter
mod = 1000003

def rankperm(perm):
    # http://stackoverflow.com/a/22643546/1090562
    rank, suffix_perms, n = 1, 1, len(perm)
    ctr = Counter()
    for i in range(n):
        x = perm[((n - 1) - i)]
        ctr[x] += 1

        inv = pow(ctr[x], mod - 2, mod)
        for y in ctr:
            if y < x:
                rank = (rank + suffix_perms * ctr[y] * inv) % mod

        suffix_perms = (suffix_perms * (i + 1) * inv) % mod
    return rank