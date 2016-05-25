# https://www.interviewbit.com/problems/intersection-of-linked-lists/
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def getLength(A):
    length = 0
    while A is not None:
        A = A.next
        length += 1
    return length

def getIntersection(A , B, diff):
    for i in xrange(diff):
        A = A.next

    while A != B:
        A, B = A.next, B.next
    return A

def getIntersectionNode(A, B):
    a, b = getLength(A), getLength(B)
    return getIntersection(A, B, a - b) if a > b else getIntersection(B, A, b - a)
