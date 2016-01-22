# https://www.interviewbit.com/problems/inorder-traversal/
def inorder_recursion(node):
    res = []
    def inorder(node):
        if node is not None:
            inorder(node.left)
            res.append(node.val)
            inorder(node.right)

    inorder(node)
    return res

# not recursive
def inorder(node):
    stack, res = [], []
    while True:
        if node is not None:
            stack.append(node)
            node = node.left
        elif stack:
            node = stack.pop()
            res.append(node.val)
            node = node.right
        else:
            return res
