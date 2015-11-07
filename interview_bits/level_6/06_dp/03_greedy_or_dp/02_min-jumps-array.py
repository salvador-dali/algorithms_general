# https://www.interviewbit.com/problems/min-jumps-array/
def min_jumps(arr):
    i, maximum, next_val, num = 0, 0, 0, 0
    n = len(arr) - 1
    while i < n and next_val < n:
        maximum = max(maximum, i + arr[i])
        if i == next_val:
            if maximum == next_val:
                return -1

            next_val = maximum
            num += 1

        i += 1

    return num
