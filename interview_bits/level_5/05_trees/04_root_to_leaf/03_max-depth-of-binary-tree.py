# https://www.interviewbit.com/problems/max-depth-of-binary-tree/
def max_depth(node):
    if node is None:
        return 0

    return max(max_depth(node.left), max_depth(node.right)) + 1
