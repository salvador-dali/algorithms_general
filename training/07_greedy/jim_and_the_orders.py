# https://www.hackerrank.com/challenges/jim-and-the-orders
arr = [(sum(map(int, raw_input().split())), i + 1) for i in xrange(input())]
arr.sort()
print " ".join([str(i[1]) for i in arr])