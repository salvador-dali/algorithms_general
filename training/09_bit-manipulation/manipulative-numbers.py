from itertools import permutations

def xor(arr):
    res = min(arr[i] ^ arr[i + 1] for i in xrange(len(arr) - 1))
    return min(arr[0] ^ arr[-1], res)

def minimum(arr):
    for el in permutations(arr):
        print el, xor(el)

arr = [13, 3, 10]
minimum(arr)