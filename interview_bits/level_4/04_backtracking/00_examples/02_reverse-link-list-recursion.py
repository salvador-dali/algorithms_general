# https://www.interviewbit.com/problems/reverse-link-list-recursion/
def reverseList(head):
    prev = None
    while head:
        tmp = head.next
        head.next = prev
        prev = head
        head = tmp

    return prev