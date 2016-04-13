# https://www.interviewbit.com/problems/length-of-last-word/
def last_word(s):
    if s == '':
        return 0
    start = 0
    last = 0
    for i in xrange(len(s)):
        letter = s[i]
        if letter == ' ':

            tmp = i - start
            start = i + 1
            if tmp != 0:
                last = tmp

    if s[-1] != ' ':
        last = i - start + 1
    return last
