# https://www.hackerrank.com/challenges/greedy-florist/
# you have K people and an array of elements.
# each element cost Ci * (n + 1), where N is the number of flowers already bought by this person
#
# greedy algorithm, sort all the list in a reversed order, then iterate through all
# of them in pairs of K elements and then sum them all up
def flowers(k, c):
    from math import ceil
    c.sort(reverse=True)
    s, l = 0, len(c)
    iterations = int(ceil(l / float(k)))

    for i in range(iterations):
        s += sum(c[i * k: i * k + k]) * (i + 1)

    return s

a, b = map(int, raw_input().split())
arr = list(map(int, raw_input().split()))
print flowers(b, arr)