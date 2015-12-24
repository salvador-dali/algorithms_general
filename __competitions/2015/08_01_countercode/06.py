class Problem():
    def __init__(self):
        self.arr = [0] * 2**16

    def add(self, s):
        for i in xrange(256):
            if i & s == 0:
                self.arr[s | i] += 1

    def delete(self, s):
        for i in xrange(256):
            if i & s == 0:
                self.arr[s | i] -= 1

    def cnt(self, s):
        res = 0
        for i in xrange(256):
            if s | (i * 256) == s:
                res += self.arr[s & (- i * 256 - 1)]
        print res
        
a = Problem()
for i in xrange(input()):
    verb, n = raw_input().split()
    if verb == 'add':
        a.add(int(n))
    elif verb == 'del':
        a.delete(int(n))
    elif verb == 'cnt':
        a.cnt(int(n))