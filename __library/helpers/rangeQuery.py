"""
# Various algorithms that requires pre-processing of the input data to be able later to answer a lot of
# specific queries later. Algorithm run in <f(n), g(n)> time (pre-processing and each query time)
# and requires h(n) extra memory.
# http://www.spoj.com/problems/FREQUENT/
# http://www.spoj.com/problems/GSS1/
# http://www.spoj.com/problems/GSS2/
# http://www.spoj.com/problems/GSS3/
# http://www.spoj.com/problems/HORRIBLE
# http://www.spoj.pl/problems/IOPC1207/
# http://www.spoj.com/problems/SEGSQRSS/
# http://www.spoj.com/problems/ORDERSET/
# http://www.spoj.com/problems/HELPR2D2/
# http://www.spoj.com/problems/TEMPLEQ
http://www.codechef.com/problems/FLIPCOIN
# http://acm.timus.ru/problem.aspx?space=1&num=1846
"""

def rangeSum(arr, queries):
    """
    for a given array and a list of queries return the
    result for each query, where the query asks to sum elements of the array from index i to j
    rangeSum([3, 7, 2, 8], [(0, 0), (1, 3), (3, 3)])

    runs in <O(n), O(1)> and O(n)
    Precalculate the sum from 1 to every position and use this information to get queries in O(1)
    """
    prefixSum, total = [0], 0
    for i in arr:
        total += i
        prefixSum.append(total)

    return [prefixSum[j + 1] - prefixSum[i] for i, j in queries]

def rangeSum2D(M, queries):
    """
    for a given matrix and a list of queries return the result of each query,
    where the query asks to sum elements of the matrix from (x1, y1, x2, y2)
    M = [[1, 2, 4, 5, -1, 3], [2, 1, 7, 8, 1, 2], [1, -2, 3, -2, 0, 2],
    [1, -1, -1, 2, 3, 7], [-3, 0, 2, 1, 4, 3], [2, 6, 4, 8, 3, 1], [7, 1, 4, 4, -3, 2]]
    rangeSum2D(M, [(4, 4, 5, 6), (1, 5, 2, 5), (2, 1, 4, 2), (0, 0, 1, 4), (1, 2, 4, 4), (2, 0, 5, 6)])

    runs in <O(n^2), O(1)> and (O(n^2))
    precalculate the sum from (0, 0) to (i, j) and use it to get any other in O(1)
    """
    def prefixSum(arr):
        res, total = [], 0
        for i in arr:
            total += i
            res.append(total)
        return res

    S = [prefixSum(i) for i in M]
    for i in xrange(1, len(S)):
        S[i] = [sum(x) for x in zip(S[i], S[i - 1])]

    res = []
    for a, b, c, d in queries:
        # all the (x, y) are reversed because of how I store matrix in python
        tmp1 = 0 if not b else S[b - 1][c]
        tmp2 = 0 if not a else S[d][a - 1]
        tmp3 = 0 if not a or not b else S[b - 1][a - 1]
        res.append(S[d][c] - tmp1 - tmp2 + tmp3)
    return res

def rangeMinQuery(arr, queries):
    """
    Given an array of numbers and a list of queries (of two types: update and execute)
    - for every update  query - update element with position with a new value
    - for every execute query - find a minimum number in this range

    This can be done using pre-processing in O(n) and then all queries are answered in O(log(n)).
    It requires O(n) space.
    http://wcipeg.com/wiki/Segment_tree

    Segment tree is used. Each node in a segment stores aggregated statistics for some segment
    of an array. The leafs store aggregated statistics for individual array elements
    The tree is stored in the array, and for an easier retrieval the starting interval is stored in the position 1.
    And if the node has the position x, then its left and right children at 2*x and 2*x+1 respectively.
    """
    def init(node, s, e):
        if s == e:
            tree[node] = arr[s]
        else:
            m, node_1 = (s + e) / 2, 2 * node
            init(node_1, s, m)
            init(node_1 + 1, m + 1, e)
            tree[node] = min(tree[node_1], tree[node_1 + 1])

    def update(node, s, e, pos, value):
        if pos < s or pos > e:
            return

        if s == e:
            tree[node] = value
        else:
            m, node_1 = (s + e) / 2, node * 2
            update(node_1, s, m, pos, value)
            update(node_1 + 1, m + 1, e, pos, value)
            tree[node] = min(tree[node_1], tree[node_1 + 1])

    def query(node, s, e, i, j):
        if i <= s and j >= e:
            return tree[node]

        if s > j or e < i:
            return float("inf")

        m, node_1 = (s + e) / 2, 2 * node
        return min(query(node_1, s, m, i, j), query(node_1 + 1, m + 1, e, i, j))

    from math import ceil, log
    tree, n = [None] * pow(2, int(ceil(log(len(arr), 2)) + 1)), len(arr) - 1
    init(1, 0, n)

    res = []
    for operation, i, j in queries:
        if operation == 'update':
            # i - position which to update, j - new value
            update(1, 0, n, i, j)
        else:
            # i - starting position, j - ending position
            res.append(query(1, 0, n, i, j))

    return res

def rangeSumQuery(arr, queries):
    # read explanation for rangeMinQuery
    def init(node, s, e):
        if s == e:
            tree[node] = arr[s]
        else:
            m, node_1 = (s + e)/2, 2 * node
            init(node_1, s, m)
            init(node_1 + 1, m + 1, e)

            tree[node] = tree[node_1] + tree[node_1 + 1]

    def update(node, s, e, pos, diff):
        if pos < s or pos > e:
            return

        tree[node] += diff
        if s != e:
            m, node_1 = (s + e)/2, 2 * node
            update(node_1, s, m, pos, diff)
            update(node_1 + 1, m + 1, e, pos, diff)

    def query(node, s, e, i, j):
        # s, e - segment representing current node
        # i, j - range of our query
        if i <= s and j >= e:   # segment of current node is inside of our query
            return tree[node]

        if s > j or e < i:      # segment of current node is outside of the query
            return 0

        m, node_1 = (s + e)/2, 2 * node
        return query(node_1, s, m, i, j) + query(node_1 + 1, m + 1, e, i, j)

    from math import log, ceil
    tree, n = [None] * pow(2, int(ceil(log(len(arr), 2))) + 1), len(arr) - 1
    init(1, 0, n)

    res = []
    for operation, i, j in queries:
        if operation == 'update':
            # i - position which to update, j - new value
            diff = j - arr[i]
            arr[i] = j
            update(1, 0, n, i, diff)
        else:
            res.append(query(1, 0, n, i, j))    # i - starting position, j - ending position

    return res

def rangeMaxQueryLazy(arr, queries):
    """
    We have a very large array called arr, and very large set of operations
    Operation #1: Increment the elements within range [i, j] with value val
    Operation #2: Get max element within range [i, j]

    http://stackoverflow.com/a/28036358/1090562
    similar to range min query but also uses the idea of lazy propagation
    with lazy propagation we update not a single element, but all elements in the range
    If we just change the update one element method, we branch its children even if the
    segment is covered within range. In the lazy version we only mark its child that it needs to
    be updated and update it when needed
    """
    def init(node, s, e):
        if s == e:
            tree[node] = arr[s]
        else:
            m, node_1 = (s + e) / 2, 2 * node
            init(node_1, s, m)
            init(node_1 + 1, m + 1, e)
            tree[node] = max(tree[node_1], tree[node_1 + 1])

    def update(node, s, e, i, j, value):
        m, node_1 = (s + e)/2, 2 * node

        if needsUpdate[node]:   # node needs to be updated
            tree[node] += needsUpdate[node]
            if s != e:
                needsUpdate[node_1] += needsUpdate[node]
                needsUpdate[node_1 + 1] += needsUpdate[node]
            needsUpdate[node] = 0

        if e < i or j < s:  # outside the range
            return

        if i <= s and e <= j:   # inside the range
            tree[node] += value
            if s != e:
                needsUpdate[node_1] += value
                needsUpdate[node_1 + 1] += value
        else:
            update(node_1, s, m, i, j, value)
            update(node_1 + 1, m + 1, e, i, j, value)
            tree[node] = max(tree[node_1], tree[node_1 + 1])

    def query(node, s, e, i, j):
        if s > j or e < i:
            return float("-inf")

        m, node_1 = (s + e)/2, 2*node
        if needsUpdate[node]:
            tree[node] += needsUpdate[node]
            if s != e:
                needsUpdate[node_1] += needsUpdate[node]
                needsUpdate[node_1 + 1] += needsUpdate[node]
            needsUpdate[node] = 0

        if s >= i and e <= j:
            return tree[node]

        return max(query(node_1, s, m, i, j), query(node_1 + 1, m + 1, e, i, j))

    from math import ceil, log
    tree, n = [None] * pow(2, int(ceil(log(len(arr), 2)) + 1)), len(arr) - 1
    needsUpdate = [0] * len(tree)
    init(1, 0, n)

    res = []
    for _ in queries:
        if _[0] == 'update':
            update(1, 0, n, _[1], _[2], _[3])
        else:
            res.append(query(1, 0, n, _[1], _[2]))

    return res