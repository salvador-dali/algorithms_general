from collections import defaultdict
from heapq import heappush, heappop

def dijkstra(graph, start, n):
    A = [None] * (n + 1)
    queue = [(0, start)]
    while queue:
        path_len, v = heappop(queue)
        if A[v] is None:
            A[v] = path_len
            for w, edge_len in graph[v].items():
                if A[w] is None:
                    heappush(queue, (path_len + edge_len, w))

    return [0 if x is None else x for x in A]

def attempt(graph, n):
    S = dijkstra(graph, 1, n)
    E = dijkstra(graph, n, n)

    a = S[-1] - 1
    print sum(max(0, a - S[i] - E[j]) + max(0, a - S[j] - E[i]) for i in xrange(1, n + 1) for j in xrange(i + 1, n + 1))

G = defaultdict(dict)
N, M = map(int, raw_input().split())
for _ in xrange(M):
    v1, v2, w = map(int, raw_input().split())
    if v2 in G[v1]:
        G[v1][v2] = min(G[v1][v2], w)
    else:
        G[v1][v2] = w

    if v1 in G[v2]:
        G[v2][v1] = min(G[v2][v1], w)
    else:
        G[v2][v1] = w

total = 0
v = dijkstra(G, 1, N)
attempt(G, N)