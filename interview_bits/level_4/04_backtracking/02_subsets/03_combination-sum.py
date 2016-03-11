# https://www.interviewbit.com/problems/combination-sum/
def summation(arr, target):
    res = set([])
    def generate_all(elements, arr, left):
        if left == 0:
            res.add(tuple(sorted(elements)))
            return
        if left < 0:
            return

        for i in arr:
            generate_all(elements + [i], arr, left - i)

    if any([i == target for i in arr]):
        res.add(tuple([target]))

    arr = list({i for i in arr if i < target})
    arr.sort()

    generate_all([], arr, target)
    res = list(res)
    res.sort()
    return [list(i) for i in res]