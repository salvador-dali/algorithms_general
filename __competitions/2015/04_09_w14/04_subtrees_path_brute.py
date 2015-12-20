from collections import defaultdict
from Queue import Queue

"""
I was not able to come up with appropriate method, so it is just a brute force
Basically creates a tree, then for every query it either
- find the path and checks the maximum
- or updates all the elements
"""

def createTreeFromEdges(edges):
    tree = defaultdict(list)
    for v1, v2 in edges:
        tree[v1].append(v2)
        tree[v2].append(v1)

    return dict(tree)

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

def updateSubtree(rTree, root, num, weightsHash):
    frontier = [root]
    while frontier:
        el = frontier.pop()
        weightsHash[el] += num
        if el in rTree:
            frontier.extend(rTree[el])

def findMax(tree, root, node1, node2, weightsHash):
    if node1 == node2:
        return weightsHash[node1]

    frontier = [root]
    checked = {root: 0}
    needToFind = {node1, node2}
    while frontier and len(needToFind):
        node = frontier.pop()
        if node in needToFind:
            needToFind.remove(node)

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
        if l1[i] == l2[i]:
            last = l1[i]

    s = (set(path1 + path2) - (set(path1) & set(path2))) | {last}
    return max(weightsHash[i] for i in s)

def makeUpdates(updates):
    for verb, n1, n2 in updates:
        if verb == 'add':
            if n2:
                updateSubtree(rootedTree, n1, n2, weights)
        else:
            findMax(tree, 1, n1, n2, weights)

N = input()
edges = [list(map(int, raw_input().split())) for _ in xrange(N - 1)]
tree = createTreeFromEdges(edges)
if len(edges):
    tree = createTreeFromEdges(edges)
else:
    tree = {1: []}
rootedTree = createRootedTree(tree, 1)
weights = {i: 0 for i in xrange(1, N + 5)}
updates = []
for i in xrange(input()):
    a, b, c = raw_input().split()
    updates.append([a, int(b), int(c)])

makeUpdates(updates)
