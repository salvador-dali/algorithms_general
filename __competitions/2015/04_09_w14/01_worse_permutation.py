def swaps(arr, n, k):
    """
    https://www.hackerrank.com/contests/w14/challenges/worst-permutation
    Swap the biggest element from the list which is not in the position
    having additional data structure to store positions of each number
    """
    numToPos = {arr[i]: i for i in xrange(n)}
    biggest = n

    while k and biggest:
        if biggest != arr[n - biggest]:
            numPos = numToPos[biggest]
            numToPos[biggest] = numToPos[arr[n - biggest]]
            numToPos[arr[n - biggest]] = numPos

            arr[numPos] = arr[n - biggest]
            arr[n - biggest] = biggest
            k -= 1

        biggest -= 1

    return arr

n, k = map(int, raw_input().split())
arr = map(int, raw_input().split())
print ' '.join(map(str, swaps(arr, n, k)))