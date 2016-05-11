# https://www.interviewbit.com/problems/add-one-to-number/
# add one to a number which represents an array

def add_one(arr):
    carry = 1
    for i in xrange(len(arr) - 1, -1, -1):
        tmp = arr[i] + carry
        carry, arr[i] = tmp / 10, tmp % 10

    if carry:
        return [1] + arr

    for i in xrange(len(arr)):
        if arr[i] != 0:
            break

    return arr[i:]
