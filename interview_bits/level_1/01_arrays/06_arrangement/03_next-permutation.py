# https://www.interviewbit.com/problems/next-permutation/
def nextPermutations(arr):
    haveFound = False
    for i in xrange(len(arr) - 1, 0, -1):
        if arr[i - 1] < arr[i]:
            haveFound, pos = True, i
            break

    if not haveFound:
        return arr[::-1]

    smallest = max(arr)
    for i in arr[pos:]:
        if arr[pos - 1] < i < smallest:
            smallest = i


    rest = [i for i in arr[pos - 1:] if i != smallest]
    rest.sort()

    return arr[:pos - 1] + [smallest] + rest
