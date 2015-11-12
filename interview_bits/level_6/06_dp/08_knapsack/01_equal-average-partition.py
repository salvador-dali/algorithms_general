# https://www.interviewbit.com/problems/equal-average-partition/
# http://karmaandcoding.blogspot.com/2012/01/partition-array-into-2-parts-with-equal.html

def isPossible(arr):
    n, s, subsetLen = len(arr), sum(arr), len(arr) / 2
    avg = s / float(n)

    T = [[[False for k in xrange(s + 1)] for i in xrange(n + 1)] for j in xrange(subsetLen + 1)]
    for i in xrange(n + 1):
        T[0][i][0] = True

    for k in xrange(1, subsetLen + 1):
        for i in xrange(1, n):
            for j in xrange(1, s + 1):
                if arr[i] <= j:
                    T[k][i][j] = T[k - 1][i - 1][j - arr[i]]

                print k, i, j
                T[k][i][j] = T[k][i][j] or T[k][i-1][j]

                if T[k][i][j] and abs(j / float(k) - avg) < 0.000001:
                    return True

    return False

def isPossible(A, start, inset, target, cache):
    if not inset:
        return abs(target) < 0.0001

    if start == len(A):
        return False


    key = (start, inset, target)
    if key in cache:
        return cache[key]
    sol = isPossible(A, start + 1, inset - 1, target - A[start], cache) or isPossible(A, start + 1, inset, target, cache)
    cache[key] = sol
    return sol

def avgset(arr):
    arr, avg = sorted(arr), float(sum(arr)) / float(len(arr))
    I, total = None, None
    for i in xrange(1, len(arr)/2 + 1):
        cache = {}
        if not isPossible(arr, 0, i, i * avg, {}):
            continue
        I, total = i, i*avg
        break

    if not I:
        return []

    a, b = [], []
    for j in xrange(len(arr)):
        if isPossible(arr, j + 1, I - 1, total - arr[j], cache):
            a.append(arr[j])
            I -= 1
            total -= arr[j]
        else:
            b.append(arr[j])

    a.sort()
    b.sort()
    return [a, b]