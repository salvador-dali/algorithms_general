# https://www.interviewbit.com/problems/permutations/
from math import factorial

def next_permutation(arr):
    for i in xrange(len(arr) - 1, 0, -1):
        if arr[i] > arr[i - 1]:
            break

    will_change = arr[i - 1]
    bigger = min(el for el in arr[i:] if el > will_change)

    last = [el for el in arr[i:] if el != bigger] + [will_change]
    last.sort()
    return arr[:i - 1] + [bigger] + last

def all_permutations(arr):
    res = []
    for i in xrange(factorial(len(arr)) - 1):
        res.append(arr)
        arr = next_permutation(arr)
    res.append(arr)
    return res


# previous was my own implementation. This one I have learned from
# https://en.wikipedia.org/wiki/Steinhaus%E2%80%93Johnson%E2%80%93Trotter_algorithm
def generate_permutations(arr):
    permutations, pos = [[]], 0

    for pos in xrange(len(arr)):
        curr_el, res = arr[pos], []
        for perm in permutations:
            for p in xrange(len(perm) + 1):
                res.append(perm[:p] + [curr_el] + perm[p:])
        permutations = res

    return permutations
