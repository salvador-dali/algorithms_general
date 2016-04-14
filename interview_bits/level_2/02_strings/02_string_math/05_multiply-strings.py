# https://www.interviewbit.com/problems/multiply-strings/
def summation(a, b):
    if len(b) > len(a):
        a, b = b, a

    a = '0' + a
    b = '0' * (len(a) - len(b)) + b

    res, carry = [], 0
    for i in xrange(len(a) - 1, -1, -1):
        s = int(a[i]) + int(b[i]) + carry
        res.append(s % 10)
        carry = s / 10

    res = ''.join(map(str, res[::-1]))
    if res[0] == '0':
        return res[1:]
    return res

def multiplyByOneDigit(a, b):
    res, carry, b = [], 0, int(b)
    for i in xrange(len(a) - 1, -1, -1):
        s = int(a[i]) * b + carry
        res.append(s % 10)
        carry = s / 10

    if carry:
        res.append(carry)

    return ''.join(map(str, res[::-1]))

def multiply(a, b):
    if len(b) > len(a):
        a, b = b, a

    s = '0'
    for i in xrange(len(b) - 1, -1, -1):
        s = summation(s, multiplyByOneDigit(a, b[i]) + '0' * (len(b) - i - 1))

    s = s.lstrip("0")
    if s == '':
        return '0'
    return s
