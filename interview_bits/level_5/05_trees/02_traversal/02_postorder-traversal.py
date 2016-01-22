# https://www.interviewbit.com/problems/postorder-traversal/
def postorder_recursive(node):
    res = []
    def postorder_helper(node):
        if node is not None:
            postorder_helper(node.left)
            postorder_helper(node.right)
            res.append(node.val)

    postorder_helper(node)

    return res


# http://www.geeksforgeeks.org/iterative-postorder-traversal-using-stack/

