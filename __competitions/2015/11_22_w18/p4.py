"""
https://www.hackerrank.com/contests/w18/challenges/two-centers
went astray by thinking that I can select a point on a tree, divide a tree into two parts
and calculate the diameter of both parts in O(n). Try each division point and select the one that
gives the smallest diameter. The problem was that a point can divide a tree in more than 2 parts.

The best I was able to come up with is O(V^3) implementation where I try all pairs of nodes and for
each of them calculate the shortest distances to them.


Now I see how pathetic I was. There is no point to check all the vertices, only the edges of the graph
"""

from collections import defaultdict
def readGraph():
    graph = defaultdict(list)
    for _ in xrange(input() - 1):
        v1, v2 = map(int, raw_input().split())
        graph[v1].append(v2)
        graph[v2].append(v1)
    return graph

def getDistances(tree, root):
    frontier, distances = [root], {root: 0}
    while frontier:
        node = frontier.pop()
        for child in tree[node]:
            if child not in distances:
                frontier.append(child)
                distances[child] = distances[node] + 1

    return distances

def get2distances(tree):
    nodes, arr = list(tree), []
    for i in xrange(len(nodes)):
        for j in xrange(i + 1, len(nodes)):
            dist1 = getDistances(tree, nodes[i])
            dist2 = getDistances(tree, nodes[j])
            arr.append(max(min(v, dist2[k]) for k, v in dist1.iteritems()))

    return min(arr)

tree = {1: {2}, 2: {1, 3}, 3: {2, 4}, 4: {3, 5}, 5: {4} }
print get2distances(tree)
