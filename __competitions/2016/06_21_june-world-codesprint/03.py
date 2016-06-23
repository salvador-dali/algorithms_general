scale = 16
num_of_bits = 8

def preprocess(a, b, c):
    s1 = bin(int(a, scale))[2:].zfill(num_of_bits)
    s2 = bin(int(b, scale))[2:].zfill(num_of_bits)
    s3 = bin(int(c, scale))[2:].zfill(num_of_bits)

    m = max(len(s1), len(s2), len(s3))

    s1 = '0' * (m - len(s1)) + s1
    s2 = '0' * (m - len(s2)) + s2
    s3 = '0' * (m - len(s3)) + s3
    return list(s1), list(s2), list(s3)

def findSolution(a, b, c, k):
    s1, s2, s3 = preprocess(a, b, c)

    additionalInvestigation = []
    for i in xrange(len(s1)):
        num = int(s1[i] + s2[i] + s3[i], 2)
        if num == 0 or num == 3:
            pass
        elif num == 1:
            s2[i] = '1'
            k -= 1
        elif num == 2:
            s2[i] = '0'
            k -= 1
        elif num == 4:
            s1[i] = '0'
            k -= 1
        elif num == 6:
            s1[i] = '0'
            s2[i] = '0'
            k -= 2
        else:
            additionalInvestigation.append(i)

    if k < 0:
        return '', '', False

    if k == 0:
        return ''.join(s1), ''.join(s2), True

    for i in additionalInvestigation:
        num = int(s1[i] + s2[i] + s3[i], 2)
        if num == 5:
            if k >= 2:
                s1[i] = '0'
                s2[i] = '1'
                k -= 2
        elif num == 7:
            s1[i] = '0'
            k -= 1

        if k == 0:
            return ''.join(s1), ''.join(s2), True

    return ''.join(s1), ''.join(s2), True

def convert(s):
    res = '%0*X' % ((len(s) + 3) // 4, int(s, 2))
    res = res.lstrip("0")
    if len(res) == 0:
        return '0'
    return res

def ful_normal(a, b, c, k):
    r1, r2, ok = findSolution(a, b, c, k)
    if not ok:
        return -1
    else:
        return convert(r1), convert(r2)

for i in xrange(input()):
    k = input()
    s1 = raw_input()
    s2 = raw_input()
    s3 = raw_input()
    res = ful_normal(s1, s2, s3, k)
    if res == -1:
        print -1
    else:
        print res[0]
        print res[1]