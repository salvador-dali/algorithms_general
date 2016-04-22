# https://www.hackerrank.com/challenges/gem-stones
def dictFromString(s):
    d = {}
    for i in s:
        if i not in d:
            d[i] = 1

    return d

def reduceHash(d1, s):
    d2 = dictFromString(s)
    d_new = {}
    for i in d1:
        if i in d2:
            d_new[i] = 1

    return d_new

num = input()
hash1 = dictFromString(raw_input())

for i in range(1, num):
    hash1 = reduceHash(hash1, raw_input())

print len(hash1)