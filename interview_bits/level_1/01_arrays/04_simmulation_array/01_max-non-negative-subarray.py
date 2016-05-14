# https://www.interviewbit.com/problems/max-non-negative-subarray/
def maxSubArray(arr):
    arr.append(-1)
    is_searching = False
    best_start, best_end, best_sum, best_len = -1, -1, -1, -1
    curr_start, curr_end, curr_sum, curr_len = -1, -1, -1, -1

    for i in xrange(len(arr)):
        el = arr[i]
        if el >= 0:
            if not is_searching:
                curr_start, curr_sum, curr_len, is_searching = i, el, 1, True
            else:
                curr_sum, curr_len = curr_sum + el, curr_len + 1
        else:
            if is_searching:
                curr_end = i
                if curr_sum > best_sum:
                    best_start, best_end, best_sum, best_len = curr_start, curr_end, curr_sum, curr_len
                elif curr_sum == best_sum and curr_len > best_len:
                    best_start, best_end, best_sum, best_len = curr_start, curr_end, curr_sum, curr_len
            is_searching = False

    return arr[best_start:best_end]

