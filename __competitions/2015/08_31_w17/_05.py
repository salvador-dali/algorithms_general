from collections import defaultdict
from itertools import chain, combinations
from copy import deepcopy

def toGraph(arr, n, m):
    M = []
    for i in xrange(n):
        line = []
        for j in xrange(m):
            if arr[i][j] == '#':
                line.append(0)
            elif arr[i][j] == '.':
                line.append(1)
            else:
                line.append(2)
        M.append(line)
    return M

def findGraph(M, n, m):
    g, points = defaultdict(set), []
    for i in xrange(n * m):
        y, x = i / m, i % m
        if M[y][x] == 2:
            points.append(i)
        if M[y][x] == 1:
            if i not in g:
                g[i] = set()
            if y < n - 1 and M[y + 1][x] == 1:
                g[i + m].add(i)
                g[i].add(i + m)
            if x < m - 1 and M[y][x + 1] == 1:
                g[i + 1].add(i)
                g[i].add(i + 1)

    return g, points

def powerSet(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

def mergeGraph(g, arr, n, m):
    for i in arr:
        y, x = i / m, i % m
        if i not in g:
            g[i] = set()
            if y > 0 and (i - m) in g:
                g[i].add(i - m)
                g[i - m].add(i)

            if y < n - 1 and (i + m) in g:
                g[i].add(i + m)
                g[i + m].add(i)

            if x > 0 and (i - 1) in g:
                g[i].add(i - 1)
                g[i - 1].add(i)

            if x < m - 1 and (i + 1) in g:
                g[i].add(i + 1)
                g[i + 1].add(i)

    return g

def getRoots(aNeigh):
    def findRoot(aNode,aRoot):
        while aNode != aRoot[aNode][0]:
            aNode = aRoot[aNode][0]
        return (aNode,aRoot[aNode][1])
    myRoot = {}
    for myNode in aNeigh.keys():
        myRoot[myNode] = (myNode,0)
    for myI in aNeigh:
        for myJ in aNeigh[myI]:
            (myRoot_myI,myDepthMyI) = findRoot(myI,myRoot)
            (myRoot_myJ,myDepthMyJ) = findRoot(myJ,myRoot)
            if myRoot_myI != myRoot_myJ:
                myMin = myRoot_myI
                myMax = myRoot_myJ
                if  myDepthMyI > myDepthMyJ:
                    myMin = myRoot_myJ
                    myMax = myRoot_myI
                myRoot[myMax] = (myMax,max(myRoot[myMin][1]+1,myRoot[myMax][1]))
                myRoot[myMin] = (myRoot[myMax][0],-1)
    myToRet = {}
    for myI in aNeigh:
        if myRoot[myI][0] == myI:
            myToRet[myI] = []
    for myI in aNeigh:
        myToRet[findRoot(myI,myRoot)[0]].append(myI)
    return myToRet

def solver(arr, n, m):
    if ''.join(arr).count('?') > 16:
        return 0
    M = toGraph(arr, n, m)
    g, points = findGraph(M, n, m)

    total = 0
    for i in powerSet(points):
        G = deepcopy(g)
        G = mergeGraph(G, i, n, m)
        if len(getRoots(G)) == 0:
            total += 1
        elif len(getRoots(G)) == 1 and sum(len(G[_]) for _ in G) / 2 == len(G) - 1:
            total += 1

    return total

n, m = map(int, raw_input().split())
arr = [raw_input() for _ in xrange(n)]

print solver(arr, n, m)

