# https://www.interviewbit.com/problems/min-sum-path-in-matrix/
def solution(arr):
    curr_sum, prev_row = 0, []
    for i in arr[0]:
        curr_sum += i
        prev_row.append(curr_sum)

    n = len(arr[0])

    arr[0], i = prev_row, 0
    for i in xrange(1, len(arr)):
        for j in xrange(n):
            if j == 0:
                arr[i][j] += arr[i - 1][j]
            else:
                arr[i][j] += min(arr[i][j - 1], arr[i - 1][j])

    return arr[i][n - 1]
