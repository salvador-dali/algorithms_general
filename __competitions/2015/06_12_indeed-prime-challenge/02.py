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

for i in xrange(1, input() + 1):
    N, R = map(int, raw_input().split())
    G = {i: set() for i in xrange(N)}
    for _ in xrange(R):
        v1, v2 = map(int, raw_input().split())
        G[v1].add(v2)
    
    r = topologicalSortLayers(G)
    if r == -1:
        print "Case " + str(i) + ": Never Ends"
    else:
        print "Case " + str(i) + ": " + str(len(r)) + " semester(s)"
