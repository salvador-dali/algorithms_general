# https://www.interviewbit.com/problems/max-product-subarray/

def max_product(arr):
    m, curr_max, curr_min = arr[0], arr[0], arr[0]
    for i in arr[1:]:
        if i < 0:
            curr_max, curr_min = curr_min, curr_max

        curr_max = max(i, curr_max * i)
        curr_min = min(i, curr_min * i)
        m = max(m, curr_max)

    return m