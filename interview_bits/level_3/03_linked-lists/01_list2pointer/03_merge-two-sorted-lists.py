# https://www.interviewbit.com/problems/merge-two-sorted-lists/
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def merge_sorted(n1, n2):
    start = ListNode(0)
    start_copy = start
    while n1 and n2:
        if n1.val < n2.val:
            start.next = n1
            n1 = n1.next
        else:
            start.next = n2
            n2 = n2.next

        start = start.next

    if not n1 and not n2:
        return start_copy.next

    if not n1:
        start.next = n2
    if not n2:
        start.next = n1

    return start_copy.next
