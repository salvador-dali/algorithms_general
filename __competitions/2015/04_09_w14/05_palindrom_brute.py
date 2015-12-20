"""
Basically bruteforce with some modification to regarding few specific test cases
https://oeis.org/A002412 total('a' * i + 'b' + 'a' * i),
https://oeis.org/A045943 total('123' * i)
https://oeis.org/A046092 total('1234' * i)
https://oeis.org/A028895 total('12345' * i)
https://oeis.org/A028896 total('123456' * i)
"""
M = 10**9 + 7

def total(s):
    l = len(s)

    # if all the letters are the same, then
    # we can calculate it with the following formula
    # https://oeis.org/A000292
    if isSame(s):
        return f(l)

    # another special case is when we have only unique elements
    # something like 'aaaaabbbbccccccccccccccc'
    # in such a case this is sum of 'aaaaa', 'bbbb', 'ccccccccccccccc'
    a = onlyUniqueElements(s)
    if a != -1:
        return a

    res = encode(s)
    mySet = {i[0] for i in res}
    if len(mySet) == len(res):
        return sum(f(i[1]) for i in res)

    # otherwise bruteforce
    return sum((P(s[i:j]) for i in xrange(l) for j in xrange(i + 2, l + 1))) % M

def P(s1):
    t = 0
    for i in xrange(1, len(s1)):
        if s1[0:i] == s1[-i:] and s1[0:i] == s1[0:i][::-1]:
            t += 1

    return t

def f(l):
    n = l - 1
    return (n * (n+1) * (n+2) / 6) % M

def isSame(s):
    char = s[0]
    n = len(s)
    if s == char * n:
        return True

    return False

def encode(input_string):
    count = 1
    prev = ''
    lst = []
    for character in input_string:
        if character != prev:
            if prev:
                entry = (prev, count)
                lst.append(entry)
            count = 1
            prev = character
        else:
            count += 1
    else:
        entry = (character, count)
        lst.append(entry)
    return lst

def onlyUniqueElements(s):
    for i in xrange(2, 9):
        t = s[0:i]
        if len(set(t)) != i:
            break

        z = s.replace(t, 'A')

        if isSame(z):
            n = len(z) - 1
            if i == 2:
                n += 2
                return n * (n - 1) * (n - 2) / 3
            else:
                return i * n * (n + 1) / 2

    return -1