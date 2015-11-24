# https://www.interviewbit.com/problems/build-identical-trees
# http://stackoverflow.com/q/33859606/1090562

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def analysis(a, b):
    if a is None and b is None:
        return 0

    if a is None:
        l = analysis(a, b.left)
        if l == -1:
            return -1

        r = analysis(a, b.right)
        if r == -1:
            return -1

        return l + r + 1

    if b is None:
        return -1

    l = analysis(a.left, b.left)
    if l == -1:
        return -1

    r = analysis(a.right, b.right)
    if r == -1:
        return -1

    return l + r
