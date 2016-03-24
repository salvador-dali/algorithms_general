# https://www.interviewbit.com/problems/remove-duplicates-from-sorted-list/
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def remove_dups(node):
    start, prev = node, ListNode(None)
    while node:
        if node.val == prev.val:
            node = node.next
        else:
            prev = node
            prev.next = node
            node = node.next

    return start
