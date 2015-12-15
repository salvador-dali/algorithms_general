# https://www.hackerrank.com/contests/w13/challenges/sherlock-and-anagrams
# the main idea is to check whether it is better to swap the element or not
# so, when you swapping, you end up paying previous price + price for the swap
# and then you need to select the smaller of them
# basically O(1)
def res(w, b, x, y, z):
    return min(y + z, x) * b + min(x + z, y) * w

for i in xrange(input()):
    b, w = map(int, raw_input().split())
    x, y, z = map(int, raw_input().split())
    print res(w, b, x, y, z)
