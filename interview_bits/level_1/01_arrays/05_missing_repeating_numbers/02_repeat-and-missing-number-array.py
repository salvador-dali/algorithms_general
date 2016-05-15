# https://www.interviewbit.com/problems/repeat-and-missing-number-array/
# having a permutation of [1, n], one number was removed, and another number was written instead of
# it. Find these numbers

def repeat_and_missing(arr):
    s1, s2 = sum(arr), sum(i*i for i in arr)

    n = len(arr)
    r1, r2 = n * (n + 1) / 2, n * (n + 1) * (2 * n + 1) / 6

    x_minus_y = r1 - s1
    x_plus_y = (r2 - s2) / x_minus_y

    return (x_plus_y + x_minus_y) / 2, (x_plus_y - x_minus_y) / 2