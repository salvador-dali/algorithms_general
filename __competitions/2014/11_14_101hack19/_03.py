def longestDistanceFromRootUniformTree(tree, root):
    frontier = [root]
    checked = {root: 0}
    while frontier:
        node = frontier.pop()
        for child in tree[node]:
            if child not in checked:
                frontier.append(child)
                checked[child] = checked[node] + 1

    maximum, leaf = -1, -1
    for i in checked:
        if checked[i] > maximum:
            maximum, leaf = checked[i], i

    return maximum, leaf

N, M = map(int, raw_input().split())
tree = {}
for i in xrange(N - 1):
    v1, v2 = map(int, raw_input().split())
    if v1 in tree:
        tree[v1].append(v2)
    else:
        tree[v1] = [v2]

    if v2 in tree:
        tree[v2].append(v1)
    else:
        tree[v2] = [v1]

for i in xrange(M):
    d = 0
    v, k = map(int, raw_input().split())
    m, node = longestDistanceFromRootUniformTree(tree, v)
    d += m
    if k > 1:
        m, node = longestDistanceFromRootUniformTree(tree, node)
        d += m * (k - 1)

    print m
