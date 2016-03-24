# https://www.interviewbit.com/problems/remove-nth-node-from-list-end/
def remove_n_th(node, n):
    start, length = node, 0
    while node:
        node = node.next
        length += 1

    if n >= length:
        return start.next

    pos_rem, node, curr = length - n, start, 0
    while node:
        curr += 1
        if curr == pos_rem:
            node.next = node.next.next
            break
        node = node.next

    return start

