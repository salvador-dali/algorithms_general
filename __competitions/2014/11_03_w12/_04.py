def DFS(tree):
    paths = {}
    frontier = [(1, [1])]
    checked = set()
    while frontier:
        vertex, prev_path = frontier.pop()
        paths[vertex] = prev_path
        checked.add(vertex)
        neighbors = tree[vertex]
        for i in neighbors:
            if i not in checked:
                frontier.append((i, prev_path + [i]))

    return paths

def pathInTree(paths, a, b):
    prev, path1, path2, i = None, paths[a], paths[b], 0
    while i < len(path1) and i < len(path2):
        el1, el2 = path1[i], path2[i]
        if el1 != el2:
            break
        prev = el1
        i += 1

    return path1[i:][::-1] + [prev] + path2[i:]

def getWeightsAndConstructTree():
    nodeWeights = {}
    N = input()
    for i in xrange(1, N + 1):
        nodeWeights[i] = list(map(int, raw_input().split()))

    tree = {}
    for i in xrange(N - 1):
        a, b = map(int, raw_input().split())
        if a in tree:
            tree[a].append(b)
        else:
            tree[a] = [b]

        if b in tree:
            tree[b].append(a)
        else:
            tree[b] = [a]

    return nodeWeights, tree

def superposition(A, B, x):
    MOD = 1000000007
    x %= MOD
    for i in xrange(len(A)):
        x = ((A[i] % MOD * x) % MOD + B[i] % MOD) % MOD
    return x

nodeWeights, tree = getWeightsAndConstructTree()
paths = DFS(tree)

for i in xrange(input()):
    query = list(map(int, raw_input().split()))
    if query[0] == 1:
        #updating all weights
        u, v, a, b = query[1], query[2], query[3], query[4]
        listOfNodes = pathInTree(paths, u, v)
        for _ in listOfNodes:
            nodeWeights[_] = [a, b]
    else:
        #calculating result
        u, v, x = query[1], query[2], query[3]
        A, B = [], []
        listOfNodes = pathInTree(paths, u, v)
        for _ in listOfNodes:
            tmp = nodeWeights[_]
            A.append(tmp[0])
            B.append(tmp[1])

        print superposition(A, B, x)
