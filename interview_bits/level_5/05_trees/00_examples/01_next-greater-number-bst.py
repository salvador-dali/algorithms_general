# https://www.interviewbit.com/problems/next-greater-number-bst/
def getSuccessor(node, data):
    successor = None
    while node:
        if node.val == data:
            node = node.right
            while node:
                successor, node = node, node.left
            return successor
        elif node.val > data:
            successor, node = node, node.left
        else:
            node = node.right
    return successor