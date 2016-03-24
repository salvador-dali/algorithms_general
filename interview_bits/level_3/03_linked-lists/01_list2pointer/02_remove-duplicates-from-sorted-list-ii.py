def removeDuplicates(head):
    while head.next:
        if head.val == head.next.val:
            next_next = head.next.next
            head.next = next_next
        else:
            head = head.next




def deleteDuplicates(self, head):
    notNeeded = ListNode('someValue')
    notNeeded.next = head
    previous, current = notNeeded, head
    while current:
        if current.next and current.next.val == cur.val:
            val = current.val
            while current and current.val == val:
                current = current.next
            previous.next = current
        else:
            previous.next = current
            previous = current
            current = current.next
    return notNeeded.next