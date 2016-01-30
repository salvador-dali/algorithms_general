# https://www.interviewbit.com/problems/path-sum/
def path_sum(node, num):
    if node is None:
        return False

    if node.val == num and node.left is None and node.right is None:
        return True

    tmp = num - node.val
    return path_sum(node.left, tmp) or path_sum(node.right, tmp)
