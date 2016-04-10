# https://www.interviewbit.com/problems/longest-palindromic-substring/
# http://difusal.blogspot.com/2014/08/manachers-algorithm-longest-palindromic.html
# http://stackoverflow.com/q/10468208/1090562
# https://www.akalin.com/longest-palindrome-linear-time
def longestPalindrome(s):
    if len(s) <= 1:
        return s

    s = ''.join(['^'] + ['#' + i for i in s] + ['#$'])
    P, maxPalCenterID = [0] * len(s), 0

    for i in xrange(1, len(s) - 1):
        while s[i + 1 + P[i]] == s[i - 1 - P[i]]:
            P[i] += 1

        if P[i] > P[maxPalCenterID]:
            maxPalCenterID = i

    return P

def longest(original):
    s = ''.join(['^'] + ['#' + i for i in original] + ['#$'])
    P, C, R, maxPalCenterID = [0] * len(s), 0, 0, 1
    for i in xrange(1, len(s) - 1):
        P[i] = min(R - i, P[2 * C - i]) if R > i else 0
        while s[i + 1 + P[i]] == s[i - 1 - P[i]]:
            P[i] += 1

            if P[i] > P[maxPalCenterID]:
                maxPalCenterID = i

            if i + P[i] > R:
                C, R = i, i + P[i]

    maxPalSize = P[maxPalCenterID]
    palStartID = (maxPalCenterID - 1 - maxPalSize) / 2
    return original[palStartID:palStartID + maxPalSize]
