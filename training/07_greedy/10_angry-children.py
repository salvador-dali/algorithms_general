# https://www.hackerrank.com/challenges/angry-children
n, k = input(), input()
candies = [input() for _ in xrange(n)]
candies.sort()

minimum = candies[-1]
for i in xrange(len(candies) - k + 1):
    d = candies[i + k - 1] - candies[i]
    if d < minimum:
        minimum = d

print minimum