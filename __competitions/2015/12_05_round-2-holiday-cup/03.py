from collections import defaultdict
def readGraph():
    graph = defaultdict(set)
    for i in xrange(input() - 1):
        v1, v2 = map(int, raw_input().split())
        graph[v1].add(v2)
        graph[v2].add(v1)
        
    return dict(graph)

def dfs(graph, start):
    visited, frontier, colors = set([]), [(start, True)], [0, 0]
    while frontier:
        vertex, color = frontier.pop()
        colors[int(color)] += 1
        if vertex not in visited:
            visited.add(vertex)
            for i in graph[vertex] - visited:
                frontier.append((i, not color))

    return colors[0] * (colors[0] - 1) / 2 + colors[1] * (colors[1] - 1) / 2
    

for i in xrange(input()):
    tree = readGraph()
    print dfs(tree, 1)