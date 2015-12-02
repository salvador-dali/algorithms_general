# https://www.interviewbit.com/problems/construct-binary-tree-from-inorder-and-postorder/
def newTree(ind, postd):
    if len(postd) == 0:
        return None
    root = TreeNode(postd[-1])
    idx = ind.index(postd[-1])
    rlen = len(ind[idx+1:])
    llen = len(ind) - rlen - 1
    if rlen > 0:
        root.right = newTree(ind[idx+1:], postd[-(rlen+1):-1])
    if llen > 0:
        root.left = newTree(ind[0:idx], postd[0:llen])
    return root