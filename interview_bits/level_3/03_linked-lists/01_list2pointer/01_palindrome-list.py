# https://www.interviewbit.com/problems/palindrome-list/

def getLength(head):
    length = 0
    while head:
        head = head.next
        length += 1
    return length

def reverse(head):
    prev = None
    while head:
        tmp = head.next
        head.next = prev
        prev = head
        head = tmp

    return prev

def transform(head):
    n = getLength(head)
    head1 = head
    for i in xrange(n / 2):
        head = head.next

    if n % 2:
        head = head.next

    head2 = reverse(head)

    for _ in xrange(n / 2):
        if head1.val != head2.val:
            return 0

        head1, head2 = head1.next, head2.next

    return 1

