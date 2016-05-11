# https://www.interviewbit.com/problems/max-sum-contiguous-subarray/
# in array, find a subarray with the maximum sum

def max_sub_array(arr):
    if_end_here_max = curr_max = arr[0]
    for i in arr[1:]:
        if_end_here_max = max(i, i + if_end_here_max)
        curr_max = max(curr_max, if_end_here_max)

    return curr_max
