# https://www.interviewbit.com/problems/insertion-sort-list/
def sortList(head):
    if not head:
        return None

    counter, tmp = 0, head
    while tmp:
        tmp = tmp.next
        counter += 1

    return sort(head, counter)

def sort(head, size):
    if size == 1:
        return head

    list2 = head
    for i in xrange(size / 2):
        list2 = list2.next

    list1, list2 = sort(head, size / 2), sort(list2, size - size / 2)
    return merge(list1, size / 2, list2, size - size / 2)


def merge(list1, size1, list2, size2):
    dummy = ListNode(0)
    list_, pointer1, pointer2 = dummy, 0, 0

    while pointer1 < size1 and pointer2 < size2:
        if list1.val<list2.val:
            list_.next, list1, pointer1 = list1, list1.next, pointer1 + 1
        else:
            list_.next, list2, pointer2 = list2, list2.next, pointer2 + 1
        list_ = list_.next

    while pointer1 < size1:
        list_.next, list1, pointer1, list_ = list1, list1.next, pointer1 + 1, list_.next
    while pointer2 < size2:
        list_.next, list2, pointer2, list_ = list2, list2.next, pointer2 + 1, list_.next

    list_.next = None
    return dummy.next