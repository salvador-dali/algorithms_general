# https://www.interviewbit.com/problems/assign-mice-to-holes/
def assignment(arr1, arr2):
    arr1.sort()
    arr2.sort()

    m = 0
    for i in xrange(len(arr1)):
        m = max(m, abs(arr1[i] - arr2[i]))

    return m