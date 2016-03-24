# https://www.interviewbit.com/problems/rotate-list/

def rotate(node, k):
    if not node:
        return None
        
    start, length, last = node, 0, None
    while node:
        last = node
        node = node.next
        length += 1

    k %= length
    if k == 0:
        return start
        
    node = start
    for _ in xrange(length - k - 1):
        node = node.next
    
    res = node.next    
    node.next = None
    last.next = start
    return res