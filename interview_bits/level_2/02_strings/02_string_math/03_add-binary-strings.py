# https://www.interviewbit.com/problems/add-binary-strings/

def sum_binary(s1, s2):
    if len(s2) > len(s1):
        s1, s2 = s2, s1
    s2 = '0' * (len(s1) - len(s2)) + s2

    carry = 0
    res = []
    for i in xrange(len(s2) - 1, -1, -1):
        addition = int(s1[i]) + int(s2[i]) + carry
        res.append(addition % 2)
        carry = addition / 2

    if carry:
        res.append(carry)

    return ''.join(map(str, res[::-1]))
