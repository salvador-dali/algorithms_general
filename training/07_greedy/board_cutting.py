# https://www.hackerrank.com/challenges/board-cutting
def cuttingBoard(x, y):
    # greedy search. Sort elements in the beginning
    # and grab the elements one by one
    x.sort(reverse=True)
    y.sort(reverse=True)

    # combine two arrays in one
    # these can be done in O(n + m), keeping track of
    # the coordinates
    combined, xNum, yNum = [], 0, 0
    for i in xrange(len(x) + len(y)):
        elX = -9999 if xNum >= len(x) else x[xNum]
        elY = -9999 if yNum >= len(y) else y[yNum]

        if elX > elY:
            combined.append([elX, 'x'])
            xNum += 1
        else:
            combined.append([elY, 'y'])
            yNum += 1

    s, xNum, yNum = 0, 0, 0
    for i in xrange(len(combined)):
        n, coordinate = combined[i]
        if coordinate == 'x':
            s += n * (yNum + 1)
            xNum += 1
        else:
            s += n * (xNum + 1)
            yNum += 1

    return s

for i in xrange(input()):
    raw_input()
    arr1 = list(map(int, raw_input().split()))
    arr2 = list(map(int, raw_input().split()))
    print cuttingBoard(arr1, arr2) % (10**9+7)