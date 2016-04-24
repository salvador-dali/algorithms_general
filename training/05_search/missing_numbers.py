# https://www.hackerrank.com/challenges/missing-numbers
# find the difference in two lists
def missingList(l1, l2):
    h1 = {}
    for i in l1:
        if i in h1:
            h1[i] += 1
        else:
            h1[i] = 1

    diff = []
    for i in l2:
        if i not in h1:
            diff.append(i)
        else:
            if h1[i] > 0:
                h1[i] -= 1
            else:
                diff.append(i)

    return diff

raw_input()
l1 = map(int, raw_input().split())
raw_input()
l2 = map(int, raw_input().split())

diff = list(set(missingList(l1, l2)))
diff.sort()
print ' '.join(map(str, diff))