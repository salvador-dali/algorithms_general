from graph import topologicalSortLayers

def graphFromSubtraction(arr, n=100):
    G = {}
    for val in xrange(n):
        G[val] = [val - i for i in arr if val - i >= 0]

    return G

def mex_arr(arr):
    # minimum excluded values for an array
    d, i = set(arr), 0
    while i in d:
        i += 1

    return i

def mex_dict(d):
    # minimum excluded values for a dictionary
    i = 0
    while i in d:
        i += 1

    return i

def grundyValues(G):
    # calculates grundy values from the graph
    # make sure that the graph has leaves
    G_copy, grundy = {v: G[v][::] for v in G}, {}
    for layer in topologicalSortLayers(G_copy):
        for val in layer:
            grundy[val] = mex_arr([grundy[z] for z in G[val]])

    return grundy

def getPeriod(arr):
    # http://stackoverflow.com/q/37383086/1090562
    min_offset, min_period, n = len(arr), len(arr), len(arr)
    best_offset, best_period = [], []
    for offset in xrange(n):
        start = arr[:offset]
        for period_len in xrange(1, (n - offset) / 2):
            period = arr[offset: offset+period_len]
            attempt = (start + period * (n / period_len + 1))[:n]

            if attempt == arr:
                if period_len < min_period:
                    best_offset, best_period = start[::], period[::]
                    min_offset, min_period = len(start), period_len
                elif period_len == min_period and len(start) < min_offset:
                    best_offset, best_period = start[::], period[::]
                    min_offset, min_period = len(start), period_len

    return best_offset, best_period

def xor(arr):
    res = 0
    for i in arr:
        res ^= i
    return res

def green_hackenbush(tree, node):
    # tree should be a rooted tree
    # https://www.hackerrank.com/contests/5-days-of-game-theory/challenges/deforestation
    res = 0
    if node in tree:
        for child in tree[node]:
            res ^= 1 + green_hackenbush(tree, child)
    return res