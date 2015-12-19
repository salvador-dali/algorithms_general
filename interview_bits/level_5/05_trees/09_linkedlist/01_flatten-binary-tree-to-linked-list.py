# https://www.interviewbit.com/problems/flatten-binary-tree-to-linked-list/
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def flatten(node):
    def preorder(node):
        if not node:
            return

        preorder.tmp.right = TreeNode(node.val)
        preorder.tmp = preorder.tmp.right

        preorder(node.left)
        preorder(node.right)

    head = TreeNode(None)
    preorder.tmp = head
    preorder(node)
    return head.right
