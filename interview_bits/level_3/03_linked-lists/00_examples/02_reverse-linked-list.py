# https://www.interviewbit.com/problems/reverse-linked-list/

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def reverse(head):
    new_head = None
    while head:
        head.next, head, new_head = new_head, head.next, head

    return new_head


def reverse(head):
    prev = None
    while head:
        tmp = head.next
        head.next = prev
        prev = head
        head = tmp

    return prev