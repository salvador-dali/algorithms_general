# https://www.hackerrank.com/contests/101hack19/challenges/two-strings
# just check whether at least one symbol is in both strings
def twoStrings(a, b):
    if len(set(a) & set(b)):
        print 'YES'
    else:
        print 'NO'

for i in xrange(input()):
    twoStrings(raw_input(), raw_input())