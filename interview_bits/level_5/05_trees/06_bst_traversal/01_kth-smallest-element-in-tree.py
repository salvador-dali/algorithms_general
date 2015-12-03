# https://www.interviewbit.com/problems/kth-smallest-element-in-tree/
def k_smallest(node, k):
    res = []
    def inorder(node):
        if not node:
            return

        inorder(node.left)
        res.append(node.val)
        inorder(node.right)

    inorder(node)
    return res[k - 1]