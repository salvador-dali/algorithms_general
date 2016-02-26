# https://www.interviewbit.com/problems/distinct-numbers-in-window/
from collections import Counter

def all_distinct(arr, k):
    hash_object = Counter(arr[:k])
    res = [len(hash_object)]
    for i in xrange(k, len(arr)):
        if hash_object[arr[i - k]] == 1:
            del hash_object[arr[i - k]]
        else:
            hash_object[arr[i - k]] -= 1

        hash_object[arr[i]] += 1
        res.append(len(hash_object))

    return res