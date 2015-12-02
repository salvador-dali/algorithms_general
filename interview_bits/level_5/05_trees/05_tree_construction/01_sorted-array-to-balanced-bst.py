# https://www.interviewbit.com/problems/sorted-array-to-balanced-bst/

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def create_tree_from_array(arr):
    if len(arr) == 0:
        return None
    mid = len(arr) / 2
    node = TreeNode(arr[mid])
    if len(arr[:mid]):
        node.left = create_tree_from_array(arr[:mid])

    if len(arr[mid + 1:]):
        node.right = create_tree_from_array(arr[mid + 1:])

    return node