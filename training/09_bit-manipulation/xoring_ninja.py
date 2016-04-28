# https://www.hackerrank.com/challenges/xoring-ninja
# sum of all xor subsets will be equal to
# having an OR of all elements and multiply it by
# 2^(len(arr) - 1)
def xorSubsets(arr):
    return reduce(lambda x, y: x | y, arr) * (2**(len(arr) - 1))

for i in xrange(input()):
    input()
    print xorSubsets(map(int, raw_input())) % (10**9 + 7)