from collections import defaultdict

input()
d = defaultdict(list)
arr = map(int, raw_input().split())
for i, el in enumerate(arr):
    d[el].append(i)

minimum = 10 ** 9
for i in d:
    if len(d[i]) > 1:
        for first, second in zip(d[i], d[i][1:]):
            minimum = min(minimum, abs(second - first))

if minimum == 10 ** 9:
    print -1
else:
    print minimum
