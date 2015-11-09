# https://www.interviewbit.com/problems/best-time-to-buy-and-sell-stocks-ii/
def maximum(arr):
    return sum(0 if arr[i + 1] - arr[i] < 0 else arr[i + 1] - arr[i] for i in xrange(len(arr) - 1))
