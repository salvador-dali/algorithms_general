from collections import defaultdict, deque

def undirectedGraphFromEdges(edges):
    graph = defaultdict(list)
    for v1, v2 in edges:
        graph[v1].append(v2)
        graph[v2].append(v1)

    return dict(graph)

def areVerticesConnected(graph, vertices):
    q, connected = deque(), set()
    for v in vertices:
        q.append(v)
        break

    while len(q):
        v = q.pop()
        connected.add(v)
        neighbors = graph[v]
        for i in neighbors:
            if i not in connected and i in vertices:
                q.append(i)

    return len(connected) == len(vertices)

def knapsackBrute(items, graph, m):
    maximum = 0
    for i in xrange(pow(2, len(items))):
        s = ('0' * len(items) + bin(i)[2:])[-len(items):]
        selected = [items[i] for i in xrange(len(s)) if s[i] == '1']
        weight = sum([i[1] for i in selected])

        if weight <= m:
            vertices = set(i[0] for i in selected)
            if areVerticesConnected(graph, vertices):
                maximum = max(maximum, sum([i[2] for i in selected]))

    print maximum

for i in xrange(input()):
    n, m = map(int, raw_input().split())
    S = list(map(int, raw_input().split()))
    V = list(map(int, raw_input().split()))
    edges = [map(int, raw_input().split()) for i in xrange(n - 1)]
    items = [(j + 1, S[j], V[j]) for j in xrange(len(S))]
    graph = undirectedGraphFromEdges(edges)
    knapsackBrute(items, graph, m)