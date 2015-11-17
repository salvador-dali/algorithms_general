# https://www.interviewbit.com/problems/highest-product/
def biggest_product_small(arr):
    m, n = float('-inf'), len(arr)

    for i in xrange(n):
        for j in xrange(i + 1, n):
            for k in xrange(j + 1, n):
                m = max(m, arr[i] * arr[j] * arr[k])

    return m


def biggest_product(arr):
    if len(arr) < 3:
        return 0
    if len(arr) <= 6:
        return biggest_product_small(arr)
    arr.sort()
    return biggest_product_small(arr[:3] + arr[-3:])


arr = [-1, -7, -9, 6, -9, 19, 17, -6, -1, 0, 20]
print str(len(arr)) + ' ' + ' '.join(map(str, arr))
print
print biggest_product(arr)