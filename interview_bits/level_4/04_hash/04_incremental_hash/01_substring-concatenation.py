# https://www.interviewbit.com/problems/substring-concatenation/
from collections import Counter

def all_words_in_array(s, arr):
    if len(arr) == 0:
        return []
    cnt, len_total, len_one, res = Counter(arr), len(arr) * len(arr[0]), len(arr[0]), []
    for i in xrange(len(s) - len_total + 1):
        cnt_attempt, tmp = Counter(), s[i:i+len_total]
        for j in xrange(0, len_total, len_one):
            small_part = tmp[j:j + len_one]
            if small_part in cnt:
                cnt_attempt[small_part] += 1
            else:
                break

        if cnt == cnt_attempt:
            res.append(i)

    return res
