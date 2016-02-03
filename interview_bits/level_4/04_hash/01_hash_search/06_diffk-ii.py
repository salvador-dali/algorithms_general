# https://www.interviewbit.com/problems/diffk-ii/
arr = [1, 5, 3]
target = 2

from collections import defaultdict
def diff_k(arr, target):
    h = defaultdict(list)
    for i in xrange(len(arr)):
        h[arr[i]].append(i)

    for i in xrange(len(arr)):
        for j in h[arr[i] + target]:
            if i != j:
                return True

    return False

print diff_k(arr, target)