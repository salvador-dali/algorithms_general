# https://www.interviewbit.com/problems/get-mode-array-updates
arr = [2, 2, 2, 3, 3]
query = [(1, 3), (5, 4), (2, 4)]

from collections import Counter

def update(arr, queries):
    cnt = Counter(arr)

    res = []
    for i, v in queries:
        prev = arr[i - 1]
        cnt[prev] -= 1
        cnt[v] += 1
        arr[i - 1] = v
        res.append(cnt.most_common(1))

    return res

update(arr, query)