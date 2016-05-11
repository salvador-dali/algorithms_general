# https://www.interviewbit.com/courses/programming/topics/arrays/problems/reach/
# You are given a sequence of points and the order in which you need to cover the points.
# Give the minimum number of steps in which you can achieve it. You start from the first point.

def maxDistance(x, y):
    points, s = [(x[i], y[i]) for i in xrange(len(x))], 0
    for i in xrange(len(x) - 1):
        p1, p2 = points[i], points[i + 1]
        x1, y1 = abs(p2[0] - p1[0]), abs(p2[1] - p1[1])
        s += max(x1, y1)
    return s