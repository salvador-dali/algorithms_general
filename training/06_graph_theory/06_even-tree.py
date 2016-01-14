# you can remove the edge only if the number of connected components would be equal to 2
# and the number of edges in both connected components is even
# we need to count the number of such divisions
from collections import defaultdict

def createGraph(edges):
    graph = defaultdict(list)
    for v1, v2 in edges:
        graph[v1].append(v2)
        graph[v2].append(v1)

    return dict(graph)

def connectedComponents(G):
    unseen = set(G.keys())
    components = []

    while unseen:
        frontier = []
        for k in unseen:
            frontier.append(k)
            break

        component = []
        while frontier:
            element = frontier.pop()
            component.append(element)
            unseen.remove(element)
            for i in G[element]:
                if i in unseen:
                    frontier.append(i)

        components.append(component)
    return components

def getDivision(edges):
    r = 0
    for i in xrange(len(edges)):
        edgesAttempt = edges[:i] + edges[i + 1:]
        graph = createGraph(edgesAttempt)
        components = connectedComponents(graph)
        if len(components) > 1:
            if len(components[0]) % 2 == 0 and len(components[1]) % 2 == 0:
                r += 1

    return r

N, M = map(int, raw_input().split())
edges = [tuple(map(int, raw_input().split())) for i in xrange(M)]
print getDivision(edges)