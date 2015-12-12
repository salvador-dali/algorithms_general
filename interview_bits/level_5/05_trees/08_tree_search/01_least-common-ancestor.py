# https://www.interviewbit.com/problems/least-common-ancestor/
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def get_path(node, v1, v2):
    mapping = {}
    def find_path(node, v1, v2, arr):
        if node is None:
            return

        if v1 == node.val:
            mapping[v1] = arr + [node.val]
        elif v2 == node.val:
            mapping[v2] = arr + [node.val]

        find_path(node.left, v1, v2, arr + [node.val])
        find_path(node.right, v1, v2, arr + [node.val])

    find_path(node, v1, v2, [])
    return mapping

def lca(node, v1, v2):
    mapping = get_path(node, v1, v2)
    if v1 not in mapping or v2 not in mapping:
        return -1

    arr1, arr2 = mapping[v1], mapping[v2]
    prev = -1
    for i in xrange(min(len(arr1), len(arr2))):
        if arr1[i] == arr2[i]:
            prev = arr1[i]
        else:
            break

    return prev
