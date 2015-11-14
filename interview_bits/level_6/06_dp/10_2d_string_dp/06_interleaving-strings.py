# https://www.interviewbit.com/problems/interleaving-strings/

def isInterleave(s1, s2, s3):
    if len(s1) + len(s2) != len(s3):
        return False

    match = [[False for _ in xrange(len(s2) + 1)] for _ in xrange(len(s1) + 1)]
    match[0][0] = True
    for i in xrange(1, len(s1) + 1):
        match[i][0] = match[i - 1][0] and s1[i - 1] == s3[i - 1]
    for j in xrange(1, len(s2) + 1):
        match[0][j] = match[0][j - 1] and s2[j - 1] == s3[j - 1]
    for i in xrange(1, len(s1) + 1):
        for j in xrange(1, len(s2) + 1):
            match[i][j] = (match[i - 1][j] and s1[i - 1] == s3[i + j - 1]) or (match[i][j - 1] and s2[j - 1] == s3[i + j - 1])
    return match[-1][-1]

# -------------

from collections import Counter

def full_solution(s1, s2, s3):
    if len(s1) + len(s2) != len(s3):
        return False
    if Counter(s1) + Counter(s2) != Counter(s3):
        return False

    hash_map = {}
    def obvious(s1, s2, s3):
        if (s1, s2, s3) in hash_map:
            return hash_map[(s1, s2, s3)]

        n1, n2, n3 = 0, 0, 0
        while n1 < len(s1) and n2 < len(s2) and n3 < len(s3):
            if s1[n1] != s3[n3] and s2[n2] != s3[n3]:
                return False

            if s1[n1] == s3[n3] and s2[n2] != s3[n3]:
                n1 += 1
                n3 += 1
            elif s2[n2] == s3[n3] and s1[n1] != s3[n3]:
                n2 += 1
                n3 += 1
            else:
                break

        s1, s2, s3 = s1[n1:], s2[n2:], s3[n3:]
        n1, n2, n3 = len(s1) - 1, len(s2) - 1, len(s3) - 1
        while n1 >= 0 and n2 >= 0 and n3 >= 0:
            if s1[n1] != s3[n3] and s2[n2] != s3[n3]:
                return False

            if s1[n1] == s3[n3] and s2[n2] != s3[n3]:
                n1 -= 1
                n3 -= 1
            elif s2[n2] == s3[n3] and s1[n1] != s3[n3]:
                n2 -= 1
                n3 -= 1
            else:
                break

        s1, s2, s3 = s1[:n1 + 1], s2[:n2 + 1], s3[:n3 + 1]
        if s1 == '' and s2 == '' and s3 == '':
            return True

        if s1 == '' and s2 == s3:
            return True

        if s2 == '' and s1 == s3:
            return True

        if s1 == '' or s2 == '':
            return False

        res = obvious(s1[1:], s2, s3[1:]) or obvious(s1, s2[1:], s3[1:])
        hash_map[(s1, s2, s3)] = res
        return res

    return obvious(s1, s2, s3)

s1, s2, s3 = 'aabcc', 'dbbca', 'aadbbcbcac'
print full_solution(s1, s2, s3)