# https://www.hackerrank.com/challenges/almost-sorted
# iterates over the elements in array to find potential positions. Does not handle sorted array
def findPosition(arr):
    # check where the difference changes
    l = [0 if arr[i - 1] < arr[i] else 1 for i in range(1, len(arr))]
    s = sum(l)

    # if this happens only once -> than it is potential swap
    # between two subsequent elements
    if s == 1:
        for i in xrange(len(l)):
            if l[i] == 1:
                return 1, i, i + 1
    # if this happens two times -> also potential swap
    # but we need to find where the last position
    elif s == 2:
        start, end = -1, -1
        for i in xrange(len(l)):
            if l[i] == 1:
                if start == -1:
                    start = i
                else:
                    end = i + 1
        return 1, start, end
    # this means that this might be a reverse
    # reverse ends when there is a 0
    else:
        startFound = 0
        for i in xrange(len(l)):
            if startFound == 0 and l[i]:
                start = i
                startFound = 1
            if startFound and l[i] == 0:
                end = i
                break

        # if there is any one after this -> than it is not possible to do with a reverse
        if sum(l[end:]):
            return -1

        return 0, start, end + 1

# verify that the the swap or reverse works
def check(isSwap, start, end, arr):
    if isSwap:
        tmp = arr[start]
        arr[start] = arr[end]
        arr[end] = tmp
    else:
        arr[start: end] = arr[start:end][::-1]

    if sum([0 if arr[i - 1] < arr[i] else 1 for i in range(1, len(arr))]):
        return -1

    if isSwap:
        return 'swap', start + 1, end + 1
    else:
        return 'reverse', start + 1, end

def almostSorted(arr):
    res = findPosition(arr)
    if res == -1:
        return -1

    return check(res[0], res[1], res[2], arr)

raw_input()
res = almostSorted(list(map(int, raw_input().split())))
if res == -1:
    print 'no'
else:
    print 'yes'
    print ' '.join(map(str, list(res)))