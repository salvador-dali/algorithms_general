# https://www.hackerrank.com/challenges/quicksort1
def partition(arr):
    val = arr[0]
    small, big = [], []
    for i in xrange(1, len(arr)):
        if arr[i] > val:
            big.append(arr[i])
        else:
            small.append(arr[i])

    return small + [val] + big

raw_input()
arr = list(map(int, raw_input().split()))
print ' '.join(map(str, partition(arr)))
