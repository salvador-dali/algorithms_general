from collections import defaultdict
from Queue import PriorityQueue

def undirectedGraphFromEdges(edges):
    """
    constructs a dictionary graph from the list of bidirectional edges (weighted or not)
    O(n) in terms of the number of edges.
    does not handle empty edges

    :param edges:   list of edges where each edge either (v1, v2) or (v1, v2, w)
                    edges = [('a', 'b', 1), ('a', 'd', 5), ('b', 'd', 2), ('b', 'c', 3), ('c', 'd', 4)]
    :return:
    """
    graph = defaultdict(list)

    if len(edges[0]) == 3:  # means that this is a weighted graph
        for v1, v2, w in edges:
            graph[v1].append((v2, w))
            graph[v2].append((v1, w))
    else:
        for v1, v2 in edges:
            graph[v1].append(v2)
            graph[v2].append(v1)

    return dict(graph)

def MST_prim(graph):
    """
    for a directed graph, finds a minimum spanning tree, using Prim's algorithm
    The main idea is the following:
    take any vertex and start growing a spanning tree in such a way,
    that each time we are taking the vertex with the smallest edge which. An edge
    should be between between some vertex in the frontier and unseen vertex

    To find maximum spanning tree one have to multiply each edge by -1 and run MST
    :param graph:   weighted graph
    :return: total weight of the MST and one of the possible MST as a list of edges
    """
    for start in graph:
        break

    added, MST, frontier, total = {start}, [], PriorityQueue(), 0
    for v1, w in graph[start]:
        frontier.put((w, start, v1))

    while not frontier.empty():
        w, v1, v2 = frontier.get()
        if v2 not in added:
            total += w
            added.add(v2)
            MST.append((v1, v2))
            for v1, w in graph[v2]:
                frontier.put((w, v2, v1))

    return total, MST

def MST_kruskal(graph):
    """
    finds a minimum spanning tree using Kruskal algorithm
    The main idea for the Kruskal algorithm is to sort all edges based on their cost and then
    starting with the cheapest and expand the MST by adding each edge that does not form a cycle

    This second thing better implemented with union-find data structure,
    :param graph:
    :return:
    """
    return 1

def reverseDirectedGraph(G):
    """Reverse the edges in the directed graph
    :param G:
    :return: reversed graph
    """
    graph = defaultdict(list)
    for v1 in G:
        for v2 in G[v1]:
            graph[v2].append(v1)

    return dict(graph)

def topologicalSortLayers(graph):
    # https://www.hackerrank.com/contests/indeed-prime-challenge/challenges/course-dilemma
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

def num_cycles_length_4(G):
    # calculates the number of different cycles of length 4. 2 times faster than my implementation
    # https://www.hackerrank.com/contests/w20/challenges/cat-jogging
    # G - should be defaultdict
    res, seen = 0, set()
    for k, v in G.iteritems():
        d = defaultdict(int)
        for x in v:
            if x not in seen:
                for y in G[x]:
                    if y not in seen:
                        d[y] += 1

        res += sum(c * (c - 1) for node, c in d.iteritems() if node != k)
        seen.add(k)

    return res / 2