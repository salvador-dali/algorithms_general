# https://www.interviewbit.com/problems/convert-sorted-list-to-binary-search-tree/
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def create_tree_from_array(arr):
    if not len(arr):
        return None

    mid = len(arr) / 2
    node = TreeNode(arr[mid])
    if len(arr[:mid]):
        node.left = create_tree_from_array(arr[:mid])

    if len(arr[mid + 1:]):
        node.right = create_tree_from_array(arr[mid + 1:])

    return node


def create_arr_from_list(node):
    arr = []
    while node:
        arr.append(node.val)
        node = node.next

    return arr