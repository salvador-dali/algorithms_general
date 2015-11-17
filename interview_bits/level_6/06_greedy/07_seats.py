# https://www.interviewbit.com/problems/seats/
def solution(s):
    for p_s in xrange(len(s)):
        if s[p_s] == 'x':
            break

    for p_e in xrange(len(s) - 1, -1, -1):
        if s[p_e] == 'x':
            break

    s = s[p_s:p_e + 1]
    print s
