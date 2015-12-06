# https://www.hackerrank.com/challenges/utopian-tree
def height(n):
    h = 1
    for i in xrange(n):
        if i % 2:
            h += 1
        else:
            h *= 2
    return h

for i in xrange(input()):
    print height(input())