from copy import copy
C, B = map(int, raw_input().split())

cities = [[tuple(map(float, raw_input().split())) for i in xrange(input())] for _ in xrange(C)]

prices = {0: 0}
for city in cities:
    new_prices = {}
    for price, score in prices.iteritems():
        for p, s in city:
            p_, s_ = price + int(p), score + s
            if p_ <= B:
                if p_ not in new_prices:
                    new_prices[p_] = s_
                elif new_prices[p_] < s_:
                    new_prices[p_] = s_

    prices = copy(new_prices)

maximum = -1
for p, s in prices.iteritems():
    maximum = max(maximum, s)

if maximum == -1:
    print -1
else:
    print "%.2f" % maximum
