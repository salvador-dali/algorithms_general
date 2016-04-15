# https://www.interviewbit.com/problems/count-and-say/

def getNext(s):
    res, prev, num = '', s[0], 1
    for i in s[1:] + 'x':
        if i != prev:
            res += str(num) + prev
            num = 1
            prev = i
        else:
            num += 1

    return res

def count_say(n):
    start = '1'
    for i in xrange(n - 1):
        start = getNext(start)
    return start
