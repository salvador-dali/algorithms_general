# https://www.interviewbit.com/problems/compare-version-numbers/
def compareVersions(s1, s2):
    arr1 = map(int, s1.split('.'))
    arr2 = map(int, s2.split('.'))
    m = max(len(arr1), len(arr2))

    arr1 += [0] * (m - len(arr1))
    arr2 += [0] * (m - len(arr2))

    for i in xrange(len(arr1)):
        if arr1[i] > arr2[i]:
            return 1
        if arr1[i] < arr2[i]:
            return -1
    return 0

