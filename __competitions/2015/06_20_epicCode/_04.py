def maxsum(sequence):
    maxSoFar, maximum = 0, 0
    for x in sequence:
        maximum = max(maximum + x, 0)
        maxSoFar = max(maxSoFar, maximum)
    return maxSoFar

def getValues(arr):
    matrix = [[i * j for j in arr] for i in reversed(arr)]
    n = len(arr)

    subArray_1 = [matrix[j][j] for j in xrange(n / 2)]
    best = maxsum(subArray_1)

    for i in xrange(1, n - 1):
        subArray_1, subArray_2 = [], []
        for j in xrange((n - i) / 2):
            subArray_1.append(matrix[j][j + i])
            best = max(best, maxsum(subArray_1))
            subArray_2.append(matrix[j + i][j])
            best = max(best, maxsum(subArray_2))

    print best

_ = input()
arr = list(map(int, raw_input().split()))
getValues(arr)
