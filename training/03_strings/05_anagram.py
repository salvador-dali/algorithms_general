# https://www.hackerrank.com/challenges/anagram
def anagram(s):
    if len(s) % 2:
        return -1

    s1, s2, hash1, diff = s[0:len(s) / 2], s[len(s) / 2:], {}, 0
    for i in s1:
        if i in hash1:
            hash1[i] += 1
        else:
            hash1[i] = 1

    for i in s2:
        if i in hash1:
            if hash1[i] > 0:
                hash1[i] -= 1
            else:
                diff += 1
        else:
            diff += 1

    return diff

for i in xrange(input()):
    print anagram(raw_input())