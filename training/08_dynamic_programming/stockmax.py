# https://www.hackerrank.com/challenges/stockmax
# one thing to notice is that the best strategy is to find the biggest element from the list and to
# trade at this point and to start looking for the next maximum element
def stockmax(arr):
    s, cur, l, index = 0, 0, len(arr), 0

    while index < l:
        maxValue, index = 0, cur
        for i in xrange(cur, len(arr)):
            if arr[i] >= maxValue:
                maxValue = arr[i]
                index = i

        additional = (index - cur) * maxValue - sum(arr[cur:index])
        s += additional
        cur = index + 1

    return s

for i in xrange(input()):
    raw_input()
    print stockmax(list(map(int, raw_input().split())))

