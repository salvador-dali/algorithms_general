# https://www.hackerrank.com/contests/w13/challenges/sherlock-and-anagrams
# select all substrings of the string and for each of these substrings
# get sorted string (ordered all the characters) and save the number of each of these unique strings.
# these numbers will catch all possible strings that can be anagrams for each other
# if there are N strings, then it will have N * (N - 1) / 2 ordered pairs
def getSubstringsAnagrams(s):
    l, h, total = len(s), {}, 0
    for i in xrange(l):
        for j in xrange(i, l):
            sorted_string = ''.join(sorted(s[i:j + 1]))
            if sorted_string in h:
                h[sorted_string] += 1
            else:
                h[sorted_string] = 1

    return sum(i * (i - 1) / 2 for i in h.values())

for i in xrange(input()):
    print getSubstringsAnagrams(raw_input())