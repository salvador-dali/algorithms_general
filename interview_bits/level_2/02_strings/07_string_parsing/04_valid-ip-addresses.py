# https://www.interviewbit.com/problems/valid-ip-addresses/
def is_valid_num(s):
    if s == '0':
        return True
    if s[0] == '0':
        return False
    return int(s) <= 255

def valid_ip(s):
    if len(s) < 4 or len(s) > 12:
        return []

    res = []
    n = len(s)
    for i in xrange(1, n):
        for j in xrange(i + 1, n):
            for k in xrange(j + 1, n):
                s1, s2, s3, s4 = s[:i], s[i:j], s[j:k], s[k:]
                if is_valid_num(s1) and is_valid_num(s2) and is_valid_num(s3) and is_valid_num(s4):
                    res.append(s1 + '.' + s2 + '.' + s3 + '.' + s4)
    res.sort()
    return res
