# https://www.hackerrank.com/challenges/the-love-letter-mystery
def numToPalindrome(s):
    l = len(s)
    return sum(abs(ord(s[i]) - ord(s[l - i - 1])) for i in range(l // 2))

for i in xrange(input()):
    print numToPalindrome(raw_input())