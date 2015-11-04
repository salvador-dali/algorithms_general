# https://www.interviewbit.com/problems/zigzag-level-order-traversal-bt/
def zigzag(root):
    res, curr_level, next_level, direction = [], [root], [], 1
    while curr_level:
        tmp = []
        for el in curr_level:
            tmp.append(el.val)
            if el.left:
                next_level.append(el.left)
            if el.right:
                next_level.append(el.right)
        curr_level, next_level = next_level, []
        if direction:
            res.append(tmp)
            direction = 0
        else:
            res.append(tmp[::-1])
            direction = 1

    return res
