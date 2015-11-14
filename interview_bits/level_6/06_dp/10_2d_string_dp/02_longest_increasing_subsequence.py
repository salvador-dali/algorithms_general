# https://www.interviewbit.com/problems/longest-increasing-subsequence/
def longest_increasing(d):
    l = []
    for i in range(len(d)):
        l.append(max([l[j] for j in range(i) if l[j][-1] < d[i]] or [[]], key=len) + [d[i]])
    return len(max(l, key=len))
