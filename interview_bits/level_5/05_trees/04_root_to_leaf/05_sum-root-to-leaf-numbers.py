# https://www.interviewbit.com/problems/sum-root-to-leaf-numbers/

def summation_in_tree(node):
    total_sum = []
    def sum_numbers(node, num):
        if node is None:
            return

        tmp = (num * 10 + node.val) % 13
        if node.left is None and node.right is None:
            total_sum.append(tmp)
            return

        sum_numbers(node.left, tmp)
        sum_numbers(node.right, tmp)

    sum_numbers(node, 0)
    return sum(total_sum) % 13


def sum_numbers(node, num):
    if node is None:
        return num

    tmp = (num * 10 + node.val) % 13
    if node.left is None and node.right is None:
        return tmp

    return sum_numbers(node.left, tmp) + sum_numbers(node.right, tmp)


