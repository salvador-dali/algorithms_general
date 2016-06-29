from collections import defaultdict
def readGraph(m):
    graph = defaultdict(set)
    for i in xrange(m):
        v1, v2 = map(int, raw_input().split())
        graph[v1].add(v2)
        graph[v2].add(v1)

    return graph

def num_cycles_length_4(G):
    s = 0
    for node in G:
        if len(G[node]) > 1:
            d = defaultdict(int)
            for i in G[node]:
                for j in G[i]:
                    if node != j:
                        d[j] += 1

            s += sum(d[k] * (d[k] - 1) for k in d)

    return s / 8

n, m = map(int, raw_input().split())
print num_cycles_length_4(readGraph(m))