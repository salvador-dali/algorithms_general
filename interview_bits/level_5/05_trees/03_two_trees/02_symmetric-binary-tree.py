# https://www.interviewbit.com/problems/symmetric-binary-tree/
def is_symmetric(node):
    values = []
    def inoder(node):
        if node:
            inoder(node.left)
            values.append(node.val)
            inoder(node.right)

    inoder(node)
    return values == values[::-1]


def is_symmetric_recursion(n1, n2):
    if n1 is None and n2 is None:
        return True

    if (n1 is None and n2 is not None) or (n2 is None and n1 is not None) or (n1.val != n2.val):
        return False

    return is_symmetric_recursion(n1.right, n2.left) and is_symmetric_recursion(n1.left, n2.right)
