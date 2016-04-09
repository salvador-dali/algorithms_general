# https://www.interviewbit.com/problems/atoi/

def atoi(s):
    s = s.strip().split(' ')[0]
    digits = set([str(i) for i in xrange(10)])
    if s == '':
        return 0

    sign = 1
    if s[0] == '-':
        sign = -1
        s = s[1:]
    elif s[0] == '+':
        sign = 1
        s = s[1:]

    res = ''
    for i in s:
        if i not in digits:
            break
        else:
            res += i

    if res == '':
        return 0

    n = sign * int(res)
    if n >= 2147483647:
        return 2147483647
    if n <= -2147483648:
        return -2147483648

    return n
