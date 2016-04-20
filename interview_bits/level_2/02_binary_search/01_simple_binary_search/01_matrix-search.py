# https://www.interviewbit.com/problems/matrix-search/

def matrixSearch(M, a):
    y, x = len(M), len(M[0])

    low, high = 0, x * y - 1
    while low <= high:
        middle = (low + high) / 2
        tmp = M[middle / x][middle % x]
        if tmp == a:
            return 1

        if tmp > a:
            high = middle - 1
        else:
            low = middle + 1

    return 0