# https://www.interviewbit.com/problems/implement-strstr/
def findSubstringInString(s1, s2):
    if s1 == '':
        return -1

    for i in xrange(len(s2) - len(s1) + 1):
        if s1 == s2[i:i + len(s1)]:
            return i
    return -1

print findSubstringInString('aahla', 'ahla')