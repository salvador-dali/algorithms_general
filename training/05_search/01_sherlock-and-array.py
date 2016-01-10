# https://www.hackerrank.com/challenges/sherlock-and-array
def arr_partition(arr):
    first, second = 0, sum(arr)

    for i in xrange(len(arr)):
        if i:
            first += arr[i - 1]
        second -= arr[i]
        if first == second:
            return True
    return False

for i in xrange(input()):
    raw_input()
    if arr_partition(map(int, raw_input())):
        print 'YES'
    else:
        print 'NO'