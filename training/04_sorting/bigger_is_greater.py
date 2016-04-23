# Given a list of elements LIST_1, rearrange the elements to construct another list LIST_2
# in such a way that, it is lexicographically greater than LIST_1.
# In case of multiple possible answers, find the lexicographically smallest one.
# if no bigger element exist, than return - 1
# works in O(n)
def biggest(arr):
    l = len(arr)

    # if the list is sorted in reversed order, then there is no number
    if all(arr[i] >= arr[i + 1] for i in xrange(len(arr) - 1)):
        return -1

    # iterate over the elements in reversed order
    # till we will find two elements that can be swapped
    # A and B can be swapped if B > A
    for i in xrange(1, l):
        if arr[l - i] > arr[l - i - 1]:
            break

    index = l - i - 1
    el = arr[index]

    # find the smallest element that is bigger than EL in the array,
    # that we already iterated through
    curMin, indexMin = 999999, 0
    for i in xrange(index + 1, l):
        if el < arr[i] < curMin:
            curMin = arr[i]
            indexMin = i

    # now swap the element ARR[INDEX] and ARR[INDEXMIN]
    tmp = arr[index]
    arr[index] = arr[indexMin]
    arr[indexMin] = tmp

    # sort the rest of the elements
    arr[index + 1:] = sorted(arr[index + 1:])
    return arr

# the same, but if a string is given
# https://www.hackerrank.com/challenges/bigger-is-greater/editorial
def biggestString(s):
    res = biggest([ord(i) for i in list(s)])
    return -1 if res == -1 else ''.join([chr(j) for j in res])

# working with a list
print biggest([1, 5, 6, 9, 6, 2, 1])

# working with a string
print biggestString('abcddef')
