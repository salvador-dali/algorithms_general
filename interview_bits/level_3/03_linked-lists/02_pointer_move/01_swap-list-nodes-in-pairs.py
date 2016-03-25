# https://www.interviewbit.com/problems/swap-list-nodes-in-pairs/
def pairwiseSwap(head):
    temp = head

    if temp is None:
        return temp

    while temp is not None and temp.next is not None:
        temp.data, temp.next.data = temp.next.data, temp.data
        temp = temp.next.next

    return head