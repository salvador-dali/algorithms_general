# https://www.interviewbit.com/problems/maximum-longest-common-subsequence
def lcs_dp(s1, s2):
    M = [[0] * (len(s2) + 1) for _ in xrange(len(s1) + 1)]

    for i in xrange(1, len(s1) + 1):
        for j in xrange(1, len(s2) + 1):
            M[i][j] = max(M[i - 1][j], M[i][j - 1], 0 if s1[i - 1] != s2[j - 1] else M[i - 1][j - 1] + 1)

    return M[-1][-1]

def lcs(s1, s2):
    cnt, total = 0, 0
    for i in xrange(min(len(s1), len(s2))):
        if s1[i] == s2[i]:
            cnt += 1
        else:
            break

    s1, s2, total = s1[cnt:][::-1], s2[cnt:][::-1], cnt

    cnt = 0
    for i in xrange(min(len(s1), len(s2))):
        if s1[i] == s2[i]:
            cnt += 1
        else:
            break

    s1, s2, total = s1[cnt:][::-1], s2[cnt:][::-1], total + cnt


    return total + lcs_dp(s1, s2)

def lcs_reverse(s):
    max_so_far = 0
    res_j, res_r = 1, 0
    for i in xrange(1, len(s)):
        s1, s2 = s[:i], s[i:][::-1]
        if min(len(s1), len(s2)) < max_so_far:
            break
        r = lcs(s1, s2)
        if r > max_so_far:
            max_so_far = r
            res_r, res_j = r, i

    return [res_j, res_r]

print lcs_reverse("abbacaabcdaabaaababcabbccababbacabbaaaa")
# print lcs_reverse("aaaaaaaaaaabbaa")