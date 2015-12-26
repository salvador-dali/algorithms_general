from collections import defaultdict

def graph_set(G):
    G_, allVertices = {}, set()
    for i in G:
        G_[i] = set(G[i])
        allVertices.update(set(G[i]))

    for i in allVertices:
        if i not in G_:
            G_[i] = set()
    return G_

def createGraphList(points, dX, dY, H):
    def cp(point, max_x=20000000):
        return point[0] * max_x + point[1]

    G = {'S': [], 'E': []}
    for i in xrange(len(points)):
        p1 = points[i]
        G[cp(p1)] = []
        if p1[0] <= dY:
            G['S'].append((cp(p1), p1[2]))

        if H - p1[0] <= dY:
            G[cp(p1)].append(('E', 0))

    for i in xrange(len(points)):
        p1 = points[i]
        for j in xrange(i + 1, len(points)):
            p2 = points[j]
            if abs(p1[0] - p2[0]) <= dY and abs(p1[1] - p2[1]) <= dX:
                if p1[0] < p2[0]:
                    G[cp(p1)].append((cp(p2), p2[2]))
                elif p2[0] < p1[0]:
                    G[cp(p2)].append((cp(p1), p1[2]))

    return G

def createGraphDict(points, dX, dY, H):
    def convertPoint(point, max_x=20000000):
        return point[0] * max_x + point[1]

    G = defaultdict(dict)
    for i in xrange(len(points)):
        p1 = points[i]
        if p1[0] <= dY:
            G['S'][convertPoint(p1)] = p1[2]

        if H - p1[0] <= dY:
            G[convertPoint(p1)]['E'] = 0

    for i in xrange(len(points)):
        p1 = points[i]
        for j in xrange(i + 1, len(points)):
            p2 = points[j]
            if abs(p1[0] - p2[0]) <= dY and abs(p1[1] - p2[1]) <= dX:
                if p1[0] < p2[0]:
                    G[convertPoint(p1)][convertPoint(p2)] = p2[2]
                elif p2[0] < p1[0]:
                    G[convertPoint(p2)][convertPoint(p1)] = p1[2]

    return G

def topologicalSortLayers(graph):
    def reverseDirectedGraph(G):
        graph = defaultdict(list)
        for v1 in G:
            for v2 in G[v1]:
                graph[v2].append(v1)

        return dict(graph)

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

def longestPath(graph_dict, graph_list, startnode, endnode):
    order = []
    g = graph_set(graph_dict)
    for part in topologicalSortLayers(g):
        order.extend(list(part))

    order.reverse()

    dist = dict((x, -10**9) for x in graph_list.keys())
    dist[startnode] = 0

    comesFrom = {}
    for node in order:
        for nbr, nbrdist in graph_list[node]:
            if dist[nbr] < dist[node] + nbrdist:
                dist[nbr] = dist[node] + nbrdist
                comesFrom[nbr] = node

    return dist[endnode]

N, H, dH, dW = map(int, raw_input().split())
points = []
for _ in xrange(N):
    points.append(map(int, raw_input().split()))

G_list = createGraphList(points, dW, dH, H)
G_dict = createGraphDict(points, dW, dH, H)
print longestPath(G_dict, G_list, 'S', 'E')