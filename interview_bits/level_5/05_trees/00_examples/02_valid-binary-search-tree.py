# https://www.interviewbit.com/problems/valid-binary-search-tree/
def is_valid_bst(node, val_s, val_b):
    if not node:
        return True

    return val_s < node.val < val_b and is_valid_bst(node.left, val_s, node.val) and is_valid_bst(node.right, node.val, val_b)