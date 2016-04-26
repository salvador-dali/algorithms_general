# https://www.hackerrank.com/challenges/mark-and-toys
def max_toys(prices, rupees):
    prices.sort()
    s = 0
    for i in range(len(prices)):
        s += prices[i]
        if s > rupees:
            return i

n, k = map(int, raw_input().split())
prices = map(int, raw_input().split())
print max_toys(prices, k)