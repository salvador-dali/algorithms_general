# https://www.hackerrank.com/challenges/jesse-and-cookies
from heapq import heappush, heappop, heapify

def work(items, k):
    heapify(items)
    for i in xrange(1, len(items) + 1):
        try:
            el1 = heappop(items)
            if el1 >= k:
                return i - 1
            el2 = heappop(items)
            heappush(items, el1 + el2 * 2)
        except:
            return -1
n, k = map(int, raw_input().split())
items = map(int, raw_input().split())
print work(items, k)