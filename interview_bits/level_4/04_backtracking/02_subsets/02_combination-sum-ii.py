# https://www.interviewbit.com/problems/combination-sum-ii/
def sum_to_n(numbers, n):
    numbers = [i for i in numbers if i <= n]
    numbers.sort()

    res = [[]]
    for el in numbers:
        res += [r + [el] for r in res]

    real_res = list({tuple(i) for i in res if sum(i) == n})
    real_res.sort()
    return [list(i) for i in real_res]
