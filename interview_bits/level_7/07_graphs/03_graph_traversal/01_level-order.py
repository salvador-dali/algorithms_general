# https://www.interviewbit.com/problems/level-order/
def level_order(root):
    if not root:
        return []
    prev, next, result, current = [root], [], [], []

    while prev:
        for i in prev:
            current.append(i.data)
            if i.left:
                next.append(i.left)
            if i.right:
                next.append(i.right)

        prev, next = next, []
        result.append(current)
        current = []

    return result