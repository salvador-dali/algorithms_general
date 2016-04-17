# https://www.interviewbit.com/problems/different-bits-sum-pairwise/
mod = 10**9 + 7
def getXor(arr):
    m = max(arr)
    bit_num = 0
    while m:
        m /= 2
        bit_num += 1

    divisor, total_sum = 1, 0
    for i in xrange(bit_num):
        sum_of_ones = 0
        for val in arr:
            sum_of_ones += val / divisor % 2

        total_sum += sum_of_ones * (len(arr) - sum_of_ones) * 2
        divisor *= 2

    return total_sum % mod
