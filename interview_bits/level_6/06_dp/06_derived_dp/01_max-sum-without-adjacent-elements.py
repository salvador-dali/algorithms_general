# https://www.interviewbit.com/problems/max-sum-without-adjacent-elements/
def find_sum(matrix):
    arr = [max(matrix[0][i], matrix[1][i]) for i in xrange(len(matrix[0]))]
    if len(arr) == 0:
        return 0
    if len(arr) == 1:
        return arr[0]

    tmp = [0] * len(arr)
    tmp[0], tmp[1] = arr[0], arr[1]

    for i in xrange(2, len(arr)):
        start = 0 if i - 4 < 0 else i - 4
        tmp[i] = max(val + arr[i] for val in tmp[start: i - 1])

    return max(tmp[-4:])
