# https://www.hackerrank.com/challenges/chocolate-game
# the game which is played on non-decreasing heaps is a silver dollar game
from collections import Counter

def silverDollar(end):
    ret, val, cnt = 0, 0, Counter([0])
    for x in xrange(end, -1, -2):
        ret += cnt[num[x] ^ val]
        if x > 0:
            val ^= num[x] - num[x-1]
            ret += cnt[val]
            cnt[val] += 1
    return ret

n, num = input(), map(int, raw_input().split())
print n * (n - 1) / 2 - silverDollar(n - 1) - silverDollar(n - 2)