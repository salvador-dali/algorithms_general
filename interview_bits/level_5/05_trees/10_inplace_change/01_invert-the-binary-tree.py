# https://www.interviewbit.com/problems/invert-the-binary-tree/
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def invert(node):
    if not node:
        return

    if not node.left:
        node.left, node.right = node.right, None
        invert(node.left)
    elif not node.right:
        node.right, node.left = node.left, None
        invert(node.right)
    else:
        node.left, node.right = node.right, node.left
        invert(node.right)
        invert(node.left)
