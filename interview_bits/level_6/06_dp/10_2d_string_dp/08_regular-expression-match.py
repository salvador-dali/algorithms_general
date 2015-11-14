# https://www.interviewbit.com/problems/regular-expression-match/

def remove_first(s1, s2):
    m, i = min(len(s1), len(s2)), 0
    while i < m and (s1[i] == s2[i] or s2[i] == '?'):
        i += 1

    s1, s2 = s1[i:], s2[i:]
    if not len(s1) and not len(s2):
        return 1, None, None

    if len(s1) and not len(s2):
        return 0, None, None

    if len(s1) and len(s2) and s2[0] != '*':
        return 0, None, None

    return None, s1[::-1], s2[::-1]

def remove_useless_stars(s):
    prev, res = '', ''
    for i in s:
        if i != prev or prev != '*':
            res += i
            prev = i
    return res

def dp(s1, s2):
    n1, n2 = len(s1), len(s2)
    prev = [1] + [0] * n1
    curr = [0] * (n1 + 1)
    for i in xrange(n2):
        if s2[i] == '*':
            for j in xrange(n1 + 1):
                curr[j] = 1 if prev[j] or curr[j - 1] else 0
        else:
            for j in xrange(1, n1 + 1):
                curr[j] = 1 if prev[j - 1] and (s2[i] == s1[j - 1] or s2[i] == '?') else 0

        prev = curr[::]
        curr = [0] * (n1 + 1)

    return prev[-1]

def regular_expression(s1, s2):
    res, s1, s2 = remove_first(s1, s2)
    if res is not None:
        return res

    res, s1, s2 = remove_first(s1, s2)
    if res is not None:
        return res

    s2 = remove_useless_stars(s2)
    if len(s2) - s2.count('*') > len(s1):
        return 0

    return dp(s1, s2)

print regular_expression('aab', '*a*b')
