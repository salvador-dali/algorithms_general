# https://www.hackerrank.com/challenges/countingsort2/
def countSort(arr):
    n = 100
    l = [0] * n
    for i in arr:
        l[i] += 1

    l1 = []
    for i in xrange(n):
        if l[i]:
            l1.extend([i] * l[i])

    return l1

raw_input()
arr = list(map(int, raw_input().split()))
print ' '.join(map(str, countSort(arr)))