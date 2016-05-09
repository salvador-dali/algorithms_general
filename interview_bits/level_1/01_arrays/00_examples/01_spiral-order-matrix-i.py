# https://www.interviewbit.com/courses/programming/topics/arrays/problems/spiral1/
# return a spiral representation of an array
def getSpiral(arr):
    x1, y1, x2, y2, direction, res = 0, 0, len(arr[0]) - 1, len(arr) - 1, 'right', []
    while x1 <= x2 and y1 <= y2:
        if direction == 'right':
            for i in xrange(x1, x2 + 1):
                res.append(arr[y1][i])
            direction, y1 = 'down', y1 + 1

        elif direction == 'down':
            for i in xrange(y1, y2 + 1):
                res.append(arr[i][x2])
            direction, x2 = 'left', x2 - 1

        elif direction == 'left':
            for i in xrange(x2, x1 - 1, -1):
                res.append(arr[y2][i])
            direction, y2 = 'up', y2 - 1

        elif direction == 'up':
            for i in xrange(y2, y1 - 1, -1):
                res.append(arr[i][x1])
            direction, x1 = 'right', x1 + 1
    return res
