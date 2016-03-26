# https://www.interviewbit.com/problems/list-cycle/

def findCycle(A):
    while A:
        if type(A.val) != int:
            A.val = A.val[0]
            return A

        A.val = [A.val]
        A = A.next

    return None

