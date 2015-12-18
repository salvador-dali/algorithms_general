def isFunny(s):
    l = len(s)
    for i in xrange(1, l):
        if abs(ord(s[i]) - ord(s[i - 1])) != abs(ord(s[l - i]) - ord(s[l - i - 1])):
            return False

    return True

for i in xrange(input()):
    print 'Funny' if isFunny(raw_input()) else 'Not Funny'