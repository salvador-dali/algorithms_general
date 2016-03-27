# https://www.interviewbit.com/problems/partition-list/
def partition(head, x):
    begSmaller = ListNode(0)
    endSmaller = begSmaller
    begLarger = ListNode(0)
    endLarger = begLarger
    pointer = head
    while pointer != None:
        if pointer.val <x:
            endSmaller.next = pointer
            endSmaller = pointer
        else:
            endLarger.next = pointer
            endLarger = pointer
        pointer = pointer.next
    endSmaller.next = begLarger.next
    endLarger.next = None
    return begSmaller.next