# https://www.interviewbit.com/problems/best-time-to-buy-and-sell-stocks-i/
def stock(arr):
    if len(arr) < 2:
        return 0

    arr = [arr[i] - arr[i - 1] for i in xrange(1, len(arr))]
    curr_max, max_so_far = 0, 0
    for i in arr:
        curr_max = max(i, curr_max + i)
        max_so_far = max(max_so_far, curr_max)

    return max_so_far
