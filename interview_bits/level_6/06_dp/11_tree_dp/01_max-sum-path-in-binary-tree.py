# https://www.interviewbit.com/problems/max-sum-path-in-binary-tree/
def max_path(root):
    if not root:
        return None

    maximum = [root.val]
    def max_path_rec(node, curr):
        if not node:
            return 0

        l = max_path_rec(node.left, curr)
        r = max_path_rec(node.right, curr)
        val = node.val

        one_way = val + max(0, l, r)
        two_way = max(one_way, l + r + val)

        maximum[0] = max(maximum[0], two_way)
        return one_way

    max_path_rec(root, maximum[0])
    return maximum[0]