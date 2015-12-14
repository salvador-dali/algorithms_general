# https://www.hackerrank.com/contests/101hack19/challenges/antipalindromic-strings
# the first character can be selected M possible times, the second M - 1, the third M - 2. Only if M - 2 is not 0
# all other elements can be selected m - 2 times.
def antipalindrome(n, m):
    total, MOD = 1, 10**9 + 7
    for i in xrange(min(3, n)):
        total *= (m - i)
    total %= MOD

    if not total:
        return 0

    if n - 3 < 1:
        return total

    return (total * pow(m - i, n - 3, MOD)) % MOD

for i in xrange(input()):
    n, m = map(int, raw_input().split())
    print antipalindrome(n, m)