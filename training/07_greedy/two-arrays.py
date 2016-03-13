# https://www.hackerrank.com/challenges/two-arrays
def temp(arr1, arr2):
    arr1.sort()
    arr2.sort(reverse=True)
    for i in range(len(arr1)):
        if arr1[i] + arr2[i] < k:
            print 'NO'
            return

    print 'YES'

for i in xrange(int(raw_input())):
    a, k = map(int, raw_input().split())
    arr1 = list(map(int, raw_input().split()))
    arr2 = list(map(int, raw_input().split()))

    temp(arr1, arr2)