# https://www.interviewbit.com/problems/2-sum/

from collections import defaultdict
def two_sum(arr, target):
    hash = defaultdict(list)
    for i in xrange(len(arr)):
        hash[arr[i]].append(i)

    solutions, minimum = [], float('inf')
    for i in xrange(len(arr)):
        tmp = target - arr[i]
        if tmp in hash:
            for val in hash[tmp]:
                if i == val:
                    break
                m = max(i, val)

                s1, s2 = min(i, val), max(i, val)
                if m < minimum:
                    solutions = [(s1, s2)]
                    minimum = m
                elif m == minimum:
                    solutions.append((s1, s2))
    solutions.sort()
    if len(solutions):
        return [solutions[0][0] + 1, solutions[0][1] + 1]
    return []
