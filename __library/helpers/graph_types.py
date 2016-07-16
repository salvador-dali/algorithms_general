# various graph types implementation

def constructLatticeGraph(n, m):
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
    edges = []
    for i in xrange(n):
        for j in xrange(m):
            v = i * m + j + 1
            for k in xrange(j + 1, m):
                edges.append((v, i * m + k + 1))
            for k in xrange(i + 1, n):
                edges.append((v, j + 1 + m * k))

    return edges










