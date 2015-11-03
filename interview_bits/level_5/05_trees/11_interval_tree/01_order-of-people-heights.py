# https://www.interviewbit.com/problems/order-of-people-heights/
arr_h = [5, 3, 2, 6, 1, 4]
arr_p = [0, 1, 2, 0, 3, 2]


def find_order(arr_h, arr_p):
    arr = zip(arr_h, arr_p)
    arr.sort()
    print arr
    res = [-1] * len(arr)
    for num, pos in arr:
        start = -1
        for i in xrange(len(arr)):
            if res[i] == -1:
                start += 1
                if start == pos:
                    res[i] = num
                    break
    return res


