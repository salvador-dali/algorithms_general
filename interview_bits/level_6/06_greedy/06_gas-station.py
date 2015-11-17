# https://www.interviewbit.com/problems/gas-station/
def find_position(arr_gas, arr_cost):
    arr = [arr_gas[i] - arr_cost[i] for i in xrange(len(arr_gas))]
    if sum(arr) < 0:
        return -1

    cur_gas, selected_pos = -1, 0
    for i in xrange(len(arr)):
        if cur_gas < 0:
            if arr[i] > 0:
                selected_pos = i
                cur_gas = arr[i]
        else:
            cur_gas += arr[i]

    return selected_pos