# https://www.hackerrank.com/challenges/benders-play

from collections import defaultdict

def reverseDirectedGraph(G):
    graph = defaultdict(list)
    for v1 in G:
        for v2 in G[v1]:
            graph[v2].append(v1)

    return dict(graph)

def topologicalSortLayers(graph):
    if not graph:
        return []

    frontier = [k for k, v in graph.iteritems() if not v]
    if not frontier:
        return -1

    graph_r, frontier_waiting, layers = reverseDirectedGraph(graph), [], []
    while frontier:
        layers.append(frontier[:])
        for i in frontier:
            del graph[i]
            if i in graph_r:
                for v in graph_r[i]:
                    graph[v].remove(i)
                    if not graph[v]:
                        frontier_waiting.append(v)
        frontier, frontier_waiting = frontier_waiting[:], []

    if graph:
        return -1

    return layers

def readGraph():
    G = defaultdict(list)
    N, M = map(int, raw_input().split())
    for i in xrange(M):
        v1, v2 = map(int, raw_input().split())
        G[v1].append(v2)
        if v2 not in G:
            G[v2] = []

    return dict(G)

def mex(arr):
    d, i = set(arr), 0
    while i in d:
        i += 1

    return i

def grundyValues(G):
    G_copy, grundy = {v: G[v][::] for v in G}, {}
    for layer in topologicalSortLayers(G_copy):
        for val in layer:
            grundy[val] = mex([grundy[z] for z in G[val]])

    return grundy

def analyze(grundy, arr):
    res = 0
    for i in arr:
        if i in grundy:
            res ^= grundy[i]
    
    return res != 0

G = readGraph()
grundy = grundyValues(G)
for _ in xrange(input()):
    tmp, arr = input(), map(int, raw_input().split())
    if analyze(grundy, arr):
        print "Bumi"
    else:
        print "Iroh"