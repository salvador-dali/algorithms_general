"""
https://www.hackerrank.com/contests/w18/challenges/rhombographs
After first look at the problem it was obvious that this should be some sort of specific class
of graphs. Sadly enough I was not able to construct a graph for any input (no matter how small).

After a couple of minutes I realized that their phrase that any A, B should be connected
through intermediate vertices C, D sounds really similar to how the rook moves on a chess board

 xxxOxx
 xxxxxx
 xxxxxx
 xOxxxx

Now it was easy to calculate the number of vertices and edges. So I was able to connect `m` and `n`
with number of edges and with the degree. That gave me ability to find out when the graph can not
be constructed and what type of `n` `m` should be used for the input.

Knowing `n` and `m` it is easy to construct a graph using chess board example.
P.S. after competition I found out that this is http://mathworld.wolfram.com/LatticeGraph.html

"""

def isConstructed(N, M, X):
    have_found, n = False, 1
    while not have_found:
        tmp = n * (X + 2) - n*n
        if N <= tmp <= M:
            m = X - n + 2
            if m >= 1:
                have_found = True
                break

        if tmp < 0:
            break

        n += 1

    if have_found:
        return True, n, m

    return False, 0, 0

def construct(ok, n, m):
    if not ok:
        print -1, -1
        return

    print n * m, n * m * (m + n) / 2 - m * n
    for i in xrange(n):
        for j in xrange(m):
            v = i * m + j + 1
            for k in xrange(j + 1, m):
                print v, i * m + k + 1
            for k in xrange(i + 1, n):
                print v, j + 1 + m * k

# N, M, X = map(int, raw_input().split())
N, M, X = 1, 4, 2
# N, M, X = 3, 6, 3
# N, M, X = 5, 12, 8
ok, n, m = isConstructed(N, M, X)
construct(ok, n, m)











