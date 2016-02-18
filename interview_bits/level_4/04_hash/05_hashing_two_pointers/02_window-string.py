# https://www.interviewbit.com/problems/window-string/
from collections import Counter

def countersEqual(etalon, current):
    if len(etalon) != len(current):
        return False
    for i in etalon:
        if i not in current or current[i] < etalon[i]:
            return False

    return True

def window2(s, t):
    cnt_etalon = Counter(t)
    p1, p2, n = 0, 0, len(s)
    best_length, pos_s, pos_e = len(s) + 10, -1, -1
    while p1 < n:
        cnt = Counter()
        for p2 in xrange(p1, n):
            if s[p2] in cnt_etalon:
                cnt[s[p2]] += 1
                if countersEqual(cnt_etalon, cnt):
                    for p1 in xrange(p1, p2 + 1):
                        if s[p1] in cnt_etalon:
                            cnt[s[p1]] -= 1
                        if not countersEqual(cnt_etalon, cnt):
                            if p2 - p1 < best_length:
                                best_length, pos_s, pos_e = p2 - p1, p1, p2
                            # print '\t', possible, s[p1:p2 + 1]
                            break
                    break
        p1 += 1

    if pos_s == -1:
        return ''

    return s[pos_s:pos_e + 1]

def minWindow(S, T):
    count1, count2 = Counter(T), Counter(T)
    count, start, minSize, minStart = len(T), 0, float('inf'), 0

    for end in range(len(S)):
        if S[end] in count2 and count2[S[end]] > 0:
            count1[S[end]] -= 1
            if count1[S[end]] >= 0:
                count -= 1

        if not count:
            while True:
                if S[start] in count2 and count2[S[start]] > 0:
                    if count1[S[start]] < 0:
                        count1[S[start]] += 1
                    else:
                        break
                start += 1

            if minSize > end-start+1:
                minSize = end-start+1
                minStart = start
    if minSize == float('inf'):
        return ''

    return S[minStart:minStart+minSize]


# s = 'abcdmxasma'
s = 'z3OyxTp7j3usoz2l0zmr8tJCocoNUvL1cVTWuroYKTluh60TsRvR8jNjiStkt2FNRxPtUn4ZTWSeqgClbFyPWqUHTaSRC5cY5JPVAW25IGusbMaRYmPWUOswP0QnU1BFYldSoDEV59efpkUXI6BQ6vnTAB4'
t = 'm'

s = 'ADOBECODEBANC'
t = 'ABC'
print window2(s, t)
print minWindow(s, t)