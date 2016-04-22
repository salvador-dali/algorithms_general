# https://www.hackerrank.com/challenges/make-it-anagram
def anagramDiff(s1, s2):
    h = {}
    for i in s1:
        if i in h:
            h[i] += 1
        else:
            h[i] = 1

    num = 0
    for i in s2:
        if i not in h:
            num += 1
        elif h[i] == 0:
            num += 1
        else:
            h[i] -= 1

    for i in h:
        if h[i]:
            num += h[i]

    return num

print anagramDiff(raw_input(), raw_input())