def randomEdges(k=2, prob=0.9):
    """
    generate a k-nary tree, where each edge has a probability of appearance
    :param k:       maximum number of children of each node
    :param prob:    probability of appearance
    :return:        list of edges
    """
    from random import randint, random
    from Queue import Queue
    edges, frontier, lastEl = [], Queue(), 1
    frontier.put(1)
    while random() <= prob:
        if not frontier:
            break

        v1 = frontier.get()
        for i in xrange(randint(1, k)):
            lastEl += 1
            frontier.put(lastEl)
            edges.append([v1, lastEl])

    return edges

def unweightedGraph(G):
    """
    Converts the weighted graph into unweighted one
    :param G:   weighted graph {node1: [(node_1, weight), ... ], ....}
    :return:    unweighted graph {node1: {node2, node3, ...}, ...}
    """
    return {i: {k[0] for k in G[i]} for i in G}

def reverseWeightedGraph(G):
    """
    Heaving the weighted Graph, it just reverse it
    :param G:   weighted graph
    :return:    reveresed weighted graph
    """
    from collections import defaultdict

    graph = defaultdict(list)
    for v in G:
        for u, d in G[v]:
            graph[u].append((v, d))

    return dict(graph)

def createRootedTree(tree, root):
    """
    from an arbitrary tree, creates a tree with a specific root
    the rooted tree has only path to the children
    :param tree:
    :param root:
    :return:
    """
    from collections import defaultdict
    from Queue import Queue
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

def Kahn(G):
    """
    Topologically sort a graph G. Input representation:
    G can be anything for which iter(G) loops through the vertices of G
    and for which G[v] produces a list of outgoing neighbors of v."""
    # http://blogse.quora.com/Topological-sorting-in-Python
    # http://en.wikipedia.org/wiki/Talk%3ATopological_sorting
    # TODO have not coded it. Understand how it works
    # Count indegrees
    indegree = dict((v,0) for v in G)
    for v in G:
        for w in G[v]:
            indegree[w] += 1

    # Collect vertices with indegree zero
    ready = [v for v in G if indegree[v] == 0]

    # Loop through ready list updating indegrees
    done = 0
    while done < len(ready):
        v = ready[done]
        for w in G[v]:
            indegree[w] -= 1
            if indegree[w] == 0:
                ready.append(w)
        done += 1

    if len(ready) != len(indegree):
        raise Exception("Not all vertices were included: graph is cyclic")
    return ready

def longestPath(G, rev_G, topSort):
    # http://www.geeksforgeeks.org/find-longest-path-directed-acyclic-graph/
    # http://www.mathcs.emory.edu/~cheung/Courses/171/Syllabus/11-Graph/Docs/longest-path-in-dag.pdf
    # http://www.logarithmic.net/pfh/blog/01208083168
    distances = {topSort[0]: 0}
    for v in topSort[1:]:
        listOfDist = [(n, d + distances[n]) for n, d in rev_G[v]]
        distances[v] = max(listOfDist, key=lambda x: x[1])[1]

    return distances

def longestDistanceFromRootUniformTree(tree, root):
    # finds the distance from the root to it's longest leaf.
    # and returns this distance together with the leaf
    # uses DFS runs in O(V + E) and space O(V)
    frontier, distances = [root], {root: 0}
    # checked stores the distance from the root to the each checked node
    while frontier:
        node = frontier.pop()
        for child in tree[node]:
            if child not in distances:
                frontier.append(child)
                distances[child] = distances[node] + 1

    # checked now has the distance to every node
    leaf, maximum = max(distances.iteritems(), key=lambda x: x[1])
    return maximum, leaf



def longestDistanceInUniformTree(tree):
    # finds the length of the longest path for a tree, also returns two nodes which creates this path
    # takes any vertex and makes it a node
    # then checks the longest distance from this node and remembers the destination.
    # then finds the longest distance from the new node. This distance will be the longest
    # and it will be from leaf1 to leaf2.
    # because longestDistance is DFS, then the whole algorithm runs in O(V + E) and takes O(V) space
    root = tree.iterkeys().next()
    _, leaf1 = longestDistanceFromRootUniformTree(tree, root)
    m, leaf2 = longestDistanceFromRootUniformTree(tree, leaf1)
    return m, leaf1, leaf2

def lowestCommonAncestor(tree, root, node1, node2):
    """
    find the lowest common ancestor between the two nodes in the rooted tree
    http://en.wikipedia.org/wiki/Lowest_common_ancestor
    http://community.topcoder.com/tc?module=Static&d1=tutorials&d2=lowestCommonAncestor
    :param tree:        {1: [2, 5, 6, 7], 2: [1, 3, 4], 3: [2], 4: [2], 5: [1], 6: [1], 7: [1, 8], 8: [7]}
    :param root:        what is considered as a root of the tree
    :param node1,node2: two nodes for which LCA should be found
    :return:
    """
    if node1 == node2:
        return node1

    frontier, checked, needToFind = [root], {root: 0}, {node1, node2}
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
        if l1[i] != l2[i]:
            return l1[i - 1]

    return l1[i]

