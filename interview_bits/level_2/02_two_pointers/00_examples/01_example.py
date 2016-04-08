# https://www.interviewbit.com/courses/programming/topics/two-pointers/

arr = [-8, -5, -4, -2, -1, 0, 1, 6, 7, 9, 13]

def findElements(arr):
    n = len(arr)
    for i in xrange(n):
        for j in xrange(n - 1, i - 1, -1):
            if i != j and arr[i] + arr[j] == 0:
                return arr[i], arr[j]

            if arr[i] + arr[j] < 0:
                break
