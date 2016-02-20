# https://www.hackerrank.com/challenges/cavity-map
def cavity(arr):
    n = len(arr)
    for i in range(1, n - 1):
        for j in range(1, n -1):
            el = arr[i][j]
            if el == 'X':
                continue
            elif el > max(arr[i - 1][j], arr[i + 1][j], arr[i][j - 1], arr[i][j + 1]):
                arr[i][j] = 'X'

    for i in arr:
        print ''.join(map(str, i))

cavity([map(int, list(raw_input())) for i in xrange(input())])