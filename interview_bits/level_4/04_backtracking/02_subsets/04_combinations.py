# https://www.interviewbit.com/problems/combinations/
def all_combinations(n, k):
    if k > n:
        return []
    res = []
    def combinations(arr, curr_comb, cur_index, num):
        if len(curr_comb) == num:
            res.append(curr_comb)
            return

        if cur_index == len(arr):
            return

        for i in xrange(cur_index, len(arr)):
            combinations(arr, curr_comb + [arr[i]], i + 1, num)

    combinations(range(1, n + 1), [], 0, k)
    return res
