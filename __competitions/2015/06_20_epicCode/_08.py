from collections import defaultdict
from Queue import Queue

def update(tree, values, node, value):
    values[node] += value
    if node in tree:
        for node_new in tree[node]:
            update(tree, values, node_new, value)

def getSum(tree, values, node):
    global s
    s += values[node]
    if node in tree:
        for node_new in tree[node]:
            getSum(tree, values, node_new)

def graphFromEdges(edges):
    graph = defaultdict(list)
    for v1, v2 in edges:
        graph[v1].append(v2)
        graph[v2].append(v1)

    return dict(graph)

def createRootedTree(tree, root):
    rootedTree, frontier, checked = defaultdict(list), Queue(), {root}
    frontier.put(root)
    while not frontier.empty():
        v = frontier.get()
        for i in tree[v]:
            if i not in checked:
                rootedTree[v].append(i)
                checked.add(i)
                frontier.put(i)

    return dict(rootedTree)

def lowestCommonAncestor(tree, root, node1, node2):
    if node1 == node2:
        return node1

    frontier, checked, needToFind = [root], {root: 0}, {node1, node2}
    while frontier and len(needToFind):
        node = frontier.pop()
        if node in needToFind:
            needToFind.remove(node)

        if node in tree:
            for child in tree[node]:
                if child not in checked:
                    frontier.append(child)
                    checked[child] = node

    path1, path2 = [node1], [node2]
    while checked[node1]:
        node1 = checked[node1]
        path1.append(node1)

    while checked[node2]:
        node2 = checked[node2]
        path2.append(node2)

    l1, l2 = path1[::-1], path2[::-1]
    for i in xrange(min(len(l1), len(l2))):
        if l1[i] != l2[i]:
            return l1[i - 1]

    return l1[i]

def reverseDirectedGraph(G):
    graph = defaultdict(list)
    for v1 in G:
        for v2 in G[v1]:
            graph[v2] = v1

    return dict(graph)

def getPath(reversedTree, n1, n2, ancestor):
    path = set([n1, n2])
    while n1 != ancestor:
        n1 = reversedTree[n1]
        path.add(n1)

    while n2 != ancestor:
        n2 = reversedTree[n2]
        path.add(n2)
    return path

N = input()
edges = [tuple(map(int, raw_input().split())) for _ in xrange(N - 1)]
tree = createRootedTree(graphFromEdges(edges), 1)
reversedTree = reverseDirectedGraph(tree)
values = {i: 0 for i in xrange(1, N+1)}

for i in xrange(input()):
    q = map(int, raw_input().split())
    if q[0] == 1:
        ancestor = lowestCommonAncestor(tree, 1, q[1], q[2])
        path = getPath(reversedTree, q[1], q[2], ancestor)
        for i in path:
            update(tree, values, i, q[3])
    else:
        s = 0
        getSum(tree, values, q[1])
        print s % 10009