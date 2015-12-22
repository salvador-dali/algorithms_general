def bestLocation(arr, s, e):
    minimum, pos_s = 1000000, 0
    for i in xrange(s, e + 1):
        el = arr[i]
        if not el:
            return 0, s, e

        if el < minimum:
            minimum = el
            pos_s = i

    if minimum != 1:
        return minimum, pos_s, pos_s

    best_l, best_p, l = 0, 0, 0
    for i in xrange(s, e + 1):
        if arr[i] == 1:
            l += 1
        else:
            if l > best_l:
                best_l, best_p = l, i
            l = 0

    if l > best_l:
        best_l, best_p = l, i + 1

    return 1, best_p - best_l, best_p - 1

def make_queries(arr, queries):
    for t, i, j in queries:
        if t == 2:
            arr[i] = j
        else:
            minimum, s, e = bestLocation(arr, i, j)
            print minimum, s + 1, e + 1

n, q = map(int, raw_input().split())
arr = map(int, raw_input().split())
queries = []
for _ in xrange(q):
    t, i, j = map(int, raw_input().split())
    if t == 1:
        queries.append((1, i - 1, j - 1))
    else:
        queries.append((2, i - 1, j))

make_queries(arr, queries)