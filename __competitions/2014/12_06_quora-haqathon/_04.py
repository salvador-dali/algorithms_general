def exprectedFromRoot(tree, cost, root):
    from Queue import Queue
    frontier, checkedDistance, listInc = Queue(), {root: 0}, []
    frontier.put(root)
    while not frontier.empty():
        node = frontier.get()
        listInc.append(node)
        for child in tree[node]:
            if child not in checkedDistance:
                frontier.put(child)
                checkedDistance[child] = checkedDistance[node] + 1

    for element in listInc[::-1]:
        s, n = 0, 0.0
        for i in tree[element]:
            if checkedDistance[element] < checkedDistance[i]:
                s += cost[i]
                n += 1

        if n != 0:
            s /= n
        else:
            s = 0

        s += cost[element]
        cost[element] = s

    return cost[root]

def minimumExpected(tree, cost, biggestNode):
    import copy
    minimum = 10**10
    minNode = None
    for i in xrange(1, biggestNode + 1):
        c = copy.copy(cost)
        expected = exprectedFromRoot(tree, c, i)
        if expected < minimum:
            minimum = expected
            minNode = i

    return minNode


biggestNode = input()
arr = list(map(int, raw_input().split()))
cost = {(i + 1): arr[i] for i in xrange(len(arr))}   

tree = {}
for i in xrange(biggestNode - 1):
    v1, v2 = map(int, raw_input().split())
    tree.setdefault(v1, []).append(v2)
    tree.setdefault(v2, []).append(v1)
    
print minimumExpected(tree, cost, biggestNode)