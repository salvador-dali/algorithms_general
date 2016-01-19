# https://www.interviewbit.com/problems/balanced-binary-tree/
def maxd(root):
    if root is None:
        return 0

    return 1 + max(maxd(root.left), maxd(root.right))

def is_balanced(root):
    if root is None:
        return True

    if abs(maxd(root.left) - maxd(root.right)) > 1:
        return False

    return is_balanced(root.left) and is_balanced(root.right)
