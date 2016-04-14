# https://www.interviewbit.com/problems/roman-to-integer/
s = 'MMXIV'

def roman2integer(s):
    d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    res, prev = 0, 1000
    for i in s:
        if d[i] > prev:
            res += d[i] - 2 * prev
        else:
            res += d[i]
        prev = d[i]

    return res

