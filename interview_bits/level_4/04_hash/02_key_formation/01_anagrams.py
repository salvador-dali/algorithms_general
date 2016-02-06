# https://www.interviewbit.com/problems/anagrams/
from collections import defaultdict

def wordToVec(word):
    vec = [0] * 27
    for i in word:
        vec[ord(i) - 97] += 1
    return tuple(vec)

def anagrams(arr):
    h = defaultdict(list)
    for i in xrange(len(arr)):
        h[wordToVec(arr[i])].append(i + 1)

    res = [v for k, v in h.iteritems()]
    res.sort()
    return res


arr = [ "abbbaabbbabbbbabababbbbbbbaabaaabbaaababbabbabbaababbbaaabbabaabbaabbabbbbbababbbababbbbaabababba", "abaaabbbabaaabbbbabaabbabaaaababbbbabbbaaaabaababbbbaaaabbbaaaabaabbaaabbaabaaabbabbaaaababbabbaa", "babbabbaaabbbbabaaaabaabaabbbabaabaaabbbbbbabbabababbbabaabaabbaabaabaabbaabbbabaabbbabaaaabbbbab", "bbbabaaabaaaaabaabaaaaaaabbabaaaabbababbabbabbaabbabaaabaabbbabbaabaabaabaaaabbabbabaaababbaababb", "abbbbbbbbbbbbabaabbbbabababaabaabbbababbabbabaaaabaabbabbaaabbaaaabbaabbbbbaaaabaaaaababababaabab", "aabbbbaaabbaabbbbabbbbbaabbababbbbababbbabaabbbbbbababaaaabbbabaabbbbabbbababbbaaabbabaaaabaaaaba", "abbaaababbbabbbbabababbbababbbaaaaabbbbbbaaaabbaaabbbbbbabbabbabbaabbbbaabaabbababbbaabbbaababbaa", "aabaaabaaaaaabbbbaabbabaaaabbaababaaabbabbaaaaababaaabaabbbabbababaabababbaabaababbaabbabbbaaabbb" ]
def anagrams2(arr):
    h = defaultdict(list)
    for i in xrange(len(arr)):
        h[''.join(sorted(arr[i]))].append(i + 1)

    res = [v for k, v in h.iteritems()]
    res.sort()
    return res
print anagrams2(arr)

