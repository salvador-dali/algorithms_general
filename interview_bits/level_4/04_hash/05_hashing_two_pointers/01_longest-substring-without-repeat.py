# https://www.interviewbit.com/problems/longest-substring-without-repeat/
def longest_non_repeating(s):
    n, maximum, p1, p2 = len(s), 0, 0, 0
    while p1 < n:
        p2, h = p1, {}
        while p2 < n:
            if s[p2] in h:
                maximum = max(maximum, len(h))
                p1 = h[s[p2]] + 1
                h[s[p2]] = p2
                break
            else:
                h[s[p2]] = p2
            p2 += 1
        if p2 == n:
            return max(maximum, len(h))

    return maximum
