# https://www.interviewbit.com/problems/min-depth-of-binary-tree/
def minDepth(root):
    if root is None:
        return 0

    if root.left is None:
        return 1 + minDepth(root.right)

    if root.right is None:
        return 1 + minDepth(root.left)

    return min(minDepth(root.left), minDepth(root.right)) + 1