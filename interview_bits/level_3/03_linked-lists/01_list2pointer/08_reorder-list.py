# https://www.interviewbit.com/problems/reorder-list/
def reverse(head):
    prev = None
    while head:
        next = head.next
        head.next = prev
        prev = head
        head = next

    return prev

def find_middle(head):
    num, copy_head = 0, head
    while head:
        head = head.next
        num += 1

    middle, head = num / 2, copy_head
    for i in xrange(middle):
        head = head.next

    start1, start2, prev = copy_head, head, None
    start2 = reverse(start2)

    for i in xrange(middle):
        next1, next2 = start1.next, start2.next
        start1.next = start2
        start2.next = next1

        start1, start2 = next1, next2

    if start2:
        start1.next = start2

    return head




