# https://www.interviewbit.com/problems/inorder-traversal-of-cartesian-tree/
# this is bruteforce stupid way which runs in O(n^2). Read how to do this in O(n)

def get_max(arr):
    pos, m = 0, arr[0]
    for i in xrange(len(arr)):
        if arr[i] > m:
            m = arr[i]
            pos = i

    return pos

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def cartesian_bigger(arr):
    if not len(arr):
        return None

    pos = get_max(arr)
    node = TreeNode(arr[pos])
    if len(arr[:pos]):
        node.left = cartesian_bigger(arr[:pos])

    if len(arr[pos + 1:]):
        node.right = cartesian_bigger(arr[pos + 1:])

    return node
