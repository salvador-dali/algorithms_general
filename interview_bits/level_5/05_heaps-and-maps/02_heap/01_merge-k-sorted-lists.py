# https://www.interviewbit.com/problems/merge-k-sorted-lists/
import heapq

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def merge_k_lists(arr):
    h, head = [], ListNode(-1)
    tmp = head
    for i in arr:
        if i:
            heapq.heappush(h, (i.val, i))

    while True:
        try:
            el = heapq.heappop(h)
            node = ListNode(el[0])
            head.next = node
            head = node

            if el[1].next:
                heapq.heappush(h, (el[1].next.val, el[1].next))
        except:
            return tmp.next
