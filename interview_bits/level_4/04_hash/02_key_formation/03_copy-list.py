# https://www.interviewbit.com/problems/copy-list/
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


def copyRandomList(head):
    if not head:
        return None

    new_head = RandomListNode(head.label)
    p, q, h = head, new_head, {head: new_head}
    p = p.next
    while p:
        temp = RandomListNode(p.label)
        h[p] = temp
        q.next = temp
        q, p = temp, p.next

    p, q = head, new_head
    while p:
        if p.random:
            q.random = h[p.random]

        p, q = p.next, q.next

    return new_head
