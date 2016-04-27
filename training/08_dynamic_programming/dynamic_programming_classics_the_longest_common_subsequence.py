# https://www.hackerrank.com/challenges/dynamic-programming-classics-the-longest-common-subsequence
def longest_common_subsequence(s1, s2):
    m, n = len(s1) + 1, len(s2) + 1
    M = [[0] * n for _ in xrange(m)]

    for i in xrange(1, m):
        for j in xrange(1, n):
            if s1[i - 1] == s2[j - 1]:
                M[i][j] = 1 + M[i - 1][j - 1]
            else:
                M[i][j] = max(M[i][j - 1], M[i - 1][j])

    res, x, y = [], len(M) - 1, len(M[0]) - 1
    while x or y:
        if M[x][y] == M[x - 1][y]:
            x -= 1
        elif M[x][y] == M[x][y - 1]:
            y -= 1
        else:
            res.append(s2[y - 1])
            x, y = x - 1, y - 1

    return res[::-1]

def longest_common_subsequence_improved(s1, s2):
    start, end, suffix = 0, 0, []
    for i in xrange(min(len(s1), len(s2))):
        if s1[i] == s2[i]:
            start += 1
        else:
            break

    prefix, s1, s2 = s1[:start], s1[start:], s2[start:]
    for i in xrange(1, min(len(s1), len(s2)) + 1):
        if s1[-i] == s2[-i]:
            end += 1
        else:
            break

    if end:
        suffix, s1, s2 = s1[-end:], s1[:-end], s2[:-end]

    res = prefix + longest_common_subsequence(s1, s2) + suffix
    return res

raw_input()
arr1, arr2 = map(int, raw_input().split()), map(int, raw_input().split())
print ' '.join(map(str, longest_common_subsequence_improved(arr1, arr2)))