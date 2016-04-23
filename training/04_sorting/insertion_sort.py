# https://www.hackerrank.com/challenges/insertion-sort/
class BinaryIndexedTree():
    def __init__(self, size):
        self.size = size
        self.tree = [0] * size

    def update(self, idx, val):
        while idx <= self.size:
            self.tree[idx] += val
            idx += (idx & -idx)

    def read(self, idx):
        sum = 0
        while idx > 0:
            sum += self.tree[idx]
            idx -= (idx & -idx)
        return sum

for _ in xrange(input()):
    n, cnt = input(), 0
    bit = BinaryIndexedTree(10**7+1)
    for val in reversed(map(int, raw_input().split())):
        bit.update(val, 1)
        cnt += bit.read(val-1)
    print cnt