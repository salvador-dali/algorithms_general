# https://www.interviewbit.com/problems/reverse-link-list-ii/
def reverseBetween(head, m, n):
    if not head or not head.next:
        return head
    dummy = ListNode(0); dummy.next = head
    head1 = dummy
    for i in range(m - 1):
        head1 = head1.next
    p = head1.next
    for i in range(n - m):
        tmp = head1.next
        head1.next = p.next
        p.next = p.next.next
        head1.next.next = tmp
    return dummy.next