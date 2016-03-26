# https://www.interviewbit.com/problems/add-two-numbers-as-lists/

def addTwoNumbers(l1, l2):
    head, curr, prev = None, None, None
    carry = 0
    while l1 and l2:
        el = l1.val + l2.val + carry
        val, carry = el % 10, el / 10
        l1, l2 = l1.next, l2.next

        if not head:
            curr = ListNode(val)
            head = curr
        else:
            prev = curr
            curr = ListNode(val)
            prev.next = curr

    leftover = l1 if l1 else l2
    while leftover:
        el = leftover.val + carry
        val, carry = el % 10, el / 10
        leftover = leftover.next

        if not head:
            curr = ListNode(val)
            head = curr
        else:
            prev = curr
            curr = ListNode(val)
            prev.next = curr

    if carry:
        prev = curr
        curr = ListNode(carry)
        prev.next = curr
    return head