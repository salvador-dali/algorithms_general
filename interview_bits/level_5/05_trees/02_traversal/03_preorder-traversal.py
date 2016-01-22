# https://www.interviewbit.com/problems/postorder-traversal/
def preorder(node):
    res = []

    def preorder_helper(node):
        if node is not None:
            res.append(node.val)
            preorder_helper(node.left)
            preorder_helper(node.right)

    preorder_helper(node)
    return res