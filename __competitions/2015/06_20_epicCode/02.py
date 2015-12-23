from collections import Counter
input()
counter = Counter(raw_input())
print sum(v * (v + 1)/2 for v in counter.itervalues())