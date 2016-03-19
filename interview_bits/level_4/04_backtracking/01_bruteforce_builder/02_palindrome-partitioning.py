# https://www.interviewbit.com/problems/palindrome-partitioning/
def cmp(a, b):
    return tuple(len(i) for i in a) < tuple(len(i) for i in b)

def is_all_palindromes(arr):
    return all(s == s[::-1] for s in arr)

def solution(arr):
    res, have_seen = set([]), set([])
    def generate(arr):
        if len(arr) == 0:
            return

        tuple_ = tuple(arr)
        if tuple_ not in have_seen:
            have_seen.add(tuple_)
            if is_all_palindromes(arr):
                res.add(tuple_)
            for i in xrange(len(arr) - 1):
                generate(arr[:i] + [arr[i] + arr[i+1]] + arr[i+2:])

    generate(list(arr))
    res = list(res)
    res.sort()

    return [list(i) for i in res]

print len(solution('cccaacbcaabb'))
