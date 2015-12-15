arr = [1, 2, 3, 4, 5, 6]

def swap(l, r):
    for i in xrange(l, r, 2):
        tmp = arr[i]
        arr[i] = arr[i + 1]
        arr[i + 1] = tmp

def swap_sum(queries):
    for i in queries:
        if i[0] == 1:
            swap(i[1] - 1, i[2] - 1)
        else:
            print sum(arr[i[1] - 1:i[2]])

    return 1


queries = [(1, 2, 5), (2, 2, 3), (2, 3, 4), (2, 4, 5), (1, 4, 5), (1, 4, 5), (2, 4, 5)]
for i in xrange(len(queries) - 1, -1, -1):
    if queries[i][0] == 2:
        break

swap_sum(queries[0:i + 1])