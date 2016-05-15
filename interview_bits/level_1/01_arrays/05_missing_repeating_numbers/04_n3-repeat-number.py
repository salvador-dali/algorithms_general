# https://www.interviewbit.com/problems/n3-repeat-number/

from collections import Counter
def repeatN_3(arr):
    cnt, bigger = Counter(), len(arr) / float(3)
    for el in arr:
        cnt[el] += 1
        if len(cnt) == 3:
            cnt = Counter({i: cnt[i] - 1 for i in cnt if cnt[i] > 1})

    d = {i: 0 for i in cnt}
    for el in arr:
        if el in d:
            d[el] += 1

    m = len(arr) / float(3)
    res = [i for i in d if d[i] > m]
    if len(res) == 0:
        return -1
    return res[0]



print repeatN_3(arr)